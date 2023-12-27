import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Specify the font properties
font_properties = {'family': 'TH Sarabun New', 'weight': 'normal', 'size': 12}

# Example data
labels = ['ก', 'ข', 'ค', 'ง', 'จ']
values = [5, 8, 3, 7, 2]

# Create a bar plot with specified font
fig, ax = plt.subplots()
ax.bar(labels, values)

# Set font properties for the plot
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(FontProperties(**font_properties))

ax.set_xlabel('แกน X', **font_properties)
ax.set_ylabel('แกน Y', **font_properties)
ax.set_title('กราฟแท่ง', **font_properties)

# Display the plot in Streamlit
st.pyplot(fig)




