import streamlit as st
import numpy as np
import pandas as pd
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

def change_num_to_text(A):
    x = []
    dict_change_num_to_text = {5: 'มากที่สุด', 4: 'มาก', 3: 'ปานกลาง', 2: "น้อย", 1: "ควรปรับปรุง", 'ไม่ระบุ': 'ไม่ระบุ'}
    for i in upload_df[A].values.tolist():  # Corrected variable name
        x.append(dict_change_num_to_text[i])
    return x

table_data5 = []  # Assuming you've defined table_data5 somewhere before this code snippet
top_name = None   # Assuming you've defined top_name somewhere before this code snippet

for i in list_stack_num:
    mat = upload_df[i].values.tolist()
    mean_sd = stat(mat)
    a = change_num_to_text(i)
    topic_word, sub_word = i.split(' [')[:2]
    topic_word = topic_word.strip()
    sub_word = sub_word.strip().replace(']', '')
    if topic_word != top_name:
        table_data5.append([topic_word, '', '', ''])
        top_name = topic_word
    A_l = count_list(a)

st.write(list_stack_num,'num')
st.write(list_stack_str,'str')
