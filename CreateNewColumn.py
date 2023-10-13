import pandas as pd
def createBonusColumn(employees:pd.DataFrame)->pd.DataFrame:
    employees['bonus']=employees['salary']*2
    return employees
  #time complexity: 391 ms
  #space complexity: 59.36 MB
