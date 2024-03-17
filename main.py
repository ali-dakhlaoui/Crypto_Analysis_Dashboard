import yfinance as yf
import streamlit as st 
import numpy as np
import seaborn as sns
import altair as alt
import plotly.figure_factory as ff

import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd
from pandas_profiling import profile_report
from streamlit_pandas_profiling import st_profile_report
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

from PIL import Image 
from urllib.request import urlopen

import streamlit.components.v1 as components  #styling the app
import codecs  # data enoder/decoder (base64,..) 


st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)





# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple='XRP-USD'
Bitcoincash='BCH-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(Bitcoincash)

# Fetch history data from Yahoo Finance
BTCHis = BTC_Data.history(period="10d")
ETHHis = ETH_Data.history(period="10d")
XRPHis = XRP_Data.history(period="10d")
BCHHis = BCH_Data.history(period="10d")

print(type(BTCHis))

# Fetch crypto data for the dataframeBTC 
BTC= yf.download(Bitcoin,start='2023-04-12',end='2023-04-12')
ETH= yf.download(Ethereum,start='2023-04-12',end='2023-04-12')
XRP= yf.download(Ripple,start='2023-04-12',end='2023-04-12')
BCH= yf.download(Bitcoincash,start='2023-04-12',end='2023-04-12')

# Side bar
with st.sidebar:
    selected = option_menu(
        menu_title= "Main Menu",
        options= ["Home","BITCOIN","ETHEREUM","RIPPLE","BITCOINCASH"] ,
        icons = ["house"],
        menu_icon= 'cast', 
        default_index = 0,

    )
# menu = ['Home','BITCOIN','ETHEREUM','RIPPLE','BITCOINCASH']
# choice = st.sidebar.selectbox("Menu",menu)
# imageBIC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))

if selected == 'Home':
    st.title("Welcome to Crypto Dashboard")
    st.write("In this Dashboard you can find the real-time prices of 3 of the most known cryptocurrency: Bitcoin, Ethereum and Ripple")

    # col1, col2, col3 = st.columns(3)
    # col1.metric(label="BITCOIN",value=max(BTCHis),delta=max(BTCHis),delta_color="inverse")
    # col2.metric(label="ETHERUEM",value=max(ETHHis),delta=0,delta_color="inverse")
    # col3.metric(label="RIPPLE",value=max(XRPHis),delta=0,delta_color="inverse")

            # create three columns
    kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="BITCOIN ⏳",
        value=BTCHis['Open'].max(axis=0),
        delta=0
    )

    kpi2.metric(
        label="ETHEREUM 💍",
        value=ETHHis['Open'].max(axis=0),
        delta=0,
    )

    kpi3.metric(
        label="RIPPLE ＄",
        value=XRPHis['Open'].max(axis=0),
        delta=0,
     )





    left ,mid, right = st.columns(3)
    with left:
        
        imageBIC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
        st.image(imageBIC)
        st.subheader("BITCOIN ($)")
        # st.markdown("Bitcoin is a digital currency -- also called cryptocurrency -- that can be traded for goods or services with vendors that accept Bitcoin as payment. With Bitcoin, holders can buy, sell and exchange goods or services without a central authority or bank as an intermediary.")
        st.line_chart(BTCHis)
        st.write(BTCHis)

    with mid:
        
        imageETH= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
        st.image(imageETH)
        st.subheader("ETHEREUM ($)")
        st.line_chart(ETHHis)
        st.write(ETHHis)

    with right:
        
        imageBIC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
        st.image(imageBIC)
        st.subheader("RIPPLE ($) ")
        st.line_chart(XRPHis)
        st.write(XRPHis)

    # # plotly_chart
    #     # Group data together
    # hist_data = [BTCHis-2, ETHHis,XRPHis+2]

    # group_labels = [' BITCOIN', 'ETHEREUM', 'RIPPLE']

    #     # Create distplot with custom bin_size
    # fig = ff.create_distplot(
    #         hist_data, group_labels, bin_size=[.1, .25, .5])

    # # Plot!
    # st.plotly_chart(fig, use_container_width=True)


elif selected == 'BITCOIN':
    st.subheader("BITCOIN")
    # % BITCOIN %

    # Bitcoin Display
    st.write("BITCOIN ($)")
    imageBIC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
    st.image(imageBIC)
    print(BTC)

    # Display da  taframe
    st.write(BTCHis)


    # Display a Chart
    col1, col2 =st.columns(2)
    with col1:
        st.header("Line Chart")
        st.line_chart(BTCHis)

    with col2:
        st.header("Bar Chart")
        st.bar_chart(BTCHis)

    st.write('---')
    st.area_chart(BTCHis)

elif selected == 'ETHEREUM':
    st.subheader("ETHEREUM")
    # Ethereum Display
    st.write("ETHEREUM ($)")
    imageETH= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
    st.image(imageETH)
    print(ETH)

    # Display dataframe
    st.write(ETHHis)
    
    # Display a Chart

    col3, col4 =st.columns(2)
    with col3:
        st.header("Line Chart")
        st.line_chart(XRPHis)

    with col4:
        st.header("Bar Chart")
        st.bar_chart(ETHHis)
    st.write('---')
    st.area_chart(ETHHis)


    # chart_data = pd.DataFrame(
    # np.random.randn(200, 3),
    # columns=['a', 'b', 'c'])

    # st.vega_lite_chart(chart_data, {
    # 'mark': {'type': 'circle', 'tooltip': True},
    # 'encoding': {
    #     'x': {'field': 'a', 'type': 'quantitative'},
    #     'y': {'field': 'b', 'type': 'quantitative'},
    #     'size': {'field': 'c', 'type': 'quantitative'},
    #     'color': {'field': 'c', 'type': 'quantitative'},
    #     },
    # })




elif selected == 'RIPPLE':
    st.subheader("RIPPLE")

    # % RIPPLE %

    # RIPPLE Display
    st.write("RIPPLE ($)")
    imageBIC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
    st.image(imageBIC)
    print(BTC)

    # Display da  taframe
    st.write(XRPHis)



    # Display a Chart
    col5, col6 =st.columns(2)
    with col5:
        st.header("Line Chart")
        st.line_chart(BTCHis)

    with col6:
        st.header("Bar Chart")
        st.bar_chart(BTCHis)

    st.write('---')
    st.area_chart(ETHHis)



elif selected == 'Home':
    st.subheader("Home")
    html_code= "<p style>" 





# # % BITCOIN %
# def local_css(style):
#     with open(style) as f:
#         st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)






# # % BITCOIN %

# # Bitcoin Display
# st.write("BITCOIN ($)")
# imageBIC= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
# st.image(imageBIC)
# print(BTC)

# # Display dataframe
# st.table(BTCHis)


# # Display a Chart
# col1, col2 =st.columns(2)
# with col1:
#     st.header("Line Chart")
#     st.line_chart(BTCHis)

# with col2:
#     st.header("Bar Chart")
#     st.bar_chart(BTCHis)

# st.write('---')


# % ETHEREUM %

# # Ethereum Display
# st.write("ETHEREUM ($)")
# imageETH= Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
# st.image(imageETH)
# print(ETH)

# # Display dataframe
# st.table(ETHHis)
# st.line_chart(ETHHis)
# # Display a Chart

# col3, col4 =st.columns(2)
# with col3:
#     st.header("Line Chart")
#     st.line_chart(ETHHis)

# with col4:
#     st.header("Bar Chart")
#     st.bar_chart(ETHHis)



# chart_data = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c'])

# st.vega_lite_chart(chart_data, {
#     'mark': {'type': 'circle', 'tooltip': True},
#     'encoding': {
#         'x': {'field': 'a', 'type': 'quantitative'},
#         'y': {'field': 'b', 'type': 'quantitative'},
#         'size': {'field': 'c', 'type': 'quantitative'},
#         'color': {'field': 'c', 'type': 'quantitative'},
#     },
# })




# chart = {
#     "mark": "point",
#     "encoding": {
#         "x": {
#             "field": "Time",
#             "type": "quantitative",
#         },
#         "y": {
#             "field": "Values",
#             "type": "quantitative",
#         },
#         "color": {"field": "Origin", "type": "nominal"},
#         "shape": {"field": "Origin", "type": "nominal"},
#     },
# }

# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])
# with tab1:
#     # Use the Streamlit theme.
#     # This is the default. So you can also omit the theme argument.
#     st.vega_lite_chart(
#         BTCHis, chart, theme="streamlit", use_container_width=True
#     )



