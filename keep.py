import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager as fm
from matplotlib.font_manager import FontProperties
#import statistics as stat
#import io
#import re
#import operator
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

script_dir = os.path.dirname(os.path.abspath(__file__))
thai_font_path = os.path.join("Sarabun-Regular.ttf")
thai_font_prop = fm.FontProperties(fname=thai_font_path)


def add_font_thai():
 fig,ax = plt.subplots()
 wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct=f'%.{digit}f', textprops={'fontproperties': thai_font_prop})
 for text in texts + autotexts:
  text.set_fontproperties(thai_font_prop)



digit = int(2)
list_pie_chart = {}
list_boxplot=[]
list_bar_chart=[]
list_comment=[]
list_stack_str=[]
list_stack_num=[]

def upload(A):
 y = A.name.split(".")[1]
 if 'xlsx' in y:
  df = pd.read_excel(A)
 elif 'csv' in y:
  df = pd.read_csv(A)
 df.fillna('ไม่ระบุ',inplace=True)
 df.replace('-','ไม่ระบุ',inplace=True)
   #st.dataframe(df)  
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
 mean_sd = {'ค่าเฉลี่ย':round(mean,digit),'ส่วนเบี่ยงเบนมาตรฐาน':round(sd,digit)}
 return mean_sd

def change_num_to_text(A):
 x = []
 dict_change_num_to_text = {5:'มากที่สุด', 4:'มาก', 3:'ปานกลาง', 2:"น้อย", 1:"ควรปรับปรุง",'ไม่ระบุ':'- ไม่ระบุ'}
 for i in uplode_df[A].values.tolist():
  x.append(dict_change_num_to_text[i])
 return x

def pie_chart(data, key):
 labels = [str(key) for key in data]
 counts = [data[key]['percent'] for key in data]
 fig,ax = plt.subplots()
 wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct=f'%.{digit}f', textprops={'fontproperties': thai_font_prop})
 for text in texts + autotexts:
  text.set_fontproperties(thai_font_prop)
 #ax.legend(wedges, labels, title="Legend", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), prop=thai_font_prop)
 plt.title(key, fontproperties=thai_font_prop)
 st.pyplot()

def boxplot(data,key):
 #fig, ax = plt.subplots()
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

upload_file = st.file_uploader(" ",type=["csv", "xlsx"])
#run_program = st.button('run program')

upload_df = upload(upload_file)
if upload_df is not None:
 #-------------------------------------------------แยกหัวข้อ----------------------------------------------------#
 list_question = [h for h in upload_df]
 if ('Times' or 'ประทับเวลา') in list_question[0]:
  list_question.pop(0)
  
 for key in list_question:
  column = upload_df[key].values.tolist()
  len_column = len(column)
  
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


  #-------------------------------------------------แสดงข้อมูลและแผนภูมิ----------------------------------------------------#      
table_head = ['หัวข้อ' , 'จำนวน' , 'เปอร์เซ็นต์']
table_data = []
#st.write('หัวข้อ' , '\t' , 'จำนวน' , '\t' , 'เปอร์เซ็นต์')
for p in list_pie_chart:
  values = count_list(upload_df[p].values.tolist(), list_pie_chart[p])
  for k in values:
    count = values[k]['count']
    percent = values[k]['percent']
    table_data.append([k, count, percent])
    #st.write(k , '\t' , count , '\t' , percent)
st.table([table_head, *table_data])
for p in list_pie_chart:
  pie_chart(count_list(upload_df[p].values.tolist()),p)

st.write('หัวข้อ','ค่าเฉลี่ย','ส่วนเบี่ยงเบนมาตรฐาน')
for b in list_boxplot:
  mean_sd = stat(upload_df[b].values.tolist())
  mean = mean_sd['ค่าเฉลี่ย']
  std = mean_sd['ส่วนเบี่ยงเบนมาตรฐาน']
  st.write(b , mean , std)
for b in list_boxplot:
 st.write(b)
 boxplot(upload_df[b].values.tolist(),b)

st.write('หัวข้อ' , 'จำนวน' , 'เปอร์เซ็นต์')
for a in list_bar_chart:
  list_values = upload_df[a].values.tolist()
  list_free = []
  for r in list_values:
    list_free = list_free + r.split(", ")
  if list_free != 0:
    set_list = list(set(list_free))
    v = count_list(list_free)
  st.write(a , len(list_free) , 100)
  for k in v:
    count = v[k]['count']
    percent = v[k]['percent']
    st.write(k , count ,  percent)
for a in list_bar_chart:
  v = split_comma(a)
  bar_chart(v,a)

other = False
for c in list_comment:
  x = []
  st.write(c)
  list_com = upload_df[c].values.tolist()
  del_nan = [n for n in list_com if n != 'ไม่ระบุ']
  set_list = list(set(del_nan))
  counts = [(k, list_com.count(k))for k in set_list]
  counts.sort(key=lambda x: x[1], reverse=True)
  for k, count in counts:
    if count > 1:
      st.write(f"{k} [{count}]")
    elif not other:
      st.write('อื่นๆ')
      other = True
    else:
      st.write('\t', '-', k)   
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
for s in dict_str_stack:
  name_top = ''
  st.write(f'{"หัวข้อ"} {"จำนวน(เปอร์เซ็นต์)"}')
  for t in dict_str_stack[s]:
    name = s+f' [{t}]'
    answer = count_list(upload_df[name].values.tolist())
    #st.write(answer)

  stacked_bar(dict_str_stack[s],s)

st.write('หัวข้อ' , 'ค่าเฉลี่ย' , 'ส่วนเบี่ยงเบนมาตรฐาน' , 'สรุป')
top_name = ''
for i in list_stack_num:
  mat = upload_df[i].values.tolist()
  mean_sd = stat(mat)
  #a = change_num_to_text(i)
  topic_word, sub_word = i.split(' [')[:2]
  topic_word = topic_word.strip()
  sub_word = sub_word.strip().replace(']','')
  if topic_word != top_name:
    st.write(topic_word)
    top_name = topic_word
  A_l = count_list(upload_df[i].values.tolist())
  for k in mean_sd:
    mean = mean_sd['ค่าเฉลี่ย']
    s_d = mean_sd['ส่วนเบี่ยงเบนมาตรฐาน']
  if mean >= 4.2:
    st.write(f"{sub_word} {mean} {s_d} {'มากที่สุด'}")
  elif mean >= 3.4:
    st.write(f"{sub_word} {mean} {s_d} {'มาก'}")
  elif mean >= 2.6:
    st.write(f"{sub_word} {mean} {s_d} {'ปานกลาง'}")
  elif mean >= 1.8:
    st.write(f"{sub_word} {mean} {s_d} {'น้อย'}")
  elif mean < 1.8:
    st.write(f"{sub_word} {mean} {s_d} {'น้อยที่สุด'}")
  for k in A_l:
    A_l[k] = A_l[k]['percent']
  if topic_word not in dict_num_stack:
    dict_num_stack[topic_word] = dict()
  dict_num_stack[topic_word][sub_word] = A_l
for i in dict_num_stack:
  stacked_bar(dict_num_stack[i],i)
 
d =st.radio(
    "What's your favorite movie genre",
    ['a','b','c'],
    index=1)


st.write(d)

