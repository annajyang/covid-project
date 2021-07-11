import pandas as pd
import numpy as np
import scipy

raw_data = pd.read_csv("us-daily-covid-vaccine-doses-administered.csv")

s = set()
for i, r in raw_data.iterrows():
    s.add(r["Entity"])
    
df = pd.DataFrame(columns=["State", "Vacc_Rate", "Case_Rate"])

def in_march(s):
    if s[6] == "3":
        return True
    return False

for state in s:
    data = raw_data.loc[(raw_data["Entity"] == state) & (raw_data["Day"].apply(in_march))]["daily_vaccinations"]
    #print (data.shape)
    arr = np.array(data)
    df.loc[df.shape[0]] = [state, scipy.stats.linregress(np.arange(1, arr.size+1), y=arr).slope, ""]
    #if state == "Alabama":
        #print (arr)

