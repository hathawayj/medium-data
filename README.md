# Handling _Medium_ Data 

> Explorations on handling data in Python and R

Pandas and R both struggle with _medium_ sized data. You may be asking what specifications differentiate small, medium, and big data. The lines are blurry as the size of the data increases and compute abilities improve. Here are my defintions.

- __Small:__ The data that comes [embeded in R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html) or Python packages like [vega-datasets](https://vega.github.io/vega-datasets/). 
- __Medium:__ Any dataset that puts a stress on the users memory and compute constraints.
- __Big:__ Any data that requires compute, storage, and memory beyond that availabe to standard local compute capabilities. [This Mac Pro](https://www.theverge.com/circuitbreaker/2019/12/10/21003636/apple-mac-pro-price-most-expensive-processor-ram-gpu) is not standard yet.

The latest technology advances in data handling have blurred the lines between each of these groups. Python and R can handle many other file formats and have their own formats (`.rds` and `.pkl`) for storing data more efficiently and effectively.  When users ask for data or when many institutions share data the files are usually some type of text file (`.txt`, `.csv`, `.tsv`) or an Excel file. The most ubiquitous format is `.csv`.

## Apache Arrow

> Apache Arrow is a software development platform for building high performance applications that process and transport large data sets. A critical component of Apache Arrow is its in-memory columnar format, a standardized, language-agnostic specification for representing structured, table-like datasets in-memory. 
> [Apache Arrow](https://arrow.apache.org/overview/)

You can read much more about the in-memory Arrow format under their [format documentation](https://arrow.apache.org/docs/format/Columnar.html). The key aspect of Arrow is 'in-memory' storage.  Once we save those files for latter use they are stored outside of memory.  For data scientists, the two most used formats are `.parquet` and `.feather`.

These new file formats allows Python and R to wrangle data that is larger than memory in a performant manner. The Python package [pyarrow](https://arrow.apache.org/docs/python/index.html) and R [arrow](https://arrow.apache.org/docs/r/) packages provide access to each of these file formats.

## Parquet files

> Apache Parquet is designed for efficient as well as performant flat columnar storage format of data compared to row based files like CSV or TSV files. [databricks](https://databricks.com/glossary/what-is-parquet)

Apache also maintains the `.parquet` format.  You can read more details about the development on their [webpage](https://parquet.apache.org/documentation/latest/). The `.parquet` format performs well with Arrow in memory objects as it is a columnar format as well.  

## Feather files

Wes McKinney and Hadley Wickham developed the Feather file format around 2016 to facilitate data collaboration between Python and R. A short time after Wes incorporated the Feather format into the Apacha Arrow project ([reference](https://wesmckinney.com/blog/feather-arrow-future/)). In 2020, the Apacha Arrow team standardized a more robust Feather format called Feather V2 that provides a rich format that can compete with `.parquet` on most fronts ([reference](https://ursalabs.org/blog/2020-feather-v2/). In comparing `.parquet` to `.feather`, Wes MicKinney's [April 23, 2020 blog post](https://ursalabs.org/blog/2020-feather-v2/) concludes;

> Parquet format has become one of the “gold standard” binary file formats for data warehousing. We highly recommend it as a portable format that can be used in many different data processing systems. It also generally (but not always) produces very small files.
> Feather V2 has some attributes that can make it attractive:
> 
> 1. Accessible by any Arrow implementation. R and Python use the Arrow C++ library internally, which is a well-supported reference implementation.
> 2. Generally faster read and write performance when used with solid state drives, due to simpler compression scheme. When read over the network, we expect Parquet will outperform.
> 3. Internal structure supports random access and slicing from the middle. This also means that you can read a large file chunk by chunk without having to pull the whole thing into memory.
> 4. Complete support for all Arrow data types. Parquet has a smaller type system and while most of Arrow can be stored in Parquet, there are some things that cannot (like unions). Support for reading nested Parquet data is not fully implemented yet, but should be in 2020 (see ARROW-1644).

## I/O and Wrangling in R and Python

These file formats and in-memory constructs are only helpful for medium data projects if we can leverage them using the tools on our local machines - R, Python, and SQL. Arrow is making progress on the available wrangling functions available before pulling the entire dataset into memory. Our goal is to leverage the Arrow methods before we run `.to_pandas()` in Python and `collect()` in R. 

### `pyarrow.parquet.read_table()` 

The `pyarrow.parquet.read_table()` returns a [`pyarrow.Table`](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table) which facilitates data wrangling methods similar to [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

Some of the most pertinent methods follow.

- `.slice()`: Much like `head()` or `limit()`.
- `.add_column()`: Add column to Table at position
- `.append_column()`: Append column at end of columns.
- `.remove_column()`: Create new Table with the indicated column removed.
- `.set_column()`: Replace column in Table at position.
- `.select()`: Select columns of the Table.
- `.drop()`: Drop one or more columns and return a new table.
- `.filter()`: Select records from a Table.
- `.to_pandas()`: Converts to a pandas DataFrame.

### dplyr

[Arrow's documentation on leveraging dplyr](https://arrow.apache.org/docs/r/articles/dataset.html). Importantly they highlight which dplyr verbs work using Arrow.

> Arrow supports the dplyr verbs `mutate()`, `transmute()`, `select()`, `rename()`, `relocate()`, `filter()`, and `arrange()`.
> Aggregation is not yet supported, so before you call `summarise()` or other verbs with aggregate functions, use `collect()` to pull the selected subset of the data into an in-memory R data frame.

They alsow help us understand how to handle a single file that is too big for memory.

> For example, you have a single CSV file that is too big to read into memory. You could pass the file path to `open_dataset()`, use `group_by()` to partition the Dataset into manageable chunks, then use `write_dataset()` to write each chunk to a separate Parquet file—all without needing to read the full CSV file into R.

The [arrow package] has [`open_dataset()`](https://arrow.apache.org/docs/r/reference/open_dataset.html) and varied [`read_` functions](https://arrow.apache.org/docs/r/reference/index.html) for importing data. We want to leverage the options that keep the data in the [Arrow Table format](https://arrow.apache.org/docs/r/reference/Table.html).

### DUCKDB

[DuckDB](https://duckdb.org/) is an in-process SQL OLAP database management system.

DuckDB provides and R package, SQL interface, and Python package that allows us to directly interact with the `.parquet` files.  Their [overview post in December 2021](https://duckdb.org/2021/12/03/duck-arrow.html) provides clean examples.

#### R

We can leverage additional dplyr manipulations beyond what is available in the arrow R package. Notice in the following example that `mutate()` and `summarise()` are available in `group_by()`.

```r
library(duckdb)
library(arrow)
library(dplyr)

# Open dataset using year,month folder partition
ds <- arrow::open_dataset("nyc-taxi", partitioning = c("year", "month"))

ds %>%
  # Look only at 2015 on, where the number of passenger is positive, the trip distance is
  # greater than a quarter mile, and where the fare amount is positive
  filter(year > 2014 & passenger_count > 0 & trip_distance > 0.25 & fare_amount > 0) %>%
  # Pass off to DuckDB
  to_duckdb() %>%
  group_by(passenger_count) %>%
  mutate(tip_pct = tip_amount / fare_amount) %>%
  summarise(
    fare_amount = mean(fare_amount, na.rm = TRUE),
    tip_amount = mean(tip_amount, na.rm = TRUE),
    tip_pct = mean(tip_pct, na.rm = TRUE)
  ) %>%
  arrange(passenger_count) %>%
  collect()

```

#### Python

DuckDB has a [short script](https://github.com/duckdb/duckdb/blob/master/examples/python/duckdb-python.py) that provides example for the Python methods.

We can make direct SQL queries using the `.execute()` method.

```python
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
```

You can review the full [SQL Functionality](https://duckdb.org/docs/sql/introduction) of DuckDB.

## Example CDC package

### R

### Python

## Resources

- https://blog.datasyndrome.com/python-and-parquet-performance-e71da65269ce
- https://arrow.apache.org/docs/python/generated/pyarrow.Table.html
- https://arrow.apache.org/cookbook/py/index.html
- https://arrow.apache.org/cookbook/r/index.html