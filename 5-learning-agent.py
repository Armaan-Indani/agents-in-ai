import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

data = pd.read_csv('my_schedule.csv')

data['Hour'] = data['Time'].apply(lambda x: int(x.split(':')[0]))

label_encoder = LabelEncoder()
data['Activity_Code'] = label_encoder.fit_transform(data['Activity'])

X = data[['DayOfWeek', 'Hour', 'Is_Holiday']].values
y = data['Activity_Code'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True)

num_classes = len(np.unique(y))

y_train_categorical = tf.keras.utils.to_categorical(y_train, num_classes)
y_test_categorical = tf.keras.utils.to_categorical(y_test, num_classes)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train_categorical, epochs=500, batch_size=8, verbose=0, validation_data=(X_test, y_test_categorical))

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

loss, accuracy = model.evaluate(X_test, y_test_categorical, verbose=0)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

y_pred_proba = model.predict(X_test)
y_pred = np.argmax(y_pred_proba, axis=1)

predicted_activities = label_encoder.inverse_transform(y_pred)
actual_activities = label_encoder.inverse_transform(y_test)

test_results = pd.DataFrame({
    'DayOfWeek': X_test[:, 0],
    'Hour': X_test[:, 1],  # Hour
    'Is_Holiday': X_test[:, 2],
    'Actual_Activity': actual_activities,
    'Predicted_Activity': predicted_activities
})

print(test_results)
