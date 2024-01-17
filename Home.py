import streamlit as st
import numpy as np
import pandas as pd
#st.set_page_config(page_title="Home",initial_sidebar_state="expanded",layout="wide")
st.write('สวัสดี')

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

upload_file = st.sidebar.file_uploader(" ",type=["csv", "xlsx"])
upload_df = upload(upload_file)

list_topic_stackbar=set()
list_stackbar=[]

if upload_file is not None:
  list_question = [h for h in upload_df]
  if ('Times' or 'ประทับเวลา') in list_question[0]:
    list_question.pop(0)
  for key in list_question:
   column = upload_df[key].values.tolist()
   len_column = len(column)
   x = Count(column)
   if '[' in key:
     list_topic_stackbar.append(key.split('[')[0])
      
