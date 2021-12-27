## Building our `.parquet` files

After using the [parquet_build.py](parquet_build.py) you will have a [parquet](parquet) folder which contains the parquet data from the 22.34 Gb `Library_Collection_Inventory.csv` in the [collection](parquet/collection) folder.  Notice that the data is stored in chunks such that each file is smaller than the 100 Mb limit that Github enforces.  Due to the efficient storage and compression the 22.34 Gb `.csv` format of the data is reduced to 5.66 Gb. In the [checkouts](parquet/checkouts) folder the data from 4.89 Gb `Checkouts_By_Title__Physical_Items_.csv` file will only require 0.97 Gb of space.

Github does ask that repositories not store more than 1 Gb of data with stronger warning if it is over 5 Gb so we have not included these Parquet files here. It is amazing that we went from over 25 Gb of data in the `.csv` format to about 6 Gb of data in the `.parquet` format.  In addition, the `.parquet` format contains the data type and datetime information as saved.  As we know, `.csv` files do not store that information.

