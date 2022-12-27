import streamlit as st
import matplotlib
import torch
import pandasProfiling
st.write('hello world')
import sys
packages_list=['matplotlib','torch','pandasProfiling']
for i in packages_list:
  if i in sys.modules.keys():
    st.write(i)
st.write('end')
