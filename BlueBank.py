#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:50:21 2022

@author: angieyou
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read json data 

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to data frame
loandata = pd.DataFrame(data)

#listing unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe particular columns
loandata['int.rate'].describe()
loandata['fico'].describe()

#debt to income ratios
loandata['dti'].describe()
#shows that most of them are in debt

#using exp() to get the annual income
income = np.exp(loandata['log.annual.inc'])
#adding annual income to loandata with income data
loandata['annualincome'] = income

#fico score 
#fico >= 300 and fico < 400 "Very Poor"
#fico >= 400 and fico < 600 "Poor"
#fico >= 600 and fico < 660 "Fair"
#fico >= 660 and fico < 780 "Good"
#fico >= 780 "Excellent"
    
fico = 700
        
if fico >= 300 and fico < 400:
        ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
        ficocat = 'Poor'
elif fico >= 600 and fico < 660:
        ficocat = 'Fair'
elif fico >= 660 and fico <780:
        ficocat = 'Good'
elif fico >= 780:
        ficocat = 'Excellent'
else: 
        ficocat = 'Unknown'
print(ficocat)

#declaring variable
 #creating length variable for length of loan data
length = len(loandata)
ficocat = []
for x in range(0,length): #starts with position 
    category = loandata['fico'][x]
        
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 400:
        cat = 'Poor'
    elif category >= 600 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 780:
        cat = 'Good'
    elif category >= 780:
        cat = 'Excellent'
    else: 
        cat = 'Unknown'    
          
    ficocat.append(cat)
        
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


#df.loc as conditional statement
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

#for interest rates, a new column is wanted
# if the rate is higher than 0.12 than it's high, if lower than low
# if higherthan 0.12 then create a new column

loandata.loc[loandata['int.rate']>0.12, 'int.rate.type']= 'High'
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type']= 'Low'

#number of loans or rows by fico category
#in the loandata, groupby fico category
#size counts the number of row
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green', width=0.1)
#matplotlib
#plot bar chart of catplot table
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='blue', width=0.4)
plt.show()
        
#scatter plot

xpoint = loandata['annualincome']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()
        
#write to csv
loandata.to_csv('Loan_Clean.csv', index = True)
        
        
        
        
        
        
        
        
        
        
        

    

    
    





