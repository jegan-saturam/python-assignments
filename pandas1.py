import pandas as pd
import time

health_df = pd.read_csv('health care diabetes.csv')

#print(health_df.columns)
#print(health_df.shape)
#print(health_df.info())

start = time.time()
#print(health_df.head())
print(health_df.describe())
end = time.time()
print("The time of execution of pandas program is :", end-start)



