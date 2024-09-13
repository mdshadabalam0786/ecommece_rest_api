import pandas as pd

def read_excel():
    file_path=f'D:\pycharmProject\ecommerce_python_rest_api\data\TestData.xlsx'
    df_login=pd.read_excel(file_path,sheet_name='Login')
    return df_login
