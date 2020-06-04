import dorm as dm
import dogui.dogui_core as dg
import pickle
import dorm_pandas_framework as dpf
import pandas as pd
db1 = dm.db("config-shipvio.ini")

ds_free_carriers_table=dm.Table.init_all_columns(db1,"ds_free_carriers")


rows=ds_free_carriers_table.select("SELECT top(10) * FROM dbo.ds_free_carriers")

ds_free_carriers_df=pd.DataFrame(rows,columns=ds_free_carriers_table.columns)
ds_free_carriers_df.drop(["id"],axis=1,inplace=True)

db1.close_connection()

print(ds_free_carriers_df.columns)
db2 = dm.Mysqldb("config-mysql-hot-mode.ini")


ds_free_demands_table_target=dm.Table.init_all_columns(db2,"ds_free_carriers")

print(ds_free_demands_table_target.columns)

ds_free_demands_table_target.insert_from_df(ds_free_carriers_df)




db2.close_connection()


def check_tables(dfs):
    pass

def insert_data(dfs,target_db):
    pass

def insert_data_to_db(dfs,target_db):
    check_tables(dfs)
    insert_data(dfs,target_db)
    
    
    
#gui1=dg.GUI()

#gui1.build_gui()