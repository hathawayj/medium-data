library(duckdb)
library(arrow)
library(dplyr)
# https://duckdb.org/2021/12/03/duck-arrow.html
# https://duckdb.org/docs/sql/aggregates
ds <- open_dataset("parquet/checkouts")

ds %>%
    head() %>%
    collect()

ds %>%
    filter(CheckoutYear == "2014") %>%
    to_duckdb() %>%
    group_by(ItemType) %>%
    summarise(
        Count = n(),
        date = min(CheckoutDateTime)) %>%
    collect() %>%
    data.frame()

ds %>%
    to_duckdb() %>%
    filter(CheckoutYear == "2015")

# https://ursalabs.org/arrow-r-nightly/articles/dataset.html
bucket <- "https://ursa-labs-taxi-data.s3.us-east-2.amazonaws.com"
for (year in 2018:2019) {
  if (year == 2019) {
    # We only have through June 2019 there
    months <- 1:6
  } else {
    months <- 1:12
  }
  for (month in sprintf("%02d", months)) {
    dir.create(file.path("nyc-taxi", year, month), recursive = TRUE)
    try(download.file(
      paste(bucket, year, month, "data.parquet", sep = "/"),
      file.path("nyc-taxi", year, month, "data.parquet"),
      mode = "wb"
    ), silent = TRUE)
  }
}
