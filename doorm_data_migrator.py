import dorm as dm
import dogui.dogui_core as dg
import pickle
import dorm_pandas_framework as dpf



db1 = dm.db("config1.ini")

db2 = dm.Mysqldb("config2.ini")

gui1=dg.GUI()

list_of_table_names=['companies']
dorm_tables=dpf.init_dorm_tables(db1,list_of_table_names)
dfs=dpf.init_dataframes_from_tables(db1,dorm_tables,list_of_table_names)
print(dfs)


gui1.build_gui()