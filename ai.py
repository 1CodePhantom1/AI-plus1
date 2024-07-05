import numpy as np
import keras

input_data=np.array([1, 2, 3, 124, -8, 153])
output_data=np.array([2, 3, 4, 125, -7, 154])

model = keras.Sequential()
model.add(keras.Input(shape=(1)))
model.add(keras.layers.Dense(units=1, activation="linear"))
model.compile(loss="mse", optimizer="adam")
fit_results=model.fit(x=input_data, y=output_data, epochs=15000)

model.save("myModel.keras")
while True:
    print(model.predict([float(input())]))