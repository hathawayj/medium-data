# %%
import pandas as pd
import numpy as np
import os

# %%
os.makedirs("feather/collection")
os.makedirs("feather/checkouts")
# %%
# collection
chunksize = 750000 # how many rows to read/write at a time.
count = 0

for df in pd.read_csv(
        'library/Library_Collection_Inventory.csv', 
        chunksize=chunksize, 
        iterator=True):
    count += 1
    df.reset_index().to_feather('parquet/collection/file_{}.feather'.format(count),
        compression = "lz4")
# %%
# checkouts
# %%
chunksize = 2000000 # how many rows to read/write at a time.
count = 0

for df in pd.read_csv(
        'library/Checkouts_By_Title__Physical_Items_.csv', 
        chunksize=chunksize, 
        iterator=True):
    count += 1
    df.reset_index().to_feather('parquet/checkouts/file_{}.feather'.format(count),
        compression = "lz4")

# %%
