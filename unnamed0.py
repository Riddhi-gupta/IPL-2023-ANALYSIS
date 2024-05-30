#Drop the “Unnamed: 0” column from the dataset

df.drop(['Unnamed: 0'], axis=1, inplace=True) 
df.head()
