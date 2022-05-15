import streamlit as st
import numpy as np
import pandas as pd


def app(df):

	st.header('Diabetes prediction app')
	st.text('''
		Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
		There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
		This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.''')


	st.subheader('View data')
	with st.beta_expander('View dataset'):
		st.table(df)
	st.subheader('Column description')
	if st.checkbox('Show summary'):
		st.table(df.describe())


	beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
	with beta_col1:
		if st.checkbox('Show column names'):
			st.table(df.columns)
	with beta_col2:
		if st.checkbox('Show column datatypes'):
			st.table(df.dtypes)
	with beta_col3:
		if st.checkbox('View column data'):
			cols = st.selectbox('Select column',(df.columns))
			st.table(df[cols])	