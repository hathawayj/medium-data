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

## DUCKDB


## Compression and Querying


## Parallelization

## Example CDC package

### R

### Python
