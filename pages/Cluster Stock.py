import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
from pyspark.sql import SparkSession
import plotly.graph_objects as go
import sys
import os
from pyspark.sql import SparkSession
sys.path.append(os.path.abspath('/Users/pprasannasai/bigdataproject/'))

st.set_page_config(page_title="Stock Cluster", page_icon=":bar_chart:", layout="wide")
st.title("Make Clusters")

def makeCluster(time='1_week'):
    url = "https://stockanalysisandprediction-59df5bff809d.herokuapp.com"
    api_url = f"{url}/api/makeCluster/?time={time}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        centroids = data['centroids']
        clusters = data['cluster_df']
        clusters_pd = pd.DataFrame(clusters)  # Corrected indentation
        return clusters_pd, centroids
    else:
        print(f"Failed to get data: {response.status_code}")
        return pd.DataFrame(), []
	
	
time_values = {"All Time":"all_time","1 week": "1_week", "2 weeks":"2_weeks",
                  "1 month":"1_month", "1 quarter":"1_quarter", "6 months":"6_months",
                  "1 year":"1_year"}

timeselected=st.sidebar.selectbox("Time frame", time_values )

[clusters, centroids]=makeCluster(time_values[timeselected])

fig = go.Figure()

# Add the first line (original line chart)
for cluster_num in range(5):
	cluster_data = clusters[clusters['cluster'] == cluster_num]
	fig.add_trace(go.Scatter(x=cluster_data['Daily_Returns'], y=cluster_data['Risk'], mode='markers',text=cluster_data['name'], name=f'Cluster {cluster_num + 1}'))
	
fig.add_trace(go.Scatter(x=[item[0] for item in centroids], y=[item[1] for item in centroids], mode='markers', name='Centroids',marker=dict(color='black', size=10, symbol='x')))

# Customize layout (optional)
fig.update_layout(width=1200, height=600,title='', xaxis_title='Daily Returns', yaxis_title='Risk')

# Show the plot in Streamlit
st.plotly_chart(fig)





