import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelBinarizer


def main():
    iris = load_iris()
    print(iris['target'])
    print(LabelBinarizer().fit_transform(iris['target']))
    train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.2,
                                                                        random_state=1)
    labels_train = LabelBinarizer().fit_transform(train_target)
    labels_test = LabelBinarizer().fit_transform(test_target)

    model = Sequential([Dense(5, input_dim=4), Activation('relu'), Dense(3), Activation('sigmoid')])

    model1 = Sequential()
    model1.add(Dense(5, input_dim=4))

    sgd = SGD(lr=.01, decay=1e-6, momentum=.9, nesterov=True)
    model.compile(optimizer=sgd, loss='categorical_crossentropy')
    model.fit(train_data, labels_train, epochs=200, batch_size=40)
    print(model.predict_classes(test_data))

    # model.save_weights('./data/w')
    # model.load_weights('./data/w')


if __name__ == '__main__':
    main()
