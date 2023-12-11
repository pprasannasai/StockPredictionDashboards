import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
from pyspark.sql import SparkSession
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.abspath('/Users/pprasannasai/bigdataproject/'))
from script import getRawAnalyticData
from script import getDailyReturns
from script import getDailyPriceChange
from script import getDailyPriceRange
from script import getDailyPriceGap
from script import getYearlyPerformance
from script import getMovingAverages
from script import getRankings
from script import getLongestContinuousTrends
from script import getCorrelationAnalytics
spark = SparkSession.builder.appName("CSV Operations").getOrCreate()
stocks = spark.read.csv("stocks.csv", header=True, inferSchema=True)
stocks_pd = stocks.toPandas()


st.set_page_config(layout="wide")
st.title('Analysis')

st.sidebar.header("Please Filter Here:")

# Display the first column 'Name' from the Pandas DataFrame
#st.write(stocks_pd['Name'])

name_map = stocks_pd.set_index('Company Name')['Name'].to_dict()
stockSelected=st.sidebar.selectbox("Stocks",name_map )

analyticSelected=st.sidebar.selectbox("Features",["open", "close", "high", "low", "volume"] )

time_values = {"All Time":"all_time","1 week": "1_week", "2 weeks":"2_weeks",
                  "1 month":"1_month", "1 quarter":"1_quarter", "6 months":"6_months",
                  "1 year":"1_year", "custom":""}

timeselected=st.sidebar.selectbox("Time frame", time_values )

#st.write(name_map[stockSelected])


raw_analytic=analyticSelected
stock_analytic=name_map[stockSelected]
time_value=time_values
if timeselected == "custom":
    custom_days = st.sidebar.text_input("Number of Days", value='0')
    time_value = "custom_" + custom_days
else:
    time_value = time_values[timeselected]
    
#st.write(time_value)

[result_df, max_result, max_date, min_result, min_date, avg_result]=getRawAnalyticData(stock_analytic, raw_analytic, time_value)

plot_df = result_df
plot_df.columns = ['date', raw_analytic]

########################
fig = go.Figure()
fig.add_trace(go.Scatter(x=plot_df['date'], y=plot_df[raw_analytic], mode='lines', name=raw_analytic+" Price (US Dollars)"))
fig.add_trace(go.Scatter(x=[max_date], y=[max_result], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
fig.add_trace(go.Scatter(x=[min_date], y=[min_result], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
fig.add_trace(go.Scatter(x=plot_df['date'], y=[avg_result] * len(plot_df['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))
fig.update_layout(width=1200, height=600, title='Stock feature', xaxis_title='Date', yaxis_title=raw_analytic+" Price (US Dollars)")
st.plotly_chart(fig)
#st.write("Average Value: "+str(avg_result))
#######################

analytics_option={"Daily Returns":"daily_returns", "Daily Price Change":"daily_price_change", "Daily Price Range":"daily_price_range", "Daily Price Gap":"daily_price_gap",
"Yealy Performance": "yearly_performance"}

selectedAnalytic=st.selectbox("Analytics:",analytics_option)

if	analytics_option[selectedAnalytic] == "daily_returns":
	[result_dfA, max_resultA, max_dateA, min_resultA, min_dateA, avg_resultA]=getDailyReturns(stock_analytic, time_value)
	plot_dfA=result_dfA
	plot_dfA.columns = ['date', selectedAnalytic]
	
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=plot_dfA[selectedAnalytic], mode='lines', name=selectedAnalytic+" (US Dollars)"))
	fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))

	fig.update_layout(width=1200, height=600, title='Stock Analytic', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	# st.write("Maximum Value: "+str(max_resultA)+", Date:"+str(max_dateA))
# 	st.write("Minimun Value: "+str(min_resultA)+", Date:"+str(min_dateA))
	#st.write("Average Value: "+str(avg_resultA))
elif analytics_option[selectedAnalytic] == "daily_price_change":
	[result_dfA, max_resultA, max_dateA, min_resultA, min_dateA, avg_resultA]=getDailyPriceChange(stock_analytic, time_value)
	plot_dfA = result_dfA
	plot_dfA.columns = ['date', selectedAnalytic]
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=plot_dfA[selectedAnalytic], mode='lines', name=selectedAnalytic+" (US Dollars)"))
	fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))

	fig.update_layout(width=1200, height=600, title='Stock Analytic', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	# st.write("Maximum Value: "+str(max_resultA)+", Date:"+str(max_dateA))
# 	st.write("Minimun Value: "+str(min_resultA)+", Date:"+str(min_dateA))
	#st.write("Average Value: "+str(avg_resultA))
elif analytics_option[selectedAnalytic] == "daily_price_range":
	[result_dfA, max_resultA, max_dateA, min_resultA, min_dateA, avg_resultA]=getDailyPriceRange(stock_analytic, time_value)
	plot_dfA = result_dfA
	plot_dfA.columns = ['date', selectedAnalytic]
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=plot_dfA[selectedAnalytic], mode='lines', name=selectedAnalytic+" (US Dollars)"))
	fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))
	fig.update_layout(width=1200, height=600, title='Stock Analytic', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	# st.write("Maximum Value: "+str(max_resultA)+", Date:"+str(max_dateA))
# 	st.write("Minimun Value: "+str(min_resultA)+", Date:"+str(min_dateA))
	#st.write("Average Value: "+str(avg_resultA))
elif analytics_option[selectedAnalytic] == "daily_price_gap":
	[result_dfA, max_resultA, max_dateA, min_resultA, min_dateA, avg_resultA]=getDailyPriceGap(stock_analytic, time_value)
	plot_dfA = result_dfA
	plot_dfA.columns = ['date', selectedAnalytic]
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=plot_dfA[selectedAnalytic], mode='lines', name=selectedAnalytic+" (US Dollars)"))
	fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))
	fig.update_layout(width=1200, height=600, title='Stock Analytic', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	# st.write("Maximum Value: "+str(max_resultA)+", Date:"+str(max_dateA))
# 	st.write("Minimun Value: "+str(min_resultA)+", Date:"+str(min_dateA))
	#st.write("Average Value: "+str(avg_resultA))
elif analytics_option[selectedAnalytic] == "yearly_performance":
	st.write("Not dependent on time input")
	[result_dfA, max_resultA, max_dateA, min_resultA, min_dateA, avg_resultA]=getYearlyPerformance(stock_analytic)
	plot_dfA = result_dfA
	plot_dfA.columns = ['date', selectedAnalytic]
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=plot_dfA[selectedAnalytic], mode='lines', name=selectedAnalytic+" (US Dollars)"))
	fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))
	fig.update_layout(width=1200, height=600, title='Stock Analytic', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	

analytics2={"Moving Averages": "moving_averages", "Rankings":"getRankings","Trends": "trends", "Correlation":"correlation"}

selectedAnalytics2=st.selectbox("Choose Analytics: ",analytics2)


if analytics2[selectedAnalytics2]=="moving_averages" :

	ma_window = {"3 day":"3_day", "5 day":"5_day", "10 day":"10_day",
                  "30 day":"30_day", "60 day":"60_day"}
	maWindowSelected=st.selectbox("Moving Average Window", ma_window)  
	[result_dfA, max_resultA, max_dateA, min_resultA, min_dateA, avg_resultA]=getMovingAverages(stock_analytic, analytics_option[selectedAnalytic], ma_window[maWindowSelected], time_value)
	plot_dfA = result_dfA
	plot_dfA.columns = ['date', selectedAnalytic]
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=plot_dfA[selectedAnalytic], mode='lines', name='Moving Averages'))
	fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))
	fig.update_layout(width=1200, height=600, title='Moving Averages', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	
elif analytics2[selectedAnalytics2] == "getRankings":
    top = {"Top 5": "top_5", "Top 10": "top_10", "Top 20": "top_20", "Top 50": "top_50", "Top 100": "top_100"}
    topn = st.selectbox("Top N stocks", list(top.keys()))
    ticker_map = stocks_pd.set_index('Name')['Company Name'].to_dict()

    result_dfA = getRankings(analytics_option[selectedAnalytic], top[topn], time_value, ma_analytic='NA', ma_window='NA')

    names = [ticker_map[item[0]] for item in result_dfA]

    st.markdown("""
    <style>
        .scrollable-container {
            overflow-y: auto;
            height: 0px;  # Adjust the height as needed
        }
    </style>
    """, unsafe_allow_html=True)

    st.write("Top N ranked Stocks:")

    st.markdown('<div class="scrollable-container">', unsafe_allow_html=True)
    for name in names:
        st.markdown(f"- {name}", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
elif analytics2[selectedAnalytics2]=="trends":
	[uptrend, downtrend]=getLongestContinuousTrends(stock_analytic, analytics_option[selectedAnalytic], time_value)
	fig = go.Figure()
	fig.add_trace(go.Scatter(
    	x=plot_dfA['date'],
    	y=plot_dfA[selectedAnalytic],
    	mode='lines', 
    	name=selectedAnalytic,
    	line=dict(color='blue')
	))		
	fig.add_trace(go.Scatter(
    x=plot_dfA[(plot_dfA['date'] >= uptrend['start_date']) & (plot_dfA['date'] <= uptrend['end_date'])]['date'],
    y=plot_dfA[(plot_dfA['date'] >= uptrend['start_date']) & (plot_dfA['date'] <=uptrend['end_date'])][selectedAnalytic],
    mode='lines+markers',
    name='Uptrend',
    line=dict(color='red')  # If you want a line, use 'line' instead of 'marker'
	))
	fig.add_trace(go.Scatter(
    x=plot_dfA[(plot_dfA['date'] >= downtrend['start_date']) & (plot_dfA['date'] <= downtrend['end_date'])]['date'],
    y=plot_dfA[(plot_dfA['date'] >= downtrend['start_date']) & (plot_dfA['date'] <=downtrend['end_date'])][selectedAnalytic],
    mode='lines+markers',
    name='Downtrend',
    line=dict(color='green')  # If you want a line, use 'line' instead of 'marker'
	))
	#fig.add_trace(go.Scatter(x=[max_dateA], y=[max_resultA], mode='markers', name='Maximum value', marker=dict(color='red', size=10)))
	#fig.add_trace(go.Scatter(x=[min_dateA], y=[min_resultA], mode='markers', name='Minimum value', marker=dict(color='green', size=10)))
	#fig.add_trace(go.Scatter(x=plot_dfA['date'], y=[avg_resultA] * len(plot_dfA['date']), mode='markers', name='Average value', marker=dict(color='lime', size=3)))
	fig.update_layout(width=1200, height=600, title='Trends', xaxis_title='Date', yaxis_title=selectedAnalytic+" (US Dollars)")
	st.plotly_chart(fig)
	st.write("Uptrend duration: "+str(uptrend[0])+", Start Date: "+str(uptrend[1])+", End Date: "+str(uptrend[2]))
	st.write("Downtrend duration: "+str(downtrend[0])+", Start Date: "+str(downtrend[1])+", End Date: "+str(downtrend[2]))
	
elif analytics2[selectedAnalytics2]=="correlation":

	corr=getCorrelationAnalytics(stock_analytic, analytics_option[selectedAnalytic], time_value,  ma_analytic = 'NA', ma_window = 'NA')
	#st.write(corr)
	top = {"Top 5":"top_5", "Top 10":"top_10", "Top 20":"top_20", "Top 50":"top_50", "Top 100":"top_100"}
	topn=st.selectbox("Top N stocks", top)
	ticker_map = stocks_pd.set_index('Name')['Company Name'].to_dict()
	count = int(top[topn][4:])
	for key, value in corr.items():
		if count > 0:
			st.write(f'{ticker_map[key]}: {value}')
			count -= 1
		else:
			break

	


	