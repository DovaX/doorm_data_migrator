import dorm as dm
import dogui as dg



db1 = dm.db("config1.ini")

db2 = dm.Mysqldb("config2.ini")

gui1=dg.GUI()


gui1.build_gui()