import pandas as pd


def chk_duplicates(excel_file,address):
    dfs = pd.read_excel(excel_file, sheet_name=None)
    for sheetname,df in dfs.items():
        if address in df['address'].tolist():
            return True
    return False

        
