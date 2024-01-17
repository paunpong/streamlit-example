import streamlit as st
import numpy as np
import pandas as pd
#st.set_page_config(page_title="Home",initial_sidebar_state="expanded",layout="wide")
st.write('สวัสดี')

list_stack_num={}
list_stack_str={}

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

def Split(A):
  for i in A:
    topic_word = i.split('[')[0]
    set_topic = topic_word
    #topic_word = topic_word.strip() 
  return set_topic  
  
  
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
        col += n
    #if num_check(Column) and set(Column).issubset({1,2,3,4,5,'ไม่ระบุ'}):
      #st.write('11')
      #for key in list_stackbar:
        #st.write(key)
        #for topic in key:
          #st.write(topic)
    
    
            
    
      
      
