font_properties = {'family': 'TH Sarabun New', 'weight': 'normal', 'size': 12}
import matplotlib.font_manager as fm

font_path = fm.findfont(FontProperties(family='TH Sarabun New'))
print(f"Found font at: {font_path}")
import streamlit as st
import matplotlib.pyplot as plt

# Example data
labels = ['ก', 'ข', 'ค', 'ง', 'จ']
values = [5, 8, 3, 7, 2]

# Create a bar plot without specifying font
plt.bar(labels, values)

# Display the plot in Streamlit
st.pyplot()



