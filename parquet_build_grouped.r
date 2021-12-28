library(arrow)
library(tidyverse)

dir.create("feather_grouped")
dir.create("feather_grouped/checkouts")
dir.create("feather_grouped/collection")

checks <- open_dataset("library/Checkouts_By_Title__Physical_Items_.csv",
    format = "csv", schema = schema(
        ID = string(),
        CheckoutYear = int64(),
        BibNumber = string(),
        ItemBarcode = string(),
        ItemType = string(),
        Collection = string(),
        CallNumber = string(),
        ItemTitle = string(),
        Subjects = string(),
        CheckoutDateTime = timestamp(unit = "s")),
    timestamp_parsers = "%m/%d/%Y %H:%M:%S %p"
    ) # https://time.is


collection <- open_dataset("library/Library_Collection_Inventory.csv",
    format = "csv", schema = schema(
        BibNum = string(),
        Title = string(),
        Author = string(),
        ISBN = string(),
        PublicationYear = string(),
        Publisher = string(),
        Subjects = string(),
        ItemType = string(),
        ItemCollection = string(),
        FloatingItem = string(),
        ItemLocation = string(),
        ReportDate = timestamp(unit = "s"),
        ItemCount = int64()),
    timestamp_parsers = "%m/%d/%Y"
    ) # https://time.is

collection %>%
    head() %>%
    collect()

collection %>%
  group_by(ItemType) %>%
  write_dataset("parquet_grouped/collection", format = "parquet")

checks %>%
    head() %>%
    collect()

# the library data has a few bad rows at the end
# not working
checks %>%
  group_by(ItemType) %>%
  write_dataset("parquet_grouped/checkouts", format = "parquet")
  
checksf <- open_dataset("feather_grouped/checkouts",
    format = "parquet")
##

cf <- open_dataset("feather_grouped/collection", format = "parquet")

