import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from script2 import makePrediction
from script import getData
from pyspark.sql import SparkSession
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Prediction")

spark = SparkSession.builder.appName("CSV Operations").getOrCreate()
stocks = spark.read.csv("stocks.csv", header=True, inferSchema=True)
stocks_pd = stocks.toPandas()
name_map = stocks_pd.set_index('Company Name')['Name'].to_dict()
stockSelected=st.sidebar.selectbox("Stocks",name_map )
stock_analytic=name_map[stockSelected]

days=st.sidebar.text_input("Number of Days for Prediction(Max. 63)", value='0')



[train_data, test_data]=makePrediction(stock_analytic)

train_data.columns=['date', 'close']
test_data=test_data[:int(days)]

test_data.columns=['date', 'close', 'predicted']
fig = go.Figure()

# Add the first line (original line chart)
fig.add_trace(go.Scatter(x=train_data['date'], y=train_data['close'], mode='lines', name='Past Prices',marker=dict(color='blue', size=5)))
fig.add_trace(go.Scatter(x=test_data['date'], y=test_data['close'], mode='lines', name='Actual Prices',marker=dict(color='green', size=5)))
fig.add_trace(go.Scatter(x=test_data['date'], y=test_data['predicted'], mode='lines', name='Predicted Prices',marker=dict(color='red', size=5)))

# Customize layout (optional)
fig.update_layout(width=1200, height=600,title='', xaxis_title='Date', yaxis_title='Close Price(USD)')

# Show the plot in Streamlit
st.plotly_chart(fig)
