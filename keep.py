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

st.set_option('deprecation.showPyplotGlobalUse', False)

digit = int(2)
list_pie_chart = {}
list_boxplot=[]

def upload(A):
  if upload_file is not None:
    y = upload_file.name.split(".")[1]
    if 'xlsx' in y:
      df = pd.read_excel(upload_file)
    elif 'csv' in y:
      df = pd.read_csv(upload_file)
  
    df.fillna('ไม่ระบุ',inplace=True)
    df.replace('-','ไม่ระบุ',inplace=True)
    st.dataframe(df)  
    return df

def num_check(A):
  for i in set(A):
    if type(i) is str and i != 'ไม่ระบุ':
      return False
    else:
      continue
  return True

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

def boxplot(data,key):
  plt.boxplot(data,showmeans=True)
  q1 = np.percentile(data,25)
  q3 = np.percentile(data,75)
  #mean = stat.mean(data)
  median = np.median(data)
  average = np.mean(data)
  outlier_above = q3+(q3-q1)*1.5
  outlier_below = q1-(q3-q1)*1.5
  c = [x for x in data if (x < outlier_below or x > outlier_above)]
  c = list(set(c))
  c.sort()
  if len(c) > 0:
    for i in range(len(c)):
      plt.text(1.1,c[i],f"Outlier_{i+1}:{c[i]:.{digit}f}")
      data = [x for x in data if x not in c]
      max = np.max(data)
      min = np.min(data)
      plt.text(1.1,max,f'Max:{max:.{digit}f}')
      plt.text(1.1,min,f'Min:{min:.{digit}f}')
  else:
    max = np.max(data)
    min = np.min(data)
    plt.text(1.1,max,f'Max:{max:.{digit}f}')
    plt.text(1.1,min,f'Min:{min:.{digit}f}')
    
  plt.text(1.1,q1,f'Q1: {q1:.{digit}f}')
  plt.text(1.1,q3,f'Q3: {q3:.{digit}f}')
  plt.text(1.1, median, f'Q2: {median:.{digit}f}')
  plt.text(1.22, average, f'Average: {average:.{digit}f}')
  plt.title(key)
  st.pyplot()

st.header('โปรแกรมสร้างรายงานสรุปผลจากฟอร์มออนไลน์')
st.title('กรุณาใส่ไฟล์ที่เป็น excel')
upload_file = st.file_uploader("Upload File",type=["csv", "xlsx"])

upload_df = upload(upload_file)
#list_query = question(upload_df)

#list_question = [h for h in upload_df]

#if ('Times' or 'ประทับเวลา') in list_question[0]:
  #list_question.pop(0)
list_question = [h for h in upload_df]
if ('Times' or 'ประทับเวลา') in list_question[0]:
  list_question.pop(0)
  
for key in list_question:
  column = upload_df[key].values.tolist()
  len_column = len(column)
  
  if '*' in key:
    list_pie_chart[key]=True
    continue

  if num_check(column):
    list_boxplot.append(key)
    continue
  

for p in list_pie_chart:
  pie_chart(count_list(upload_df[p].values.tolist()),p)

for b in list_boxplot:
  boxplot(upload_df[b].values.tolist(),b)
