import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import numpy_financial as npf
import seaborn as sns

#meanint=.04
meanint=float(input("Please provide the mean interest rate: "))
#ensuring the input is converted to a decimal for later calculations
if meanint >1:
    meanint=meanint/100

#sdint=.01
sdint=float(input("Enter the Standard deviation: "))
#ss=30
ss=int(input("Enter the sample size: "))
trials=100000
n=10
pv=0
pmt=10
nbin=11

values=[0]*trials
values2=[0]*trials


i=0
while i<trials:
    interestrates=np.random.normal(meanint,sdint,ss)
    fvl=npf.fv(interestrates,n,-pmt,pv,0)
    values[i]=np.mean(fvl)
    fv2=npf.fv(interestrates,n,-pmt,pv,1)
    values2[i]=np.mean(fv2)
    i+=1

#alpha adds transperency, useful when overlapping charts are needed
plt.hist(values,bins=nbin,alpha=.5,color="red", edgecolor="grey",
         label="Future value of ordinary annuity")
plt.hist(values2,bins=nbin,alpha=.5,color="blue", edgecolor="grey",
         label="Future value of annuity due")
plt.title("Distribution of future values")
plt.xlabel("Future values")
plt.ylabel("Frequency out of "+str(trials))
plt.legend(loc="upper left")
plt.show()

sns.displot(values,bins=nbin,color="purple")
plt.show()
