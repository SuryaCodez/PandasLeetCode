import pandas as pd
def dropDuplicateEmails(customers:pd.DataFrame)->pd.DataFrame:
    customers.drop_duplicates(subset='email',keep='first',inplace=True)
    return customers
#time complexity:456 ms
#space complexity:59.97 MB
