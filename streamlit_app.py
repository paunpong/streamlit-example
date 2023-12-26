#import matplotlib as mpl
#import matplotlib.pyplot as plt
import io
import statistics as stat
import re
import operator
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


st.header('โปรแกรมสร้างรายงานสรุปผลจากฟอร์มออนไลน์')

st.title('กรุณาใส่ไฟล์ที่เป็น excel')

upload_file = st.file_uploader("Upload File")

for i in upload_file:
  x = i
  break
y = list(upload_file)[0]


