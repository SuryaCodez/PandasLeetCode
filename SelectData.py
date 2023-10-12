import pandas as pd
def selectData(students:pd.DataFrame)->pd.DataFrame:
    return students.loc[students["student_id"]==101,["name","age"]]
  #time complexity: 575 ms
  #space complexity: 61.19 MB
