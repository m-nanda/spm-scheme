from matplotlib import units
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras

def running_time(start, end, arg='Total Running Time: '):
  '''
  Function to calculate running time
  '''
  total_time = end - start
  total_time_s = total_time
  unit = 'second'
  if 60 < total_time < 3600:
    total_time /= 60
    unit = 'minutes'
  if total_time >= 3600:
    total_time /=3600
    unit = 'hour'
  print(f'{arg} {total_time} {unit}')
  return total_time_s

def splitting_data(data=None, col=5, window=10, 
                   train_ub='2015-11-01',  #23:59:50
                   test_lb='2015-11-01',
                   print_shape=True): #00:00:00
    
    # Form data x & y
    x = data.iloc[:,0:col]
    y = data.iloc[:,col]
    # y = data.iloc[:,col:]
    
    # Train data
    x_tr = x.loc[:train_ub]
    y_tr = y.loc[:train_ub]
    
    # Test data
    x_ts = x.loc[train_ub:]
    y_ts = y.loc[train_ub:]
    
    # Build sequence data
    x_train, y_train, x_test, y_test = [], [], [], []
    for i in range(y_tr.shape[0] - (window-1)):        
      x_train.append(x_tr.iloc[i:i+window].values)
      y_train.append(y_tr.iloc[i+(window-1)])
    
    for i in range(y_ts.shape[0] - (window-1)):
      x_test.append(x_ts.iloc[i:i+window].values)
      y_test.append(y_ts.iloc[i])

    x_train = np.array(x_train)
    x_test = np.array(x_test)
    
    y_train, y_test = np.array(y_train).reshape(-1,1), np.array(y_test).reshape(-1,1)
    if print_shape:  
      print(f'Ukuran x_train:{x_train.shape},\nUkuran y_train:{y_train.shape}\n')
      print(f'Ukuran x_test:{x_test.shape},\nUkuran y_test:{y_test.shape}\n')
      print(x_train[0], end=' ')
      print(y_train[0], '\n-----------------------------')
      print(x_test[0], end=' ')
      print(y_test[0], '\n-----------------------------')

    return x_train, y_train, x_test, y_test

# 0
def model_d_lstm(input_shape, act_fn='sigmoid', p=0.1, unit=10):
    tf.random.set_seed(42)
    np.random.seed(42)

    model = tf.keras.models.Sequential(
            name = 'Deep-LSTM', layers=[
            tf.keras.layers.LSTM(units=unit, return_sequences=True, input_shape=input_shape),
            tf.keras.layers.Dropout(rate=p),
            # tf.keras.layers.LSTM(units=unit, return_sequences=True),
            tf.keras.layers.LSTM(units=unit, return_sequences=False),
            tf.keras.layers.Dropout(rate=p),
            tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.summary()

    # COMPILE
    model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(0.00001), metrics=['accuracy'])
    return model

# 1  
def model_rnn(input_shape, act_fn='sigmoid', p=0.1, unit=10):
  tf.random.set_seed(42)
  np.random.seed(42)
  
  model = tf.keras.models.Sequential(
    name='Vanilla-Model', layers=[
    tf.keras.layers.SimpleRNN(units=unit, return_sequences=True, input_shape=input_shape),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.SimpleRNN(units=unit),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.Dense(1, activation='sigmoid')
  ])
  model.summary()
  model.compile(loss='binary_crossentropy', 
                optimizer=tf.keras.optimizers.Adam(0.00001), 
                metrics=['accuracy'])
  return model

# 2
def model_gru(input_shape, act_fn='sigmoid', p=0.1, unit=10):
  tf.random.set_seed(42)
  np.random.seed(42)
  
  model = tf.keras.models.Sequential(
    name='GRU-Model', layers=[
    tf.keras.layers.GRU(units=unit, return_sequences=True, input_shape=input_shape),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.GRU(units=unit),
    tf.keras.layers.Dropout(rate=p),    
    tf.keras.layers.Dense(1, activation='sigmoid')
  ])
  model.summary()
  model.compile(loss='binary_crossentropy', 
                optimizer=tf.keras.optimizers.Adam(0.00001), 
                metrics=['accuracy'])
  return model

# 3
def model_bigru(input_shape, act_fn='sigmoid', p=0.1, unit=10):
  tf.random.set_seed(42)
  np.random.seed(42)
  
  model = tf.keras.models.Sequential(
    name='BiGRU-Model', layers=[
    tf.keras.layers.Bidirectional(tf.keras.layers.GRU(units=unit, input_shape=input_shape)),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.Bidirectional(tf.keras.layers.GRU(units=unit)),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.Dense(1, activation='sigmoid')
  ])
  # model.summary()
  model.compile(loss='binary_crossentropy', 
                optimizer=tf.keras.optimizers.Adam(0.00001), 
                metrics=['accuracy'])
  return model

# 3
def model_bilstm(input_shape, act_fn='sigmoid', p=0.1, unit=10):
  tf.random.set_seed(42)
  np.random.seed(42)
  
  model = tf.keras.models.Sequential(
    name='BiLSTM-Model', layers=[
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=unit, return_sequences=True, input_shape=input_shape)),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=unit)),
    tf.keras.layers.Dropout(rate=p),
    tf.keras.layers.Dense(1, activation='sigmoid')
  ])
  # model.summary()
  model.compile(loss='binary_crossentropy', 
                optimizer=tf.keras.optimizers.Adam(0.00001), 
                metrics=['accuracy'])
  return model