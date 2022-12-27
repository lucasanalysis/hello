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
import pandas
import numpy
import streamlit_pandas_profiling
import streamlit_shap
import tensorflow
import cv2
packages_list=['matplotlib','torch','pandas_profiling','skimage','lime','tqdm','xgboost','lightgbm','openTSNE','shap','bokeh','torchvision','deepchecks',
              'pandas','numpy','base64','PIL','streamlit_pandas_profiling','streamlit_shap','tensorflow','cv2']
for i in packages_list:
  if i in sys.modules.keys():
    st.write(i)
st.write('end')
