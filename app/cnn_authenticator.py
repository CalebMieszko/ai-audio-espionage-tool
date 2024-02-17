from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D, Dropout
from keras.optimizers import Adam


def build_model(input_shape):
    model = Sequential()

    # Convolutional layer
    model.add(Conv1D(64, kernel_size=5, activation='relu',
              input_shape=(input_shape, 1)))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Dropout(0.2))

    # Another convolutional layer
    model.add(Conv1D(128, kernel_size=5, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))

    # Output layer
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer=Adam(
        learning_rate=0.001), metrics=['accuracy'])

    return model
