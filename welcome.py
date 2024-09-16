import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

css_file = open("style.css")

st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)


# 3 cards for the welcome page

# about card
st.markdown(
    """
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">About</h5>
            <p class="card-text">This is a simple dashboard to explore the data of the credit risk analysis dataset.</p>
        </div>
        <div class="card-footer">
            <a href="/about" class="btn btn-primary">View About</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# view data
st.markdown(
    """
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">View Data</h5>
            <p class="card-text">View the data of the credit risk analysis dataset.</p>
        </div>
        <div class="card-footer">
            <a href="/view" class="btn btn-primary">View Data</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# view analysis
st.markdown(
    """
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">View Analysis</h5>
            <p class="card-text">View the analysis of the credit risk analysis dataset.</p>
        </div>
        <div class="card-footer">
            <a href="/analysis" class="btn btn-primary">View Analysis</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

