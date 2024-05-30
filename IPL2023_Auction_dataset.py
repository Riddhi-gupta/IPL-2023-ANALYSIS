#We will now Import the IPL 2023 Auction dataset using pandas
#We are using the IPL 2023 Auction dataset here.

#copy the given below url to see the source of dataset
#https://www.kaggle.com/datasets/rajkumarpandey02/ipl-player-auction-dataset-2023

df = pd.read_csv('IPL_Squad_2023_Auction_Dataset.csv') 
print(df.shape) 
df.head()
