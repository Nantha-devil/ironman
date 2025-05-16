import pandas as pd 
df= pd.read_csv("Google_data.csv")
#all data are print
print(df)
#divit categories and types 
df.info()
#missing value and sum is total of missing value
missing_value = df.isnull().sum()
print(missing_value)
mean_value=df["Rating"].mean()
print("mean_value",mean_value)
#describe() is total of mean, std, min,max. %,count
print(df.describe())    
# T is use transport (colum ma irukaratha row va matharathu)
print(df.describe().T)    
# include use pannuna letterla varum numberla varathu user easy full
print(df.describe(include='object'))