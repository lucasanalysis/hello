import streamlit as st
import matplotlib
import torch
import pandas_profiling
st.write('hello world')
import sys
packages_list=['matplotlib','torch','pandas_profiling']
for i in packages_list:
  if i in sys.modules.keys():
    st.write(i)
st.write('end')
