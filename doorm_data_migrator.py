import dorm as dm
import dogui.dogui_core as dg
import pickle
import dorm_pandas_framework as dpf



db1 = dm.db("config1.ini")

db2 = dm.Mysqldb("config2.ini")

list_of_table_names=['companies']
dorm_tables=dpf.init_dorm_tables(db1,list_of_table_names)
dfs=dpf.init_dataframes_from_tables(db1,dorm_tables,list_of_table_names)
print(dfs)


def check_tables(dfs):
    pass

def insert_data(dfs,target_db):
    pass

def insert_data_to_db(dfs,target_db):
    check_tables(dfs)
    insert_data(dfs,target_db)
    
    

#gui1=dg.GUI()

#gui1.build_gui()