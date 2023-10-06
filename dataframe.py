import pandas as pd
def createDataframe(student_data: List[List[int]])-> pd.DataFrame:
    column_names=["student_id","age"]
    result_dataframe=pd.DataFrame(student_data,columns=column_names)
    return result_dataframe
  
#time complexity: 421 ms
#space complexity: 59.69 mb
