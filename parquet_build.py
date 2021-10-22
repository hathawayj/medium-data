# %%
import pandas as pd
import numpy as np
import os

# %%
os.makedirs("parquet/collection")
os.makedirs("parquet/checkouts")

# %%
checkoutsDtypes = {
    'ID':str,
    'CheckoutYear':int,
    'BibNumber':int,
    'itemBarcode':str,
    'itemType':str,
    'Collection':str,
    'CallNumber':str,
    'itemTitle':str,
    'Subjects':str,
    'CheckoutDateTime':str
}
# %%
# collection
chunksize = 750000 # how many rows to read/write at a time.
count = 0

for df in pd.read_csv(
        'library/Library_Collection_Inventory.csv', 
        chunksize=chunksize, 
        iterator=True):
    count += 1
    df.reset_index().to_parquet('parquet/collection/file_{}.parquet'.format(count),
        compression = "brotli")
# %%
# checkouts
# https://data.seattle.gov/Community/Checkouts-by-Title/tmmm-ytt6
chunksize = 1750000 # how many rows to read/write at a time.
count = 0

for df in pd.read_csv(
        'library/Checkouts_By_Title__Physical_Items_.csv',
        chunksize = chunksize, 
        iterator=True,
        dtype=checkoutsDtypes,
        parse_dates = ['CheckoutDateTime']):
    count += 1
    df.reset_index().to_parquet('parquet/checkouts/file_{}.parquet'.format(count),
        compression = "brotli")

# %%
