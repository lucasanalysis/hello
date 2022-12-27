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
import shap
import pytorch_grad_cam
import torchvision
import PIL
import bokeh
packages_list=['matplotlib','torch','pandas_profiling','skimage','lime','tqdm','xgboost','lightgbm','pytorch_grad_cam','shap','PIL','bokeh','torchvision']
for i in packages_list:
  if i in sys.modules.keys():
    st.write(i)
st.write('end')
