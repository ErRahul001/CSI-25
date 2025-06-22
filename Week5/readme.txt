Task 1  : Copy data from one database to another with event trigger
For this purpose I've built a pipeline that copies data from a blob storage to an SQL database based on event triggers with the help of Azure Data Factory.
Task 2  : Copy data from one database to another with schedule trigger
For this purpose I've built a pipeline that copies data from a blob storage to an SQL database based on schedule triggers with the help of Azure Data Factory.
It was possible with minor tweaking in the existing event based pipeline.
Task 3 : Copy an input file into multiple formats. 
Here the input csv file is being copied to target Parquet, Avro and csv file with event and schedule based triggers.
Task 4 : Copy all and selective tables from one database to another database.
Here lookup function is used to copy selective tables from one database to another.
