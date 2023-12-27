import matplotlib as mpl
import matplotlib.pyplot as plt
import io
import statistics as stat
import re
import operator
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.header('โปรแกรมสร้างรายงานสรุปผลจากฟอร์มออนไลน์')
st.title('กรุณาใส่ไฟล์ที่เป็น excel')
upload_file = st.file_uploader("Upload File",type=["csv", "xlsx"])

if upload_file is not None:
  if upload_file.type == '.csv':
    df = df = pd.read_csv(upload_file)
  else:
    df = pd.read_excel(upload_file)

  df.fillna('ไม่ระบุ',inplace=True)
  df.replace('-','ไม่ระบุ',inplace=True)
  st.dataframe(df)
