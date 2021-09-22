#!/usr/bin/env python3
'''Bitcoin Forecasting module'''
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt
preprocess_data = __import__('preprocess_data').preprocess_data
WindowGenerator = __import__('window_generator').WindowGenerator


seed = 0
tf.random.set_seed(seed)
np.random.seed(seed)


def rescale_data(df, m_std):
    '''Rescales or normalizes the dataframe with respect to the training mean
       and standard deviation
    Args:
        df is the pandas dataframe to be rescaled
        m_std is a tupple containing the training mean and standard deviation

    Returns: the rescaled data frame
    '''
    return (df - m_std[0]) / m_std[1]


def direscale_data(df, m_std):
    '''Reverses the reescaling or normalization of the dataframe
    Args:
        df is the pandas dataframe to be direscaled
        m_std is a tupple containing the training mean and standard deviation

    Returns: the direscaled data frame
    '''
    return (df * m_std[1]) + m_std[0]


MAX_EPOCHS = 50


def compile_and_fit(model, window, patience=5):
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                      patience=patience,
                                                      mode='min')

    model.compile(loss=tf.losses.MeanSquaredError(),
                  optimizer=tf.optimizers.Adam(),
                  metrics=[tf.metrics.MeanAbsoluteError()])

    history = model.fit(window.train, epochs=MAX_EPOCHS,
                        validation_data=window.test,
                        callbacks=[early_stopping])
    return history


preprocess_data()

# To read the csv files generated during the Preprocessing
train_df = pd.read_csv("./train_df.csv", index_col=0)
test_df = pd.read_csv("./test_df.csv", index_col=0)
train_df_datetime = pd.read_csv("./train_df_datetime.csv", index_col=0)
test_df_datetime = pd.read_csv("./test_df_datetime.csv", index_col=0)
train_df_datetime['Datetime'] = pd.to_datetime(train_df_datetime['Datetime'])
test_df_datetime['Datetime'] = pd.to_datetime(test_df_datetime['Datetime'])
train_df_datetime.set_index('Datetime', inplace=True)
test_df_datetime.set_index('Datetime', inplace=True)

# Data re-scalling:
m_std = (train_df.mean(), train_df.std())
train_df = rescale_data(train_df, m_std)
test_df = rescale_data(test_df, m_std)

# Model Design (Recurrent Neural Network)
lstm_model = tf.keras.models.Sequential([
    # Shape [batch, time, features] => [batch, time, lstm_units]
    tf.keras.layers.LSTM(32, return_sequences=True),
    tf.keras.layers.LSTM(64, return_sequences=True),
    # Shape => [batch, time, features]
    tf.keras.layers.Dense(units=1),
    # tf.keras.layers.Reshape([1, -1])
])

# Instantiating the WindowGenerator:
wide_window = WindowGenerator(
    input_width=24, label_width=24, shift=1,
    train_df=train_df, test_df=test_df,
    label_columns=['Close'])

# Training the model:
if (not os.path.exists('./bitcoin_prediction.h5')):
    history = compile_and_fit(lstm_model, wide_window)
    lstm_model.save('./bitcoin_prediction.h5')
else:
    lstm_model = tf.keras.models.load_model('./bitcoin_prediction.h5')

# Plotting the training retults:
wide_window.plot(lstm_model)

# Predicting:
predictions = lstm_model.predict(
    tf.keras.preprocessing.timeseries_dataset_from_array(
        data=test_df,
        targets=None,
        sequence_length=wide_window.input_width,
        sequence_stride=1,
        shuffle=False,
        batch_size=1,)
)

outputs = predictions[:, -1:, :]
new_shape = (outputs.shape[0], outputs.shape[1])

df_preds2_test = pd.DataFrame(
    data=outputs.reshape(new_shape),
    columns=['Close'],
)

df_preds_test = pd.DataFrame(np.nan, index=range(24), columns=['Close'])
df_preds_test = df_preds_test.append(df_preds2_test)
idx_start = test_df.index[0]
idx_end = test_df.index[-1]
df_preds_test['idxs'] = range(idx_start, idx_end + 2)
df_preds_test.set_index(keys='idxs', drop=True, inplace=True)

# Plotting Predictions:

# Return the data to is original scale
test_df = direscale_data(test_df, m_std)
df_preds_test = direscale_data(df_preds_test, m_std)

# Plot a sample section of the data set
plt.figure(figsize=(15, 7))
days = 7
hours = days * 24
plt.plot(
    test_df_datetime.index[-hours:],
    test_df[-hours:],
    label='Inputs',
    marker='.'
)
plt.plot(
    test_df_datetime.index[-hours:],
    df_preds_test[-hours - 1:-1],
    label='Predictions',
    marker='.')
plt.title('Bitcoin Price Predictions')
plt.xlabel('Time')
plt.ylabel('Price $USD')
plt.legend()
plt.plot()
