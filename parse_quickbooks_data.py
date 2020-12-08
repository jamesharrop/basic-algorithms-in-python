# Reads data from QuickBooks Excel output, and combines two detail profit and loss files (from two time periods) into one 
# file which keeps the detail from each time period but also shows the comparision between the two periods

import numpy as np
import pandas as pd

def read_db_from_file(filename):
    # Read in the data from Excel and drop unusued columns
    df = pd.read_excel(filename)
    del df['Unnamed: 6']
    df = df.drop([0,1,2,3,4])
    return df

def parse_QB_data(filename):
    # df1 will be our output dataframe
    df1 = pd.DataFrame(columns=['Category','Date','Memo', 'Amount'])

    lastdescr = 'start'
    newheading = False
    descr = ""

    for index, row in df.iterrows():
        descr = row["Business name"]
        date1 = row['Unnamed: 1']
        memo1 = row['Unnamed: 3']
        memo2 = row['Unnamed: 4']
        amount = row['Unnamed: 5']
        if np.isnan(amount):
            lastdescr = descr
        if isinstance(descr, float):
            if np.isnan(descr):

                # This code is to combine the memo1 and memo2, removing NaNs (equivalent to blank cells in the original files):
                concat_memo = True
                if isinstance(memo1, float):
                    if np.isnan(memo1):
                        memo = str(memo2)
                        concat_memo = False
                if isinstance(memo2, float):
                    if np.isnan(memo2):
                        memo = str(memo1)
                        concat_memo = False
                if isinstance(memo1, float) and isinstance(memo2, float):
                    if np.isnan(memo1) and np.isnan(memo2):
                        memo = ""
                        concat_memo = False
                if concat_memo:
                    memo = str(memo1) + ", " + str(memo2)

                df1 = df1.append({"Category": lastdescr, "Date":  date1, "Memo": memo, "Amount": amount}, ignore_index=True)
                
    df1['Date'] =  pd.to_datetime(df1['Date'])
    return df1


def combine_year_data(df2019, df2020):
    dfout = pd.DataFrame(columns=['Category', 'Date', 'Memo', 'Amount', 'Total','Difference','Difference_Percent'])
    lastcategory = "start"
    total = 0

    for index, row in df2019.iterrows():
        category = row["Category"]
        date = row['Date']
        memo = row['Memo']
        amount = row['Amount']

        if category != lastcategory: # We found a new category
            # Write out a subtotal
            dfout = dfout.append({"Memo": "A:", "Total": total}, ignore_index=True)

            # Find the next year's entries for that category
            total2 = 0
            for index2, row2 in df2020.iterrows():
                # This simplistic approach is really slow (? O(n^2)) but works fine for this use case 
                # which is just a small number of transactions
                category2 = row2["Category"]
                date2 = row2['Date']
                memo2 = row2['Memo']
                amount2 = row2['Amount']
                if category2 == lastcategory:
                    dfout = dfout.append(row2)
                    total2 += amount2

            # Write out a subtotal
            dfout = dfout.append({"Memo": "B:", "Total": total2}, ignore_index=True)

            if total == 0: # Don't calculate percentage if total = 0 as that will throw an error
                dfout = dfout.append({"Difference": total2-total}, ignore_index=True)
            else:
                dfout = dfout.append({"Difference": total2-total, "Difference_Percent": (total2-total)/total}, ignore_index=True)
            
            dfout = dfout.append({"Category": ""}, ignore_index=True)
            total = 0

        dfout = dfout.append({"Category": category, "Date":  date, "Memo": memo, "Amount": amount}, ignore_index=True)

        lastcategory = category
        total += amount
        
    return dfout

df = read_db_from_file(r'2019.xlsx')
df2019 = parse_QB_data(df)

df = read_db_from_file(r'2020.xlsx')
df2020 = parse_QB_data(df)

dfout = combine_year_data(df2019, df2020)

dfout.to_excel("out.xlsx", index=False)
