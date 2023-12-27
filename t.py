import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Install and use a Thai font (e.g., Noto Sans Thai)
font_path = "/path/to/notosansthai_regular.ttf"  # Replace with the path to your installed font file
font_properties = FontProperties(fname=font_path)

# Your Streamlit app code goes here...

# Example data
labels = ['ก', 'ข', 'ค', 'ง', 'จ']
values = [5, 8, 3, 7, 2]

# Create a bar plot
plt.bar(labels, values)

# Set Thai font for the plot
plt.xlabel('แกน X', fontproperties=font_properties)
plt.ylabel('แกน Y', fontproperties=font_properties)
plt.title('กราฟแท่ง', fontproperties=font_properties)

# Display the plot in Streamlit
st.pyplot()
