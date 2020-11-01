from Assignment1 import *

df = pd.read_csv("test.csv")

print(get_entropy_of_dataset(df))

for i in 'ABCD':
    print(i,":",get_entropy_of_attribute(df,i))

print(get_selected_attribute(df))