import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache

def load_data():
    df = pd.read_csv("all_stocks_5yr.csv",index_col="date")

    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols= text_df.columns

    stock_cols =df['Name']
    unique_stocks = stock_cols.unique()
    return df, numeric_cols, text_cols, unique_stocks


df, numeric_cols, text_cols, unique_stocks = load_data()


st.title("Stock Dashboard")

check_box = st.sidebar.checkbox(label=" Donot display dataset")

if not check_box:
    st.write(df)    

st.sidebar.title("Settings")
st.sidebar.subheader("Timeseries Setting")
feature_selection = st.sidebar.multiselect(label = "Features to Plot", options =numeric_cols )

stock_dropdown = st.sidebar.selectbox(label="Stock ticker", options = unique_stocks)


if feature_selection:
    print(feature_selection)
    df = df[df['Name'] == stock_dropdown]
    df_features =df[feature_selection]

    plotly_figure = px.line(data_frame=df_features, x=df_features.index, y=feature_selection, title=(str(stock_dropdown) + ' ' +'Timeline'))


    st.plotly_chart(plotly_figure)
