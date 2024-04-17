#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Load your dataset
df = pd.read_csv("C://Users//nandh//Downloads//HR Data.csv")
# 1) Removing unnecessary columns
unnecessary_columns = ['EmployeeCount', 'Over18', 'StandardHours'] # Specify the unnecessary columns

df = df.drop(columns=unnecessary_columns, errors='ignore')
# 2) Renaming columns
new_column_names = {
 'Age': 'EmployeeAge',
 'Attrition': 'AttritionStatus',
 'BusinessTravel': 'TravelType',
 'DailyRate': 'DailyRateUSD',
 'Department': 'DeptName',
 'DistanceFromHome': 'DistanceFromHomeKM',
 'Education': 'EducationLevel',
 'EducationField': 'FieldOfStudy',
 'EmployeeNumber': 'EmployeeID',
 'EnvironmentSatisfaction': 'EnvSatisfaction',
 'Gender': 'Gender',
 'HourlyRate': 'HourlyRateUSD',
 'JobInvolvement': 'JobInvolvementLevel',
 'JobLevel': 'JobLevel',
 'JobRole': 'JobTitle',
 'JobSatisfaction': 'JobSatisfaction',
 'MaritalStatus': 'MaritalStatus', # Include this if needed
 'MonthlyIncome': 'MonthlyIncomeUSD',
 'MonthlyRate': 'MonthlyRateUSD',
 'NumCompaniesWorked': 'NumCompaniesWorked',
 'OverTime': 'OverTime',
 'PercentSalaryHike': 'SalaryHikePercent',
 'PerformanceRating': 'PerformanceRating',
 'RelationshipSatisfaction': 'RelationshipSatisfaction',
 'StockOptionLevel': 'StockOptionLevel',
 'TotalWorkingYears': 'TotalWorkingYears',
 'TrainingTimesLastYear': 'TrainingTimesLastYear',
 'WorkLifeBalance': 'WorkLifeBalance',
 'YearsAtCompany': 'YearsAtCompany',
 'YearsInCurrentRole': 'YearsInCurrentRole',
 'YearsSinceLastPromotion': 'YearsSinceLastPromotion',
 'YearsWithCurrManager': 'YearsWithCurrManager'
}
df = df.rename(columns=new_column_names)
# 3) Eliminating redundant entries
df = df.drop_duplicates()
# 5) Eliminating NaN values
df = df.dropna()
# 6) Saving the cleaned dataset to a new CSV file
df.to_csv(r"C:\Users\nandh\OneDrive\Desktop\cleaned data.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:








# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:







# In[ ]:




