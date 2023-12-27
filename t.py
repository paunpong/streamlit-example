import streamlit as st
import matplotlib.pyplot as plt

# Install and use a Thai font (e.g., Noto Sans Thai)
font_path = "/path/to/notosansthai_regular.ttf"  # Replace with the path to your installed font file
font_properties = {'family': 'Noto Sans Thai', 'weight': 'normal', 'size': 12}

# Your Streamlit app code goes here...

# Example data
labels = ['ก', 'ข', 'ค', 'ง', 'จ']
values = [5, 8, 3, 7, 2]

# Create a bar plot
plt.bar(labels, values)

# Set Thai font for the plot
plt.xlabel('แกน X', **font_properties)
plt.ylabel('แกน Y', **font_properties)
plt.title('กราฟแท่ง', **font_properties)

# Display the plot in Streamlit
st.pyplot()

