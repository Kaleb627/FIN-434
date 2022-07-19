import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import easygui
from easygui import *

#user input prompt
msg="Please enter the data"
title="valuation"
fieldNames=["Stock Price xx.xx","Interest rate .xx","Percent on Margin .xx",
            "Commission Rate .xx","Maintenance Margin .xx"]
fieldValues=[]
fieldValues=multenterbox(msg,title,fieldNames)

#blank input check
while 1:
    if fieldValues == None: break
    errmsg=""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() =="":
            errmsg=errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break
    fieldValues = multenterbox(errmsg, title,fieldNames,fieldValues)

#Assigning entered values to variable in needed format
p = float(fieldValues[0])
r = float(fieldValues[1])
b = float(fieldValues[2])
i = float(fieldValues[3])
x = float(fieldValues[4])

##test inputs
#p = 28
#r = 0.02
#b = 0.5
#i = 0.01
#x = 0.3

#Format checks/fixes
if ((p or r or b or i or x)<0):
    msgbox("Number cannot be negative")
    exit
if r > 1:
    r /= 100
if b > 1:
    b /= 100
if i > 1:
    i /= 100
if x > 1:
    x /= 100

#margin call
call=((p*b)*x)
msgbox("You will receive a mrgin call at stock price $" + str(call))

#array and other calc variables 
low = ((p * b) * (1 - x))
high = (p * 2)
num = int((high - low) + 1)
pr=np.arange(low,high,1)
profit=np.zeros(num)

#calculation loop
z=0
while z < num:
    profit[z] = (((pr[z])-((pr[z])*i)-(p)-((p)*i)-(((p)*b)*r))/(p))
    print(profit[z])
    z += 1

#charting
plt.plot(pr,profit)
plt.xlabel("Price")
plt.ylabel("Profit/Loss")
plt.title("Margin Payoff")
plt.show()