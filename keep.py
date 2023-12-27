import matplotlib as mpl
import matplotlib.pyplot as plt
import statistics as stat
#import io
#import re
#import operator
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from matplotlib.font_manager import FontProperties
font_path = "/path/to/notosansthai_regular.ttf"  # Replace with the path to your installed font file
font_properties = FontProperties(fname=font_path)

st.set_option('deprecation.showPyplotGlobalUse', False)

digit = int(2)
list_pie_chart = {}

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
    return df
    
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

def stat(A):
  mean = stat.mean(A)
  sd = stat.stdev(A)
  mean_sd = {'ค่าเฉลี่ย':round(mean,digit),'ส่วนเบี่บงเบนมาตรฐาน':(sd,digit)}
  return mean_sd

def pie_chart(data,key):
  labels = [str(key) for key in data]
  counts = [data[key]['percent']for key in data]
  #x,ax = plt.subplots()
  plt.pie(counts, labels=labels, autopct=f'%.{digit}f')
  plt.title(key)
  st.pyplot()
  #plt.show()

st.header('โปรแกรมสร้างรายงานสรุปผลจากฟอร์มออนไลน์')
st.title('กรุณาใส่ไฟล์ที่เป็น excel')
upload_file = st.file_uploader("Upload File",type=["csv", "xlsx"])

upload_df = upload(upload_file)

list_question = [h for h in upload_df]

if ('Times' or 'ประทับเวลา') in list_question[0]:
  list_question.pop(0)

for key in list_question:
  column = upload_df[key].values.tolist()
  len_column = len(column)
  
  if '*' in key:
    list_pie_chart[key]=True
    continue

for p in list_pie_chart:
  pie_chart(count_list(upload_df[p].values.tolist()),p)
