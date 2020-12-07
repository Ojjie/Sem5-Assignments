import pandas as pd

fname = "LBW_dataset.csv"
df = pd.read_csv(fname)

#cleaning data
df = df.drop(columns=['Education'])
df = df.interpolate()
df['Community'] = df['Community'].round()
df['Delivery phase'] = df['Delivery phase'].round()
df['IFA'] = df['IFA'].round()


#df = df.round()
mean_weight = df['Weight'].mean()
mean_age = df['Age'].mean()
mean_hb = df['HB'].mean()
mean_bp = df['BP'].mean()

std_weight = df['Weight'].std()
std_age = df['Age'].std()
std_hb = df['HB'].std()
std_bp = df['BP'].std()

# In the below code we standardise the data so that there is no unnecessary bias in the neural network.
# mean_x --> mean of column x
# std_x --> standard deviation of column x
df.loc[:, 'Weight'] = df.Weight.apply(lambda x : (x - mean_weight) / std_weight )
df.loc[:, 'Age'] = df.Age.apply(lambda x : (x - mean_age) / std_age)
df.loc[:, 'HB'] = df.HB.apply(lambda x : (x - mean_hb) / std_hb)
df.loc[:, 'BP'] = df.BP.apply(lambda x : (x - mean_bp) / std_bp)

df.to_csv("LBW_Dataset_Cleaned.csv")