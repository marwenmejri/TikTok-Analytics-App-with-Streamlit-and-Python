import streamlit as st
import pandas as pd
from tiktok import get_data
from subprocess import call
import plotly.express as px


# Set page width to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown(
    "This dashboard allows you to analyse trending 📈 tiktoks using Python and Streamlit.")
st.sidebar.markdown(
    "To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>", unsafe_allow_html=True)

# Input
HASHTAG = st.text_input('Search for a hashtag here', value='')

# Button
if st.button("Get Data"):
    # st.write(HASHTAG)
    call(['python', 'tiktok.py', HASHTAG])

    # Load in the data saved
    df = pd.read_csv("tiktokdata.csv")

    # Plotly visualization Here
    fig = px.histogram(df, x='desc', hover_data=[
                       'desc'], y='stats_diggCount', height=300)
    st.plotly_chart(fig, use_container_width=True)

    # Split columns
    left_col, right_col = st.columns(2)

    # First Chart - video stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=[
                          'desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second Chart
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=[
                          'author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)

    # Show tabular dataframe in streamlit
    df
