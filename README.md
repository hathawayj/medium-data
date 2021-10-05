# Handling _Medium_ Data 

> Explorations on handling data in Python and R

Pandas and R both struggle with _medium_ sized data. You may be asking what specifications differentiate small, medium, and big data. The lines are blurry as the size of the data increases and compute abilities improve. Here are my defintions.

- __Small:__ The data that comes [embeded in R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/00Index.html) or Python packages like [vega-datasets](https://vega.github.io/vega-datasets/). 
- __Medium:__ Any dataset that puts a stress on the users memory and compute constraints.
- __Big:__ Any data that requires compute, storage, and memory beyond that availabe to standard local compute capabilities. [This Mac Pro](https://www.theverge.com/circuitbreaker/2019/12/10/21003636/apple-mac-pro-price-most-expensive-processor-ram-gpu) is not standard yet.

The latest technology advances in data handling have blurred the lines between each of these groups. Python and R can handly many other file formats and have their own formats (`.rds` and `.pkl`) for storing data more efficiently and effectively.  When users ask for data or when many institutions share data the files are usually some type of text file (`.txt`, `.csv`, `.tsv`) or an Excel file. The most ubiquitus format is `.csv`.

## DUCKDB

## Parquet files

## Compression and Querying

## Parallelization

## Example CDC package

### R

### Python
