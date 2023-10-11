import pandas as pd
def selectFirstRows(employees:pd.DataFrame)->pd.DataFrame:
    return employees.head(3)
  #time complexity: 514 ms
  #space complexity: 58.51 MB
