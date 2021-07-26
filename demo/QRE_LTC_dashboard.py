'''
Descripttion: 
version: 
Author: Jin
Date: 2021-07-05 08:23:24
LastEditors: Jin
LastEditTime: 2021-07-05 15:07:16
'''
import streamlit as st
import pandas as pd
import numpy as np
import psycopg2

"""
load data
"""



@st.cache
def load_data():
    ## 连接到一个给定的数据库
    conn = psycopg2.connect(database="postgres", user="postgres",
                            password="123456", host="192.168.51.94", port="5432")
    ## 建立游标，用来执行数据库操作
    cursor = conn.cursor()

    ## 执行SQL命令
    #cursor.execute("DROP TABLEO  test_conn")
    #cursor.execute("CREATE TABLE test_conn(id int, name text)")
    #cursor.execute("INSERT INTtest_conn values(1,'haha')")

    ## 提交SQL命令
    conn.commit()

    ## 执行SQL SELECT命令
    cursor.execute("select * from ods_jt_zcjg")

    ## 获取SELECT返回的元组
    rows = cursor.fetchall()
    # for row in rows:
    #     print('id = ',row[0], 'name = ', row[1])
    df = pd.DataFrame(rows)

    ## 关闭游标
    cursor.close()

    ## 关闭数据库连接
    conn.close()

    # data = pd.read_csv(DATA_URL, nrows=nrows)
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return df

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)