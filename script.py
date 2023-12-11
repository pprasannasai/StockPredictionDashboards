import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
from pyspark.sql import SparkSession
import sys
import os
sys.path.append(os.path.abspath('/Users/pprasannasai/bigdataproject/'))

url="https://stockanalysisandprediction-59df5bff809d.herokuapp.com"
def getRawAnalyticData(stock_ticker, raw_analytic, time = 'all_time'):
  api_url = f"{url}/api/getRawAnalyticData/{stock_ticker}/{raw_analytic}/?time={time}"
  parameters = {'stock_ticker': stock_ticker, 'time': time}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])

# API to calculate Daily Returns in a given time period.

def getDailyReturns(stock_ticker, time = 'all_time'):
  api_url = f"{url}/api/getDailyReturns/{stock_ticker}/?time={time}"
  parameters = {'stock_ticker': stock_ticker, 'time': time}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])
  
# API to get Daily Price Change in a given time period.

def getDailyPriceChange(stock_ticker, time = 'all_time'):

  api_url = f"{url}/api/getDailyPriceChange/{stock_ticker}/?time={time}"
  parameters = {'stock_ticker': stock_ticker, 'time': time}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])
  
# API to get Daily Price Range in a given time period.

def getDailyPriceRange(stock_ticker, time = 'all_time'):
  api_url = f"{url}/api/getDailyPriceRange/{stock_ticker}/?time={time}"
  parameters = {'stock_ticker': stock_ticker, 'time': time}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])
  
# API to get Daily Price Gap in a given time period.

def getDailyPriceGap(stock_ticker, time = 'all_time'):
  api_url = f"{url}/api/getDailyPriceGap/{stock_ticker}/?time={time}"
  parameters = {'stock_ticker': stock_ticker, 'time': time}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])
  

def getYearlyPerformance(stock_ticker='AAPL'):

  api_url = f"{url}/api/getYearlyPerformance/{stock_ticker}"
  parameters = {'stock_ticker': stock_ticker}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])
    
def getMovingAverages(stock_ticker, analytic, ma_window = "3_day", 
                      time = 'all_time'):
   
  api_url = f"{url}/api/getMovingAverages/{stock_ticker}/{analytic}/?time={time}&ma_window={ma_window}"
  parameters = {'stock_ticker': stock_ticker}
  response = requests.get(api_url)
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # If your interested data is in the 'result_df' key
    result_data = data['result_df']
    
    # Convert to Pandas Series
    result_series = pd.Series(result_data)

    # Resetting the index to create a DataFrame with 'date' and 'value' columns
    result_df = result_series.reset_index()
    result_df.columns = ['date', 'value']
  
  return result_df, float(data['max_result']), data['max_date'], float(data['min_result']), data['min_date'], float(data['avg_result'])

  
def getRankings(analytic, top_n = 'top_10', time = 'all_time', 
                 ma_analytic = 'NA', ma_window = 'NA'):

	api_url = f"{url}/api/getRankings/{analytic}"
	response = requests.get(api_url)
	data = response.json()
	return data[: int(top_n[4:])]
  
def getLongestContinuousTrends(stock_ticker, analytic, time='all_time', ma_window='NA', ma_analytic='NA'):
    api_url = f"{url}/api/getLongestContinuousTrends/{stock_ticker}/{analytic}/?time={time}"

    response = requests.get(api_url)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        print(data)
        uptrend = pd.Series(data[0], index=['duration', 'start_date', 'end_date'])
        downtrend = pd.Series(data[1], index=['duration', 'start_date', 'end_date'])
    return uptrend, downtrend
    

    
def getStockData(data, stock_ticker):
  # api_url = f"{url}/stock/{stock_ticker}"
#   response = requests.get(api_url)
  
  stock_data = data[data['Name'] == stock_ticker]
  return stock_data
  
def getData():
  
  spark = SparkSession.builder.appName("CSV Operations").getOrCreate()
  stocks = spark.read.csv("all_stocks_5yr.csv", header=True, inferSchema=True)
  data = stocks.toPandas()
  return data
  
def getAnalyticData(analytic, stock_ticker, time = 'all_time',  
                    ma_analytic = 'NA', ma_window = 'NA'):

  if analytic == 'yearly_performance':
    res = getYearlyPerformance(stock_ticker)
  
  elif analytic == 'daily_price_gap':
    res = getDailyPriceGap(stock_ticker, time)
  
  elif analytic == 'daily_price_range':
    res = getDailyPriceRange(stock_ticker, time)
  
  elif analytic == 'daily_price_change':
    res = getDailyPriceChange(stock_ticker, time)
  
  elif analytic == 'daily_returns':
    res = getDailyReturns(stock_ticker, time)
  
  elif analytic == 'moving_averages':
    res = getMovingAverages(stock_ticker, ma_analytic, ma_window, time)
  
  return res
  
def getDuration(start_date, end_date):
    
    if not isinstance(start_date, str) and not isinstance(end_date, str):
      return (end_date - start_date)

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    time_difference = end_date - start_date
    duration = time_difference.days
    
    return duration

def getCorrelationAnalytics(target_stock_ticker='AAPL', analytic='daily_returns', time='all_time', ma_analytic='NA', ma_window='NA'):
    api_url = f"{url}/api/getCorrelationAnalytics/{target_stock_ticker}/{analytic}/?time={time}"

    response = requests.get(api_url, timeout=1000)
    data = response.json()
    sorted_dict = sorted(data.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_dict)
    return sorted_dict
# def getCorrelationAnalytics(target_stock_ticker = 'AAL', analytic = 'daily_returns', time = 'all_time', ma_analytic = 'NA', ma_window = 'NA'):
# 	corr={'UAL': 0.45795314330415476,
#  'DAL': 0.45493913427953275,
#  'LUV': 0.40929661454325517,
#  'ALK': 0.342700746304422,
#  'TROW': 0.2189623404226664,
#  'APH': 0.21687376186195245,
#  'AMP': 0.212048054904255,
#  'WYN': 0.2096935591550657,
#  'BK': 0.2095526007706321,
#  'XRAY': 0.20629947668323784,
#  'MAR': 0.20592244252076589,
#  'BAC': 0.20488787459519373,
#  'RHI': 0.2047495642123695,
#  'BWA': 0.20353411769573393,
#  'MTB': 0.2027996721422895,
#  'PRU': 0.20156760653044764,
#  'LEG': 0.2013450764138541,
#  'ADI': 0.2005799283340337,
#  'IR': 0.20038398126833876,
#  'NTRS': 0.20016700023415407,
#  'FFIV': 0.19996543903469274,
#  'CTSH': 0.19973808761671433,
#  'BRK.B': 0.1988002820874263,
#  'ADS': 0.19840531018124152,
#  'CMI': 0.19820978232012748,
#  'MCO': 0.19809510593879948,
#  'A': 0.1979921948993694,
#  'TEL': 0.19766384226969086,
#  'BLK': 0.19762995618698032,
#  'ROP': 0.19727323362373184,
#  'MHK': 0.19675983802265212,
#  'UNM': 0.19662783392665503,
#  'BEN': 0.19626102312363652,
#  'FISV': 0.19618985558691268,
#  'GT': 0.19592782434779935,
#  'STI': 0.1958890096523059,
#  'AOS': 0.19471415414243765,
#  'MS': 0.1944080859961975,
#  'SCHW': 0.19414921762995463,
#  'PFG': 0.19410799469302017,
#  'EXPE': 0.1931568953881234,
#  'GS': 0.19309656582433563,
#  'LRCX': 0.1930117272833957,
#  'C': 0.19265100284810635,
#  'SNA': 0.1925412902901505,
#  'IVZ': 0.19244724073378566,
#  'URI': 0.1921866716174782,
#  'MAS': 0.19187424724845875,
#  'KMX': 0.1916082777835184,
#  'CTAS': 0.19128319297215893,
#  'PAYX': 0.19115466953069743,
#  'TMK': 0.19104289507375585,
#  'WHR': 0.19032148522756745,
#  'ZION': 0.1903208253500314,
#  'HON': 0.1901647687468992,
#  'HBAN': 0.19011083407785495,
#  'INTU': 0.1896490027875133,
#  'AXP': 0.18957996908302738,
#  'MA': 0.18937485929940354,
#  'TMO': 0.18892491200598177,
#  'UPS': 0.1887416886717519,
#  'DFS': 0.1887321223920984,
#  'MCHP': 0.18855120391780514,
#  'HST': 0.18848475738784237,
#  'SIG': 0.1880722832509632,
#  'COF': 0.18791565714036004,
#  'BA': 0.18787356856886755,
#  'RJF': 0.18771358374553124,
#  'COL': 0.18725192605937102,
#  'LNC': 0.18667911641512192,
#  'ADSK': 0.1865339817577032,
#  'V': 0.186020448718085,
#  'FDX': 0.18578117882210843,
#  'TXN': 0.18558126126745506,
#  'PPG': 0.18506068912561058,
#  'AME': 0.18501740858635574,
#  'LUK': 0.1850023489486637,
#  'KEY': 0.18485383260980678,
#  'JPM': 0.18469693707669646,
#  'NKE': 0.18462148101536296,
#  'GM': 0.18441197080139973,
#  'EA': 0.18438582319372868,
#  'PNC': 0.18437747409480612,
#  'SEE': 0.18433541349879534,
#  'CMA': 0.18431661946099218,
#  'L': 0.18415466838649683,
#  'NSC': 0.18392720198228293,
#  'UNP': 0.18355607637188787,
#  'HRS': 0.18350216191817276,
#  'UTX': 0.1834619493309002,
#  'ETFC': 0.1832994309047339,
#  'LEN': 0.18301057514435745,
#  'ANSS': 0.18298991510851995,
#  'NCLH': 0.18245291015494122,
#  'AVY': 0.18228211400257482,
#  'AMG': 0.18208021518290865,
#  'CB': 0.18195427330767255,
#  'TRIP': 0.18187877922726284,
#  'PCLN': 0.18187312636652658,
#  'F': 0.18175859856381288,
#  'HIG': 0.18147980134819236,
#  'JWN': 0.18134777128267554,
#  'GLW': 0.18117303223296868,
#  'APD': 0.18117265089509907,
#  'JBHT': 0.1809927408536904,
#  'TXT': 0.18092410544324258,
#  'SPGI': 0.180887225316318,
#  'RCL': 0.1807668363698296,
#  'STT': 0.1807251178188081,
#  'GD': 0.1806779825127158,
#  'CCL': 0.18058813766684176,
#  'UAA': 0.18020434829362644,
#  'CERN': 0.1802010502208336,
#  'FLR': 0.1801235557596674,
#  'FBHS': 0.18006092561084808,
#  'FLS': 0.18001916208915597,
#  'SWK': 0.17993305582225283,
#  'TDG': 0.17968160065626648,
#  'AMAT': 0.17927619138027243,
#  'PKI': 0.1792051871042557,
#  'HOG': 0.17903249146016664,
#  'MGM': 0.17889190387921086,
#  'MET': 0.17878721981350243,
#  'IPG': 0.17864150519213468,
#  'FITB': 0.17855377760339483,
#  'SNPS': 0.17831567892068914,
#  'DHI': 0.17829799683407405,
#  'MDT': 0.1781550262190675,
#  'AVGO': 0.17812193494106127,
#  'PCAR': 0.17804732226454537,
#  'ITW': 0.17781718942358,
#  'LOW': 0.17762216414343465,
#  'HSIC': 0.17752558712357583,
#  'PH': 0.1775209235449143,
#  'SHW': 0.17745012553706085,
#  'ETN': 0.17739489590817842,
#  'PX': 0.17737574426311245,
#  'USB': 0.1773713922820151,
#  'HOLX': 0.17731778131455728,
#  'GPN': 0.1772143279918984,
#  'CA': 0.1772115927253717,
#  'UHS': 0.17689576552797262,
#  'PGR': 0.17669747863010876,
#  'EMR': 0.1766821501298315,
#  'WFC': 0.1765121168803349,
#  'ADP': 0.17629222214480977,
#  'BBT': 0.1762234082338576,
#  'ADBE': 0.17616272821468754,
#  'AJG': 0.17612286012019096,
#  'CAH': 0.17598939032558314,
#  'MCK': 0.1759713722277604,
#  'HD': 0.1759395089406067,
#  'SBUX': 0.17589394227497235,
#  'DOV': 0.175758879662699,
#  'SWKS': 0.17574751138990605,
#  'CBG': 0.17565500300733977,
#  'NOC': 0.17552671106632423,
#  'PKG': 0.1755015182744296,
#  'ARNC': 0.17535229571502167,
#  'AKAM': 0.17529072792384848,
#  'MMC': 0.17496140850962275,
#  'WU': 0.17472368517301431,
#  'ILMN': 0.17463027907528805,
#  'KSU': 0.17438370035121847,
#  'JCI': 0.1743767831803457,
#  'FLIR': 0.1742080404410262,
#  'PSX': 0.17419841082645662,
#  'MTD': 0.17418016293238328,
#  'JEC': 0.174144196722612,
#  'HII': 0.1740424260203466,
#  'KLAC': 0.17398977616651512,
#  'XLNX': 0.17398918647553097,
#  'PWR': 0.1739863553951816,
#  'OMC': 0.17392481102000526,
#  'AIG': 0.17388015037556784,
#  'IP': 0.17377884749663547,
#  'TIF': 0.17370519786517663,
#  'FL': 0.1735156155741963,
#  'TSCO': 0.17348928570986732,
#  'DHR': 0.1734617904543988,
#  'IBM': 0.1727501409047381,
#  'ROK': 0.17269308903343084,
#  'XYL': 0.1724903764774953,
#  'RF': 0.1723487621921315,
#  'LLL': 0.172314198069561,
#  'ALLE': 0.17208465026412123,
#  'IT': 0.17203241314027448,
#  'ESRX': 0.1719598117131271,
#  'MMM': 0.1718219226550108,
#  'LMT': 0.17179183356251432,
#  'NDAQ': 0.17124876608723189,
#  'CINF': 0.17092503670828552,
#  'AMGN': 0.1709094325692479,
#  'DVA': 0.17063096397529812,
#  'GOOGL': 0.1703402837982574,
#  'PBCT': 0.17021520127966747,
#  'INTC': 0.17019703993679938,
#  'MYL': 0.17013181865137064,
#  'EQIX': 0.1699911158738898,
#  'CTXS': 0.16997423595058217,
#  'AIZ': 0.16989782470564488,
#  'VMC': 0.1698922920958668,
#  'ALL': 0.16985186547694905,
#  'EFX': 0.16978505169870517,
#  'PNR': 0.16968070836123872,
#  'LYB': 0.16943444663205318,
#  'WDC': 0.1693337973840604,
#  'VFC': 0.16922800378067446,
#  'PHM': 0.16911090486440086,
#  'CBS': 0.16886766760552993,
#  'MON': 0.16873768983553844,
#  'TSS': 0.1687137655503708,
#  'ALXN': 0.16868411505073752,
#  'CVS': 0.16853413721247754,
#  'CAT': 0.16845330086793803,
#  'MLM': 0.1684108704472782,
#  'DISH': 0.16838447369967974,
#  'DGX': 0.1683724539649706,
#  'GRMN': 0.16830822805068663,
#  'FIS': 0.16826592899714546,
#  'VNO': 0.16796752809296145,
#  'XL': 0.16794626480723063,
#  'MSI': 0.16781492487414024,
#  'LKQ': 0.1677448253710209,
#  'AMZN': 0.16769437036735582,
#  'GPC': 0.16760436717601807,
#  'CSX': 0.1675745008711156,
#  'CDNS': 0.16740254954354472,
#  'BIIB': 0.16706275989320912,
#  'NTAP': 0.16701422144608033,
#  'CMG': 0.16701266405511495,
#  'DLTR': 0.1668896024623081,
#  'WAT': 0.16684497348804161,
#  'ZBH': 0.16662772858053881,
#  'AYI': 0.16649043556674337,
#  'CRM': 0.16647884107553093,
#  'HBI': 0.16637450686988917,
#  'YUM': 0.16636215127944493,
#  'VRTX': 0.16634509133592051,
#  'LH': 0.16625725029528718,
#  'TRV': 0.16574356236932114,
#  'EXPD': 0.16547580233027379,
#  'MU': 0.16545145003521264,
#  'ACN': 0.1654211579808795,
#  'STX': 0.16539235503501462,
#  'QCOM': 0.16512566979653204,
#  'MCD': 0.16507629860324355,
#  'RHT': 0.1647228816850446,
#  'RTN': 0.16472065394978688,
#  'GE': 0.16465622723942766,
#  'CELG': 0.1646349461323862,
#  'TWX': 0.16449516050058735,
#  'ECL': 0.16444411859520147,
#  'IDXX': 0.1642564883434991,
#  'IFF': 0.1641442571810961,
#  'XRX': 0.16411807718482432,
#  'ICE': 0.16365135589205163,
#  'SLG': 0.16363445462268683,
#  'FB': 0.16356609561578744,
#  'AGN': 0.163554606398132,
#  'SYK': 0.16344722212023116,
#  'VRSK': 0.16343903437622767,
#  'AON': 0.1632828173928686,
#  'BAX': 0.163066184407654,
#  'PDCO': 0.16301602183111616,
#  'M': 0.16290671992652236,
#  'TJX': 0.16283370577376838,
#  'EBAY': 0.1628311123805492,
#  'ABT': 0.1626117096680554,
#  'VRSN': 0.16255023903007781,
#  'COO': 0.16253376471378475,
#  'EMN': 0.16226623537229123,
#  'ROST': 0.16182879026023297,
#  'BSX': 0.16172146952208,
#  'AFL': 0.16171736579941304,
#  'JNPR': 0.16136713319978335,
#  'LB': 0.161206386059345,
#  'SRCL': 0.16117180940154158,
#  'AAP': 0.16108662468693072,
#  'HRB': 0.1609956186815569,
#  'CTL': 0.1608237899314857,
#  'DRI': 0.16068968067427855,
#  'ADM': 0.16055181512006,
#  'HAL': 0.16044337611395446,
#  'RSG': 0.16015889577370884,
#  'GOOG': 0.1601571068755556,
#  'ZTS': 0.15993769041177772,
#  'HCA': 0.1599102662699374,
#  'DIS': 0.1597541100415199,
#  'CHRW': 0.15954659424381157,
#  'UNH': 0.15915551923325777,
#  'FMC': 0.158943911851069,
#  'RMD': 0.15890695381914233,
#  'INCY': 0.15877095831472465,
#  'ANTM': 0.15871375039874064,
#  'FAST': 0.15865018275441303,
#  'CMCSA': 0.15841203211978375,
#  'VIAB': 0.15815431779637268,
#  'KORS': 0.1581380862368071,
#  'SJM': 0.15802604265104128,
#  'BF.B': 0.15780164712663822,
#  'ORCL': 0.15757212487339722,
#  'STZ': 0.1575480729026075,
#  'CME': 0.15670757481912467,
#  'DRE': 0.15654124498038643,
#  'PFE': 0.15627940246992683,
#  'NFLX': 0.1562498590058935,
#  'ALGN': 0.15612910847773945,
#  'BBY': 0.15603583551494324,
#  'IQV': 0.15596603896485034,
#  'MAC': 0.15570907393175024,
#  'NVDA': 0.15552181038274251,
#  'VZ': 0.15540765714658694,
#  'VLO': 0.1553882098875325,
#  'MDLZ': 0.15528501451315008,
#  'NUE': 0.15509955024239055,
#  'INFO': 0.15493529060057462,
#  'ALB': 0.1548857500050275,
#  'GILD': 0.1546267575288767,
#  'AET': 0.15461745738641103,
#  'SNI': 0.15461431417383106,
#  'RL': 0.1545431931914351,
#  'ESS': 0.15453329623832712,
#  'KMB': 0.15445937761282738,
#  'WBA': 0.1542516199033185,
#  'GWW': 0.15421615174553938,
#  'GPS': 0.15404533153456829,
#  'MPC': 0.15404302681721213,
#  'CNC': 0.15400591329775234,
#  'ABC': 0.15388314586903687,
#  'EW': 0.15382822496097015,
#  'ATVI': 0.15376373720686987,
#  'NLSN': 0.1537092716741694,
#  'MSFT': 0.15369656212659097,
#  'BMY': 0.15355024342646342,
#  'KR': 0.15284582634616886,
#  'WMB': 0.15283498878231497,
#  'WM': 0.15276371211257375,
#  'EL': 0.15274090806117016,
#  'BLL': 0.15273111963586802,
#  'REG': 0.1526275380193608,
#  'AES': 0.15249390397129786,
#  'CHTR': 0.15247703888453612,
#  'CF': 0.1523413235101298,
#  'AAPL': 0.1523399711257059,
#  'ANDV': 0.1523286878173766,
#  'BXP': 0.15209965049189667,
#  'ULTA': 0.1518790937951116,
#  'CSCO': 0.15175057537733708,
#  'SBAC': 0.15159598657855644,
#  'CI': 0.1514814107770341,
#  'COTY': 0.15136914268240861,
#  'ABBV': 0.15134202211621603,
#  'VAR': 0.15124485566269807,
#  'MNST': 0.15124065932875755,
#  'UDR': 0.15102251380481174,
#  'TPR': 0.15095589209529714,
#  'WY': 0.15086084617553883,
#  'NWL': 0.15085458060866855,
#  'AZO': 0.15084984428905085,
#  'RE': 0.1506440642188263,
#  'NAVI': 0.15053210596026192,
#  'KMI': 0.15048910764108847,
#  'WYNN': 0.15035120746556407,
#  'MRK': 0.1503444003809257,
#  'IRM': 0.1501651917446048,
#  'VTR': 0.15015701434654724,
#  'MOS': 0.15004443172465556,
#  'DISCK': 0.1493886087239911,
#  'DISCA': 0.14938415601446045,
#  'DPS': 0.14872434244219754,
#  'NOV': 0.1486092853896131,
#  'NWSA': 0.14859662174345176,
#  'PVH': 0.1485172966729877,
#  'DE': 0.14826114245157848,
#  'CL': 0.14815368006203358,
#  'BDX': 0.14814702124431997,
#  'MO': 0.14806821558879418,
#  'AEE': 0.14745901948764667,
#  'ORLY': 0.14730008093201616,
#  'SYY': 0.14727952359891797,
#  'NWS': 0.14727063429914694,
#  'TAP': 0.14716767347453039,
#  'CPB': 0.146905104874238,
#  'FOXA': 0.1468409992924679,
#  'FOX': 0.14683138093668371,
#  'KIM': 0.14674142775723142,
#  'SPG': 0.1464821697811748,
#  'AMT': 0.1463928952712585,
#  'GGP': 0.14581369713719797,
#  'JNJ': 0.1458103126084959,
#  'SYF': 0.14552332960256,
#  'SLB': 0.14542708238963217,
#  'EQT': 0.14537964152403154,
#  'HES': 0.14512807870691677,
#  'CNP': 0.14503505480475098,
#  'CFG': 0.1449561906065123,
#  'AMD': 0.14434038293845558,
#  'PRGO': 0.1441722707230634,
#  'HRL': 0.1439417565087327,
#  'PSA': 0.1438073550322224,
#  'ISRG': 0.14372263893674297,
#  'DG': 0.14321809620960435,
#  'CVX': 0.14308713922007868,
#  'LLY': 0.14271384321632138,
#  'AIV': 0.1426028888791582,
#  'WMT': 0.14255283403705854,
#  'HAS': 0.14227256778053385,
#  'EXR': 0.14190610299763723,
#  'PLD': 0.14188498448390596,
#  'HSY': 0.14185657741431446,
#  'HP': 0.14161849265370807,
#  'REGN': 0.14149776002254755,
#  'OXY': 0.1409729239729048,
#  'GIS': 0.14097208579448656,
#  'XOM': 0.14090311484926085,
#  'TGT': 0.140417489037376,
#  'KSS': 0.1402665399760387,
#  'ARE': 0.14020488178673501,
#  'PXD': 0.14016643656453512,
#  'NBL': 0.14002026076579363,
#  'SYMC': 0.13992840769829043,
#  'COST': 0.1397448514139012,
#  'APC': 0.13971921346484498,
#  'CHD': 0.13968774552968707,
#  'HCN': 0.13930824865304664,
#  'DVN': 0.13926033102210475,
#  'FRT': 0.13913729940554767,
#  'AEP': 0.1374902692031157,
#  'NRG': 0.1372786210177069,
#  'FCX': 0.13704924544666616,
#  'QRVO': 0.1367425924830344,
#  'FTI': 0.13667191665816472,
#  'HPQ': 0.1365411701017724,
#  'COG': 0.13620143633904008,
#  'CXO': 0.13591621451915398,
#  'APA': 0.13569044276343978,
#  'PNW': 0.13553664210815053,
#  'TSN': 0.13545450908467402,
#  'PG': 0.13543792110549985,
#  'PEP': 0.1350972816096248,
#  'T': 0.13451833520989265,
#  'EOG': 0.13435322812257533,
#  'MRO': 0.1343152808665214,
#  'KO': 0.13430059990063217,
#  'NEE': 0.13430004299480663,
#  'PYPL': 0.13429316995751164,
#  'CMS': 0.13413973469244037,
#  'HUM': 0.13402140340283583,
#  'K': 0.13400697202133485,
#  'CBOE': 0.13395291449577473,
#  'CLX': 0.13366527264086234,
#  'COP': 0.13360077226864142,
#  'APTV': 0.13342434438694442,
#  'WRK': 0.13328402310163376,
#  'AVB': 0.13319074483104032,
#  'PM': 0.1330030395711038,
#  'XEC': 0.13288834683789127,
#  'MAA': 0.13278767152531823,
#  'PCG': 0.1324832386352385,
#  'NFX': 0.13226282204339232,
#  'CHK': 0.1316958317734378,
#  'MAT': 0.13161177937108084,
#  'CAG': 0.13132582322303313,
#  'PPL': 0.13130238994494198,
#  'CCI': 0.1310751810408601,
#  'RRC': 0.1310674322487001,
#  'MKC': 0.1305488024644806,
#  'FE': 0.1304704902671964,
#  'EIX': 0.1302363239882925,
#  'ETR': 0.129976728728682,
#  'SO': 0.1299361242112222,
#  'WEC': 0.12948567242063638,
#  'EXC': 0.12887596878862448,
#  'CSRA': 0.12882805622794624,
#  'O': 0.12878636570885288,
#  'FTV': 0.12840080110690053,
#  'ES': 0.12820018209447034,
#  'PEG': 0.12722058367970884,
#  'ED': 0.12721899667820483,
#  'HCP': 0.12702226388655896,
#  'KHC': 0.1270138091852301,
#  'UA': 0.12694305437949926,
#  'OKE': 0.12649766831012604,
#  'DLR': 0.1262421417349715,
#  'DUK': 0.12609926699461813,
#  'EQR': 0.1260924626787969,
#  'WLTW': 0.12604078553677994,
#  'DTE': 0.12569185884830944,
#  'SRE': 0.1239961225022802,
#  'SCG': 0.12390830540331546,
#  'HPE': 0.12349007530571184,
#  'AWK': 0.1234760737009432,
#  'D': 0.12261766608959,
#  'HLT': 0.12228525097378104,
#  'LNT': 0.12216295898221245,
#  'EVHC': 0.12121182773167197,
#  'NEM': 0.12105503606590647,
#  'NI': 0.12033786917871911,
#  'XEL': 0.11864252872741421,
#  'DWDP': 0.11706417736534647,
#  'BHGE': 0.11647594876595618,
#  'BHF': 0.11242107317271036,
#  'DXC': 0.11224239190216169}
# 	return corr
         