'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
	entropy = 0 
	unique_values = df.iloc[:,-1].unique()

	for value in unique_values:
		p_i = df.iloc[:,-1].value_counts()[value]/len(df.iloc[:,-1])  #try with nunique
		entropy += -p_i*np.log2(p_i)

	return entropy


'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
	entropy_of_attribute = 0
	unique_values_attribute = df[attribute].unique()
	unique_values = df.iloc[:,-1].unique()
	length = len(df.iloc[:,-1])
	for val in unique_values_attribute:
		entropy = 0
		indices = df[df[attribute] == val].index
		prop = df[attribute].value_counts()[val]/length
		final_col = []
		for index in indices:
			final_col.append(df.iloc[index][df.columns[-1]])
		for value in unique_values:
			p_i = final_col.count(value)/len(final_col)
			if(p_i != 0):
				entropy -= p_i*np.log2(p_i)
		entropy_of_attribute += prop*entropy
	return abs(entropy_of_attribute)



'''Return Information Gain of the attribute provided as parameter'''
	#input:int/float/double/large,int/float/double/large
	#output:int/float/double/large
def get_information_gain(df,attribute):
	information_gain = 0
	information_gain = get_entropy_of_dataset(df) - get_entropy_of_attribute(df,attribute)
	return information_gain


''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
   
	information_gains={}
	selected_column=''

	'''
	Return a tuple with the first element as a dictionary which has IG of all columns 
	and the second element as a string with the name of the column selected

	example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
	'''
	frame = df.iloc[:,0:-1]
	for (columnName, columnData) in frame.iteritems():
		information_gains[columnName]=get_information_gain(df, columnName)
	selected_column = max(information_gains, key=information_gains.get)
	return (information_gains,selected_column)


'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''

