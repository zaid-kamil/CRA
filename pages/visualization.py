import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Credit Risk Analysis', page_icon=':moneybag:', layout='centered')

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("client_data.csv")

df = load_data()

# Streamlit app
st.title('Credit Risk Analysis Dashboard')

# Sidebar
st.sidebar.header('Filters')
sex_filter = st.sidebar.multiselect('Select Sex', df['sex'].unique())
education_filter = st.sidebar.multiselect('Select Education Level', df['education_level'].unique())
marital_status_filter = st.sidebar.multiselect('Select Marital Status', df['marital_status'].unique())

# Apply filters
filtered_df = df
if sex_filter:
    filtered_df = filtered_df[filtered_df['sex'].isin(sex_filter)]
if education_filter:
    filtered_df = filtered_df[filtered_df['education_level'].isin(education_filter)]
if marital_status_filter:
    filtered_df = filtered_df[filtered_df['marital_status'].isin(marital_status_filter)]

# Charts
st.header('Visualizations')

# 1. Pie chart: Default Payment Distribution
default_counts = filtered_df['default_payment_next_month'].value_counts()
fig_pie = px.pie(values=default_counts.values, names=default_counts.index, title='Default Payment Distribution')
st.plotly_chart(fig_pie)

# 2. Bar chart: Average Limit Balance by Education Level
avg_limit_balance = filtered_df.groupby('education_level')['limit_balance'].mean().reset_index()
fig_bar = px.bar(avg_limit_balance, x='education_level', y='limit_balance', title='Average Limit Balance by Education Level')
st.plotly_chart(fig_bar)

# 3. Scatter plot: Limit Balance vs. Bill Amount 1
fig_scatter = px.scatter(filtered_df, x='limit_balance', y='bill_amt_1', color='sex', 
                         title='Limit Balance vs. Bill Amount 1', 
                         labels={'sex': 'Sex (1=Male, 2=Female)'})
st.plotly_chart(fig_scatter)

# 4. Line chart: Bill Amounts over 6 months
bill_cols = ['bill_amt_1', 'bill_amt_2', 'bill_amt_3', 'bill_amt_4', 'bill_amt_5', 'bill_amt_6']
bill_data = filtered_df[bill_cols].mean().reset_index()
bill_data.columns = ['Month', 'Average Bill Amount']
bill_data['Month'] = bill_data['Month'].str.extract('(\d+)').astype(int)
fig_line = px.line(bill_data, x='Month', y='Average Bill Amount', title='Average Bill Amount over 6 Months')
st.plotly_chart(fig_line)

# 5. Heatmap: Correlation between numerical variables
numerical_cols = ['limit_balance'] + bill_cols + ['pay_amt_' + str(i) for i in range(1, 7)]
corr_matrix = filtered_df[numerical_cols].corr()
fig_heatmap = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                                        x=corr_matrix.columns,
                                        y=corr_matrix.columns,
                                        colorscale='Viridis'))
fig_heatmap.update_layout(title='Correlation Heatmap of Numerical Variables')
st.plotly_chart(fig_heatmap)

# 6. Box plot: Limit Balance Distribution by Marital Status
fig_box = px.box(filtered_df, x='marital_status', y='limit_balance', 
                 title='Limit Balance Distribution by Marital Status')
st.plotly_chart(fig_box)

# 7. Histogram: Distribution of Pay Amounts
pay_cols = ['pay_amt_1', 'pay_amt_2', 'pay_amt_3', 'pay_amt_4', 'pay_amt_5', 'pay_amt_6']
pay_data = pd.melt(filtered_df[pay_cols], var_name='Pay Period', value_name='Amount')
fig_hist = px.histogram(pay_data, x='Amount', color='Pay Period', 
                        title='Distribution of Pay Amounts',
                        marginal='box', log_y=True)
st.plotly_chart(fig_hist)

# Additional insights
st.sidebar.header('Key Insights')
st.sidebar.write(f"Total number of records: {len(filtered_df)}")
st.sidebar.write(f"Default rate: {filtered_df['default_payment_next_month'].mean():.2%}")
st.sidebar.write(f"Average limit balance: ${filtered_df['limit_balance'].mean():.2f}")
st.sidebar.write(f"Average bill amount (last month): ${filtered_df['bill_amt_1'].mean():.2f}")