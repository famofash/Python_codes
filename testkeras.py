from sklearn import preprocessing, svm
import pandas as pd
import numpy as np
import pickle
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from sklearn.preprocessing import LabelBinarizer
import sklearn.datasets as skds
from pathlib import Path
import arff
from sklearn.preprocessing import MinMaxScaler
arrfile = 'C:/Users/Myrioi-User/PycharmProjects/deeplearning/dataset.arff'
fp = open(arrfile)
decoder = arff.ArffDecoder()
d = decoder.decode(fp, encode_nominal=False)

data_tags = ["category", "class"]
data_list = d['data']
scaler = MinMaxScaler(feature_range=(0, 1))

train_size = int(len(data_list) * .8)
train_posts = data_list[:train_size]
test_posts = data_list[train_size:]
X_train = []
Y_train = []

X_test = []
Y_test = []

for data in train_posts:
    X_train.append(data[:26])
    for ydata in data[26: 27]:
        Y_train.append(ydata)
for data in test_posts:
    X_test.append(data[:26])
    for ydata in data[26: 27]:
        Y_test.append(ydata)

num_labels = 3
vocab_size = 7500
batch_size = 500
tokenizer = Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(X_train)
x_train = tokenizer.texts_to_matrix(X_train, mode='tfidf')
x_test = tokenizer.texts_to_matrix(X_test, mode='tfidf')

encoder = LabelBinarizer()
encoder.fit(Y_train)
y_train = encoder.transform(Y_train)
y_test = encoder.transform(Y_test)

model = Sequential()
model.add(Dense(512, input_shape=(vocab_size,)))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=30,
                    verbose=1,
                    validation_split=0.1)

score = model.evaluate(x_test, y_test,
                       batch_size=batch_size, verbose=1)

print('Test accuracy:', score[1])

text_labels = encoder.classes_

for i in range(10):
    prediction = model.predict(np.array([x_test[i]]))
    print(prediction)
    predicted_label = text_labels[np.argmax(prediction[0])]

    print('Actual Class:' + Y_test[i])
    print("Predicted Class: " + predicted_label)