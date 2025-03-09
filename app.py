import pandas as pd
import datetime as dt
import os
from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output
from urllib.parse import quote as url_quote

class db:
    def __init__(self):
        self.transactions = transaction_init()
        self.cc = pd.read_csv(r'db\country_codes.csv',index_col=0)
        self.customers = pd.read_csv(r'db\customers.csv',index_col=0)
        self.prod_info = pd.read_csv(r'db\prod_cat_info.csv')

    def merge(self):
        pass


# read all files
@staticmethod
def transaction_init():
    transactions = pd.DataFrame()
    src = r'db\transactions'
    for filename in os.listdir(src):
        transactions = transactions._append(pd.read_csv(os.path.join(src,filename),index_col=0))
    #conert a date
    def convert_dates(x):
        try:
            return dt.datetime.strptime(x,'%d-%m-%Y')
        except:
            return dt.datetime.strptime(x,'%d/%m/%Y')

    transactions['tran_date'] = transactions['tran_date'].apply(lambda x: convert_dates(x))

    return transactions

# join a datebase with category of columns
def merge(self):
    df = self.transactions.join(self.prod_info.drop_duplicates(subset=['prod_cat_code'])
    .set_index('prod_cat_code')['prod_cat'],on='prod_cat_code',how='left')

    df = df.join(self.prod_info.drop_duplicates(subset=['prod_sub_cat_code'])
    .set_index('prod_sub_cat_code')['prod_subcat'],on='prod_subcat_code',how='left')

    df = df.join(self.customers.join(self.cc,on='country_code')
    .set_index('customer_Id'),on='cust_id')

    self.merged = df

df = db()
df.merge()


#  build a dashboard
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# build a layout
app.layout = html.Div([html.Div([dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sprzedaż globalna',value='tab-1'),
                            dcc.Tab(label='Produkty',value='tab-2')
                            ]),
                            html.Div(id='tabs-content')
                    ],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

if __name__ == '__main__':
    app.run_server(debug=True)

