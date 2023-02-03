#Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras. callbacks import EarlyStopping, ModelCheckpoint

#Data_set
Col_names = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Nov"]
Row_Names = ["Corporate Proposals won - Microwave", "Corporate Proposals won - FTTB", "Wholesale proposals won", "Data Centre proposals won", "SMB & Residential FTTx Proposals won - FTTx + Dedicated", "SMB Proposals won (Orders received) - SME ODU"]
Data_set = "/content/Actualized data.csv"
df = pd.read_csv(Data_set, Month = Col_names, Service = Row_Names)

#Check Data_set content
df.head()