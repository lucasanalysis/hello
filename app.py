import streamlit as st
import matplotlib
import torch
import pandas_profiling
st.write('hello world')
import sys
import skimage
import lime
import tqdm
import xgboost
import lightgbm
import torchvision
import bokeh
import shap
import openTSNE
import deepchecks
packages_list=['matplotlib','torch','pandas_profiling','skimage','lime','tqdm','xgboost','lightgbm','openTSNE','shap','bokeh','torchvision','deepchecks']
for i in packages_list:
  if i in sys.modules.keys():
    st.write(i)
st.write('end')
