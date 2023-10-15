import pandas as pd
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'], inplace=True)
    return students
#time complexity:526 ms
#space complexity:59.84 MB
