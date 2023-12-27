import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Find the font file for 'TH Sarabun New'
font_path = fm.findfont(fm.FontProperties(family='TH Sarabun New'))

# Check if the font was found
if font_path:
    st.success(f"Found font at: {font_path}")
else:
    st.error("Font not found. Make sure 'TH Sarabun New' is installed on your system.")

# Example data
labels = ['ก', 'ข', 'ค', 'ง', 'จ']
values = [5, 8, 3, 7, 2]

# Create a bar plot without specifying font
plt.bar(labels, values)

# Display the plot in Streamlit
st.pyplot()




