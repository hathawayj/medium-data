# %%
# import sys
# !{sys.executable} -m pip install duckdb
# %%
import pandas as pd 
import numpy as np
import sqlite3
import duckdb 

# %%
sqlite_file = 'lahmansbaseballdb.sqlite'
connLite = sqlite3.connect(sqlite_file)

# %%
# See the tables in the database
table = pd.read_sql_query(
    "SELECT * FROM sqlite_master WHERE type='table'",
    connLite)
print(table.filter(['name']))
print('\n\n')
# 8 is collegeplaying
print(table.sql[8])

# %%
# con = duckdb.connect(database=':memory:')

connDuck = duckdb.connect(database='lahmansbaseballdb.db', read_only=False)

# %%
batpost = pd.read_sql_query("SELECT * FROM battingpost", connLite)

connDuck.register('battingpost_view', batpost)
connDuck.execute('CREATE TABLE battingpost AS SELECT * FROM battingpost_view')
# https://github.com/duckdb/duckdb/issues/302
# %%
connDuck.close()
# %%
