import pandas as pd
import os
def mer(username):
 module_dir = os.path.dirname(__file__)
 a=pd.read_csv(os.path.join(module_dir,f'csvfile/{username}.csv'))
 b=pd.read_csv(os.path.join(module_dir,f'csvfile/{username}_output.csv'))
 b= b.dropna(axis=1)
 merged = a.merge(b,on='m_id')
 merged.to_csv(os.path.join(module_dir,f'csvfile/{username}_final.csv'),index=False)
