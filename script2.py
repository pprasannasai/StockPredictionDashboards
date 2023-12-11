import tensorflow as tf
import pandas as pd
import requests

#from stockanalysisandprediction.management.commands.train_prediction_model.py import getStockData, getTargetData, standardizeData, createDataPartitions, getPredictions
from script3 import getStockData, getTargetData, standardizeData, createDataPartitions, getPredictions

def makePrediction(stock_ticker):
    url = "https://stockanalysisandprediction-59df5bff809d.herokuapp.com"
    api_url = f"{url}/api/getPrediction/{stock_ticker}"
    response = requests.get(api_url)
    data = response.json()

    # Assuming 'train' and 'test' data are dictionaries with dates as keys
    train = data.get("train", {})
    close_train_data = train.get("close", {})

    # Convert to Pandas DataFrame
    train_data = pd.DataFrame(list(close_train_data.items()), columns=['date', 'close'])
    #test_data = pd.DataFrame(list(test.items()), columns=['date', 'predicted'])
    
    test = data.get("test", {})

    # Separate 'close' and 'predicted' data
    close_data = test.get("close", {})
    predicted_data = test.get("predicted", {})

    # Convert to DataFrame
    close_df = pd.DataFrame(list(close_data.items()), columns=['date', 'close'])
    predicted_df = pd.DataFrame(list(predicted_data.items()), columns=['date', 'predicted'])

    # Merge the DataFrames on the 'date' column
    test_data = pd.merge(close_df, predicted_df, on='date')


    return train_data, test_data