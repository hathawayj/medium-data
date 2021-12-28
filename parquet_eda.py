
# %%
#import sys
#!{sys.executable} -m pip install duckdb pyarrow

# Need pyarrow > 6.0.0
# import sys
# !{sys.executable} -m pip install --upgrade pyarrow

import sys
!{sys.executable} -m pip install --upgrade duckdb
# %% 
import pandas as pd
import numpy as np
import duckdb

import pyarrow.dataset as ds
import pyarrow.parquet as pq

# %%
checks = pq.read_table('parquet/checkouts')
collection = pq.read_table('parquet/collection')
# %%
print(checks.num_rows)
checks.slice(length=10).to_pandas()


# %%
checks.filter(('CheckoutYear', '=', '2014'))


# %%
# We transform the dataset DuckDB relation
ddb = duckdb.arrow(checks)
# %%
# https://duckdb.org/docs/sql/aggregates
(ddb
    .filter("CheckoutYear == 2014")
    .aggregate("ItemType, count(*) as count, min(CheckoutDateTime) as date, last(CheckoutDateTime) as lastdate, first(CheckoutDateTime) as firstdate", "ItemType")
    .arrow()
    .to_pandas())
# %%
# Reads Parquet File to an Arrow Table
arrow_table = pq.read_table('integers.parquet')

# Gets Database Connection
con = duckdb.connect()

(con.execute('''
        SELECT SUM(data)
        FROM arrow_table
        WHERE data > 50
    ''')
    .fetch_arrow_table()
    .to_pandas())

# %%
