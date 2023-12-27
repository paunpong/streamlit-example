# download font file มาก่อน
!wget https://awards.opdc.go.th/awards_opdc/assets/fonts/THSarabunNew/THSarabunNew.ttf

# import and install
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_list = fm.createFontList(['THSarabunNew.ttf'])
fm.fontManager.ttflist.extend(font_list)

# set font
plt.rcParams['font.family'] = 'TH Sarabun New'
plt.rcParams['xtick.labelsize'] = 20.0
plt.rcParams['ytick.labelsize'] = 20.0
# plot
st.bar(['ก','ข','ค'], [1,2,3]);




