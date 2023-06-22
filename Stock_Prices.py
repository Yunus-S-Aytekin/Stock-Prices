import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import mplcyberpunk

df = pd.read_csv("stock_data.csv")
dates = [df["Date"].iloc[i] for i in np.round(np.linspace(0,1711,8)).astype(int)]

plt.style.use("cyberpunk")
# https://matplotlib.org/stable/tutorials/introductory/customizing.html
fig = plt.figure()

line = plt.plot(df["Date"],df["FB"],c="#4267B2",label="Facebook",picker=True)
plt.plot(df["Date"],df["TWTR"],c="#1DA1F2",label="Twitter")
plt.plot(df["Date"],df["NFLX"],c="#E50914",label="Netflix")

for y,c in zip(["FB","TWTR","NFLX"],["#4267B2","#1DA1F2","#E50914"]):
    for w in range(10):
        plt.plot(df["Date"],df[y],c=c,alpha=0.06,linewidth=2+(w))

plt.fill_between(df["Date"],df["NFLX"],df["FB"], color="#E50914", alpha=0.3, where=(df["NFLX"]>=df["FB"]))
plt.fill_between(df["Date"],df["FB"],df["TWTR"], color="#4267B2", alpha=0.3)
plt.fill_between(df["Date"],df["TWTR"],[0]*len(df), color="#1DA1F2", alpha=0.3)

plt.xticks(dates)
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title("Stock Prices")
plt.xlim(dates[0],dates[7])
plt.ylim(0,600)
plt.legend()
plt.show()