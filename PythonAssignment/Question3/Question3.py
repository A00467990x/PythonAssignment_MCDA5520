#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:29:31 2023

@author: sammy
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title("Question 3 Streamlit App")
uploaded_file = st.file_uploader("Upload CSV file here: ", type = "csv", accept_multiple_files= False)


if uploaded_file is not None:
    st.write("filename:", uploaded_file.name)
    st.write("dataframe preview: ")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
    # st.write("Age value: ")
    # st.write(dataframe["Age"])
    
    st.write("Histogram preview: ")
    
    x = dataframe["Age"]
    plt.hist(x)
    plt.title('Age Histogram')
    st.pyplot()