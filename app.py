#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import joblib

# Title
st.header("Boston House Price Prediction")

# Input bar 1
crim = st.number_input("Enter CRIM")
zn = st.number_input("Enter ZN")
indus = st.number_input("Enter INDUS")

nox = st.number_input("Enter NOX")
rm = st.number_input("Enter RM")
age = st.number_input("Enter AGE")
dis = st.number_input("Enter DIS")
rad = st.number_input("Enter RAD")
tax = st.number_input("Enter TAX")
ptratio = st.number_input("Enter PTRATIO")
b = st.number_input("Enter B")

lstat = st.number_input("Enter Lstat")

chas = st.selectbox("Select CHAS", (0, 1))

if st.button("Submit"):
    
    # Unpickle classifier
    lr = joblib.load("lr.pkl")
    

    X=pd.DataFrame([[crim,zn,indus,nox,rm,age,dis,rad,tax,ptratio,b,lstat,chas]],columns=['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
           'PTRATIO', 'B', 'LSTAT','CHAS'])

    prediction = lr.predict(X)[0]               
    st.text(f"The house price is  {prediction}")               


# In[ ]:



