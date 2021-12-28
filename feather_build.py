# %%
# not working yet.
import pandas as pd
import numpy as np
import os

# %%
os.makedirs("feather/collection")
os.makedirs("feather/checkouts")

# %%
# column types
# both say that BibNum is int but I used str
# https://data.seattle.gov/Community/Library-Collection-Inventory/6vkj-f5xf
collection_cols = {
    'BibNum': str,
    'Title': str,
    'Author': str,
    'ISBN': str,
    'PublicationYear': str,
    'Publisher': str,
    'Subjects': str,
    'ItemType': str,
    'ItemCollection': str,
    'FloatingItem': str,
    'ItemLocation': str,
    'ReportDate': str,
    'ItemCount': int
}

# https://data.seattle.gov/Community/Checkouts-By-Title-Physical-Items-/5src-czff
checkouts_cols = {
    'ID': str,
    'CheckoutYear': str,
    'BibNumber': str,
    'ItemBarcode': str,
    'ItemType': str,
    'Collection': str,
    'CallNumber': str,
    'ItemTitle': str,
    'Subjects': str,
    'CheckoutDateTime': str,
}


# %%
# collection
chunksize = 750000 # how many rows to read/write at a time.
count = 0

for df in pd.read_csv(
        'library/Library_Collection_Inventory.csv', 
        chunksize=chunksize, dtype=collection_cols,
        parse_dates=['ReportDate'],
        iterator=True):
    count += 1
    df.reset_index().to_feather('feather/collection/file_{}.feather'.format(count),
        compression = "lz4")
# %%
# checkouts
chunksize = 2000000 # how many rows to read/write at a time.
count = 0

for df in pd.read_csv(
        'library/Checkouts_By_Title__Physical_Items_.csv', 
        chunksize=chunksize, dtype=checkouts_cols,
        parse_dates=['CheckoutDateTime'],
        iterator=True):
    count += 1
    df.reset_index().to_feather('feather/checkouts/file_{}.feather'.format(count),
        compression = "lz4")

# %%
