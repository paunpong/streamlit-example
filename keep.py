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
list_bar_chart=[]
list_comment=[]
list_stack_str=[]
list_stack_num=[]


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

def check_comma(A):
  for i in A:
    if (', ' in str(i)):
      return True
  return False

def split_comma(A):
  submiss = upload_df[A].values.tolist()
  res = []
  for i in submiss:
    res = res + i.split(", ")
    del_nan = [n for n in res if n != 'ไม่ระบุ']
  return res

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
  mean = np.mean(A)
  sd = np.std(A)
  mean_sd = {'ค่าเฉลี่ย':round(mean,digit),'ส่วนเบี่บงเบนมาตรฐาน':(sd,digit)}
  return mean_sd

#def change_num_to_text(A):
  #x = []
  #dict_change_num_to_text = {5:'มากที่สุด', 4:'มาก', 3:'ปานกลาง', 2:"น้อย", 1:"ควรปรับปรุง",'ไม่ระบุ':'- ไม่ระบุ'}
  #for i in uplode_df[A].values.tolist():
    #x.append(dict_change_num_to_text[i])
  #return x

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

def bar_chart(data,key):
  count_more_than = []
  count_equal = []
  plt.figure(figsize=(9,6))
  for i in set(data):
    if i != 'ไม่ระบุ':
      values = data.count(i)
      if values > 1:
        count_more_than.append(i)
      else:
        count_equal.append(i)

    len_equal = len(count_equal)

    if len_equal > 1:
      values = [data.count(i) for i in count_more_than if i != 'ไม่ระบุ'] + [len_equal]
      labels = [str(i) for i in count_more_than if i != 'ไม่ระบุ'] + ['อื่นๆ']
    else:
      values = [data.count(i) for i in set(data) if i != 'ไม่ระบุ']
      labels = [str(i) for i in set(data) if i != 'ไม่ระบุ']

  plt.bar(labels, values)
  plt.title(key)
  st.pyplot()

def stacked_bar(data,key):
  name = data.keys()
  d_f = pd.DataFrame(data.values(),index=name)
  d_f.plot.barh(stacked=True, figsize=(9,4)).legend(loc='upper right');
  plt.title(key)
  st.pyplot()

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

  if '**' in key:
    list_bar_chart.append(key)
    continue
  
  if '*' in key:
    list_pie_chart[key]=True
    continue

  if '[' in key:
    if num_check(column) and set(column).issubset({1,2,3,4,5,'ไม่ระบุ'}):
      list_stack_num.append(key)
    else:
      list_stack_str.append(key)
    continue

  if check_comma(column):
    list_bar_chart.append(key)
    continue

  if column.count('ไม่ระบุ') > .25*len_column:
    list_comment.append(key)
    continue

  if num_check(column):
    list_boxplot.append(key)
    continue

  if len(set(column)) >.50*len_column:
    list_comment.append(key)
    continue

  if len(set(column)) < 6:
    list_pie_chart[key]=True
  else:
    list_bar_chart.append(key)

for p in list_pie_chart:
  pie_chart(count_list(upload_df[p].values.tolist()),p)

for b in list_boxplot:
  boxplot(upload_df[b].values.tolist(),b)

for a in list_bar_chart:
  v = split_comma(a)
  bar_chart(v,a)

for i in list_comment:
  list_com = upload_df[i].values.tolist()
  bar_chart(list_com,i)

dict_str_stack = dict()
dict_num_stack = dict()

for i in list_stack_str:
  topic_word, sub_word = i.split(' [')[:2]
  topic_word = topic_word.strip()
  sub_word = sub_word.strip().replace(']','')
  A_l = count_list(upload_df[i].values.tolist())
  for k in A_l:
    A_l[k] = A_l[k]['percent']
  if topic_word not in dict_str_stack:
    dict_str_stack[topic_word] = dict()
  dict_str_stack[topic_word][sub_word] = A_l
for i in dict_str_stack:
  stacked_bar(dict_str_stack[i],i)

for i in list_stack_num:
  mat = upload_df[i].values.tolist()
  mean_sd = stat(mat)
  #a = change_num_to_text(i)
  topic_word, sub_word = i.split(' [')[:2]
  topic_word = topic_word.strip()
  sub_word = sub_word.strip().replace(']','')
  for k in A_l:
    A_l[k] = A_l[k]['percent']
  if topic_word not in dict_num_stack:
    dict_num_stack[topic_word] = dict()
  dict_num_stack[topic_word][sub_word] = A_l
for i in dict_num_stack:
  stacked_bar(dict_num_stack[i],i)
  
