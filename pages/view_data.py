import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Credit Risk Analysis', page_icon=':moneybag:', layout='wide')

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("client_data.csv")

df = load_data()

# Streamlit app
st.title('Credit Risk Analysis Dataset')

st.write('This dataset contains information about clients and their credit risk. The goal is to predict if a client will default on their loan.')
st.sidebar.info('The dataset contains the following columns:')

st.sidebar.dataframe(df.columns, use_container_width=True)


st.dataframe(df, use_container_width=True, 
             column_config={
                    'max_width': '200',
                    'min_width': '50',
             })

numdf = df.select_dtypes(include=['int64', 'float64']).describe().style.highlight_max().highlight_min(color='lightgreen')
# numerical analysis
st.header('Numerical Analysis')
st.dataframe(
    numdf,
    use_container_width=True,
)
