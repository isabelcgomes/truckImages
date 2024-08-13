import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models


class EarlyStoppingAtMinLoss(keras.callbacks.Callback):
    def __init__(self, patience=0):
        super(EarlyStoppingAtMinLoss, self).__init__()
        self.patience = patience
        self.best_weights = None

    def on_train_begin(self, logs=None):
        self.wait = 0
        self.stopped_epoch = 0
        self.best = np.Inf

    def on_epoch_end(self, epoch, logs=None):
        current = logs.get("val_loss")
        if np.less(current, self.best):
            self.best = current
            self.wait = 0
            self.best_weights = self.model.get_weights()
        else:
            self.wait += 1
            if self.wait >= self.patience:
                self.stopped_epoch = epoch
                self.model.stop_training = True
                print("Restoring model weights from the end of the best epoch.")
                self.model.set_weights(self.best_weights)

    def on_train_end(self, logs=None):
        if self.stopped_epoch > 0:
            print("Epoch %05d: early stopping" % (self.stopped_epoch + 1))

datadir = 'images'

generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255,
                                                            validation_split=0.3)
train_gen = generator.flow_from_directory(directory=datadir,
                                          batch_size=32,
                                          target_size=(128, 128),
                                          subset='training')
val_gen   = generator.flow_from_directory(directory=datadir,
                                          batch_size=32,
                                          target_size=(128, 128),
                                          subset='validation')



base_model = keras.applications.Xception(
    weights="imagenet",
    input_shape=(128, 128, 3),
    include_top=False,
)
base_model.trainable = True

inputs = keras.Input(shape=(128, 128, 3))

x = base_model(inputs, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dropout(0.3)(x)

outputs = keras.layers.Dense(10)(x)

fine_tune_at = 100
for layer in base_model.layers[:fine_tune_at]:
  layer.trainable =  False

model_tl = keras.Model(inputs, outputs)


init = time.time()

model_tl.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001),
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['categorical_accuracy'])

model_tl.fit(train_gen, epochs = 100,
             callbacks=[EarlyStoppingAtMinLoss()],
             validation_data = val_gen
            )

end = time.time()
print(f'Tempo de execução: {"%.2f" %((end - init)/60)} minutos')

evaluation = model_tl.evaluate(val_gen)

print(evaluation)

predicted_classes = model_tl.predict(val_gen)
predicted = predicted_classes.argmax(1)

y_values = [f"\n\n\n\n{key}" for key in val_gen.class_indices.keys()]


cm = confusion_matrix(val_gen.classes, predicted)

plt.figure(figsize = (14,10))
sns.heatmap(cm, annot=True)
plt.xticks(list(val_gen.class_indices.values()),val_gen.class_indices.keys(), rotation=45)
plt.yticks(list(val_gen.class_indices.values()),y_values, rotation=0)
plt.savefig("TCC_ConfusionMatrix")

num_classes = 10
print(classification_report(val_gen.classes, predicted, target_names=val_gen.class_indices.keys()))