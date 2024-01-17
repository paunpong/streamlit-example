import streamlit as st
st.set_page_config(page_title="Home",initial_sidebar_state="expanded",layout="wide")
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


