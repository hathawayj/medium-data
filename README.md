# Handling _Medium_ Data 

> Explorations on handling data in Python and R

Pandas and R both struggle with _medium_ sized data. You may be asking what specifications differentiate small, medium, and big data. The lines are blurry as the size of the data increases and compute abilities improve. Here are my defintions.

- __Small:__ The data that comes [embeded in R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html) or Python packages like [vega-datasets](https://vega.github.io/vega-datasets/). 
- __Medium:__ Any dataset that puts a stress on the users memory and compute constraints.
- __Big:__ Any data that requires compute, storage, and memory beyond that availabe to standard local compute capabilities. [This Mac Pro](https://www.theverge.com/circuitbreaker/2019/12/10/21003636/apple-mac-pro-price-most-expensive-processor-ram-gpu) is not standard yet.

The latest technology advances in data handling have blurred the lines between each of these groups. Python and R can handle many other file formats and have their own formats (`.rds` and `.pkl`) for storing data more efficiently and effectively.  When users ask for data or when many institutions share data the files are usually some type of text file (`.txt`, `.csv`, `.tsv`) or an Excel file. The most ubiquitous format is `.csv`.

## Parquet files

> Apache Parquet is designed for efficient as well as performant flat columnar storage format of data compared to row based files like CSV or TSV files. [databricks](https://databricks.com/glossary/what-is-parquet)

After using the [parquet_build.py](parquet_build.py) you will have a [parquet](parquet) folder which contains the parquet data from the 22.34 Gb `Library_Collection_Inventory.csv` in the [collection](parquet/collection) folder.  Notice that the data is stored in chunks such that each file is smaller than the 100 Mb limit that Github enforces.  Due to the efficient storage and compression the 22.34 Gb `.csv` format of the data is reduced to 5.66 Gb. In the [checkouts](parquet/checkouts) folder the data from 4.89 Gb `Checkouts_By_Title__Physical_Items_.csv` file will only require 0.97 Gb of space.

Github does ask that repositories not store more than 1 Gb of data with stronger warning if it is over 5 Gb so we have not included these Parquet files here. It is amazing that we went from over 25 Gb of data in the `.csv` format to about 6 Gb of data in the `.parquet` format.  In addition, the `.parquet` format contains the data type and datetime information as saved.  As we know, `.csv` files do not store that information.

Finally, this new format allows Python and R to wrangle data that is larger than
## Arrow files

https://wesmckinney.com/blog/arrow-columnar-abadi/
## DUCKDB


## Compression and Querying


## Parallelization

## Example CDC package

### R

### Python
