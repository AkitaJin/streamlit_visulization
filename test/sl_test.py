'''
Descripttion: 
version: 
Author: Jin
Date: 2021-07-01 13:49:34
LastEditors: Jin
LastEditTime: 2021-07-02 09:46:12
'''
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
# 2 
# st.title('My first app')
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
# 'first column': [1, 2, 3, 4],
# 'second column': [10, 20, 30, 40]
# }))

# 3
"""
# 3
## My first app
Here's our first attempt at using data to create a table:
"""
df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
})
df

"""
# 4
## 4.1 Draw a line chart
"""
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)

"""
## 4.2 Plot a map
"""
map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)


"""
# 5
## 5.1 Use checkboxes to show/hide dat
"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
    chart_data

# """
# 5.2 Use a selectbox for options
# """
# option = st.selectbox(
#         'Which number do you like best?',
#         df['first column'])
# 'You selected: ', option

"""
# 6 LAY OUT YOUR APP
## 6.1 Sidebar-selectbox
"""
option = st.sidebar.selectbox(
        'Which number do you like best?',
        df['first column'])
'You selected:', option

"""
## beta_columns & beta_expander
"""
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

"""
# 7 SHOW PROGRESS
"""
import time
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1) 

'...and now we\'re done!'