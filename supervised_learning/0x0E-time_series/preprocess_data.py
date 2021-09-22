#!/usr/bin/env python3
'''preprocess data module'''
import os
import datetime
import pandas as pd
import tensorflow as tf


def preprocess_data():
    '''Preprocess the Coinbase dataset to do a Bitcoin forecasting'''

    zip_path = tf.keras.utils.get_file(
        origin=('https://github.com/gcifuentess/' +
                'holbertonschool-machine_learning/raw/main/' +
                'supervised_learning/0x0E-time_series/data/' +
                'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip'),
        fname='coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip',
        extract=True)
    csv_path, _ = os.path.splitext(zip_path)

    df = pd.read_csv(csv_path)

    # Timestamp to Datetime:
    df['Timestamp'] = pd.to_datetime(df["Timestamp"], unit='s')
    df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)

    # Selecting features:
    df = df[['Datetime', 'Close']]
    df.set_index('Datetime', inplace=True)

    # We are using Forward fill to handle missing values:
    df['Close'].fillna(method='ffill', inplace=True)

    # Changing Periodicity (minutes to hours)
    df['Datetime'] = df.index
    df = df.groupby([(df.index.year),
                     (df.index.month),
                     (df.index.day),
                     (df.index.hour)]).last()
    df.set_index('Datetime', inplace=True)
    df = df[:-1]  # last value with wrong periodicity

    # Extract Relevant Section of Data (2017 - 2019)
    trunc = df.index.to_series().between("2017", "2021")
    df = df[trunc]

    # Split Data (Train and Test sets):
    SPLIT = 0.70
    n = len(df)
    train_df = df[0:int(n * SPLIT)]
    test_df = df[int(n * SPLIT):]
    train_df.reset_index(inplace=True)
    test_df.reset_index(inplace=True)
    train_df_datetime = train_df.pop('Datetime')
    test_df_datetime = test_df.pop('Datetime')

    # Saving data:
    train_df.to_csv("./train_df.csv")
    test_df.to_csv("./test_df.csv")
    train_df_datetime.to_csv("./train_df_datetime.csv")
    test_df_datetime.to_csv("./test_df_datetime.csv")
