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

digit = int(2)

def upload(A):
  if upload_file is not None:
    y = upload_file.name.split(".")[1].lower()
    if 'xlsx' in y:
      df = pd.read_excel(upload_file)
    elif 'csv' in y:
      df = pd.read_csv(upload_file)
  
    df.fillna('ไม่ระบุ',inplace=True)
    df.replace('-','ไม่ระบุ',inplace=True)
    st.dataframe(df)

def count_list(A,removenan=True):
  if removenan and 'ไม่ระบุ'in A:
    A = [n for n in A if n != 'ไม่ระบุ']
  list_A = list(set(A))
  count_dict = dict()
  len_A = len(A)
  for c in list_A:
    per = (A.count(c)/len_A)*100
    count_dict[c] = {"count":A.count(c),"percent":round(per,digit)}
  return count_dict    

st.header('โปรแกรมสร้างรายงานสรุปผลจากฟอร์มออนไลน์')
st.title('กรุณาใส่ไฟล์ที่เป็น excel')
upload_file = st.file_uploader("Upload File",type=["csv", "xlsx"])

upload(upload_file)

