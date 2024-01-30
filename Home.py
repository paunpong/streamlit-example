import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#st.set_page_config(page_title="Home",initial_sidebar_state="expanded",layout="wide")
st.write('สวัสดี')

list_stack_num={}
list_stack_str={}
digit = int(2)
def upload(A):
  if A is not None:
    y = A.name.split(".")[1]
  if 'xlsx' in y:
    df = pd.read_excel(A)
  elif 'csv' in y:
    df = pd.read_csv(A)
  df.fillna('ไม่ระบุ',inplace=True)
  df.replace('-','ไม่ระบุ',inplace=True)
  df.replace(' ','ไม่ระบุ',inplace=True)
   #st.dataframe(df)  
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

def stacked_bar(data,key):
 fig,ax = plt.subplots()
 name = data.keys()
 data = data.values()
 ax.set_yticklabels(name)
 d_f = pd.DataFrame(data,index=name)
 d_f.plot.barh(stacked=True, figsize=(9,4),ax=ax).legend(bbox_to_anchor=(1, 0, 0.16, 1))
 #stacked_plot.legend(loc='upper right')
 plt.title(key)
 st.pyplot()

def stat(A):
 A = [5 if x == 'มากที่สุด'else(4 if x == 'มาก'else(3 if x == 'ปานกลาง' else(2 if x == 'น้อย' else(1 if x == 'น้อยที่สุด' else(0 if x == 'ไม่ระบุ' else x))))) for x in A]
 mean = np.mean(A)
 sd = np.std(A)
 mean_sd = {'ค่าเฉลี่ย':round(mean,digit),'ส่วนเบี่ยงเบนมาตรฐาน':round(sd,digit)}
 return mean_sd
  
def num_check(A):
  for i in set(A):
    if type(i) is str and i != 'ไม่ระบุ':
      return False
    else:
     continue
  return True

def Split_sub(A):
 for i in A:
  sub = i.split('[')[1]
 return sub

def Count(A,removenan=True):
  if removenan and 'ไม่ระบุ' in A:
    A = [n for n in A if n != 'ไม่ระบุ']
  list_A = list(set(A))
  counta = dict()
  for i in list_A:
    counta[i] = A.count(i)
  return counta

def split_comma(A):
 res = []
 for i in A:
  res = res + i.split(", ")
 return res

def Split(A):
  for i in A:
    topic = i.split('[')[0]
  return topic  

def change_num_to_text(A):
    x = []
    dict_change_num_to_text = {5: 'มากที่สุด', 4: 'มาก', 3: 'ปานกลาง', 2: "น้อย", 1: "ควรปรับปรุง", 'ไม่ระบุ': 'ไม่ระบุ'}
    for i in upload_df[A].values.tolist():  # Corrected variable name
        x.append(dict_change_num_to_text[i])
    return x
  
  
upload_file = st.sidebar.file_uploader(" ",type=["csv", "xlsx"])
upload_df = upload(upload_file)

if upload_file is not None:
  list_topic_stackbar=[]
  list_stackbar=[]
  list_question = [h for h in upload_df]
  if ('Times' or 'ประทับเวลา') in list_question[0]:
    list_question.pop(0)
  for key in list_question:
    column = upload_df[key].values.tolist()
    len_column = len(column)
    x = Count(column)
    if '[' in key:
      list_stackbar.append(key)
      topic = Split(list_stackbar)
      list_topic_stackbar.append(topic)
  set_topic = set(list_topic_stackbar)
  for i in set_topic:
    col = []
    for n in list_stackbar:
      if i in n:
        col.append(n)
    Column = upload_df[col].values.tolist()
    sum_Column = sum(Column,[])
    if num_check(sum_Column)and set(sum_Column).issubset({1,2,3,4,5,'ไม่ระบุ'}):
      for key in col:
        list_stack_num[key]=True
    else:
      for key in col:
        list_stack_str[key]=True
        
if upload_file is not None:
  list_num_key = list(list_stack_num.keys())
  list_str_key = list(list_stack_str.keys())
  tab1, tab2 = st.sidebar.tabs(['ประเภทแผนภูมิ', 'ปรับแต่งรายระเอียดแผนภูมิ'])
  with tab1:
    x = 1000
    endtext =""
    topic_long = st.radio('แสดงหัวข้อแบบย่อ', ['ใช่', 'ไม่ใช่'], horizontal=True)
    if topic_long =="ใช่":
      x=32
      endtext = "ฯ"
    numberitem = 0
    
    for topic in list_str_key:
      s = Split_sub(topic)
      st.write(s)
      numberitem = numberitem+1
      strnumberitem = str(numberitem)+')'
      head_bulet = strnumberitem + topic
      str_val = st.radio(head_bulet,['แผนภูมิแท่งแบบต่อกัน'], horizontal=True)
      st.text("")
    for topic in list_num_key:
      numberitem = numberitem+1
      strnumberitem = str(numberitem)+')'
      head_bulet = strnumberitem + topic
      num_val = st.radio(head_bulet,['แผนภูมิแท่งแบบต่อกัน'], horizontal=True)
      st.text("")
  
    


top_name = None  
dict_num_stack={}
for i in list_stack_num:
    mat = upload_df[i].values.tolist()
    mean_sd = stat(mat)
    a = change_num_to_text(i)
    topic_word, sub_word = i.split(' [')[:2]
    topic_word = topic_word.strip()
    sub_word = sub_word.strip().replace(']', '')
    if topic_word != top_name:
      top_name = topic_word
    A_l = count_list(a)
    for k in A_l:
      A_l[k] = A_l[k]['percent']
    if topic_word not in dict_num_stack:
      dict_num_stack[topic_word] = dict()
    dict_num_stack[topic_word][sub_word] = A_l
    for i in dict_num_stack:
      stacked_bar(dict_num_stack[i],i)


