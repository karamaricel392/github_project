import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.preprocessing.text import Tokenizer

data = """Hello, world! This is a test dataset. You can use it for training your model."""
tokens = Tokenizer()
tokenizer.fit_on_texts(data)
X = tokenizer.texts_to_sequences(data)
y = [word for word in data if word not in set([word.lower() for word in X])]
# X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(len(X),)))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
