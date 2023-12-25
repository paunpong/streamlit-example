!wget https://github.com/Phonbopit/sarabun-webfont/raw/master/fonts/thsarabunnew-webfont.ttf
# !pip install -U --pre matplotlib
import matplotlib as mpl
mpl.font_manager.fontManager.addfont('thsarabunnew-webfont.ttf') # 3.2+
mpl.rc('font', family='TH Sarabun New')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import statistics as st
import re
import operator
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
โปรแกรมสร้างรายงานสรุปผลจากฟอร์มออนไลน์
"""
