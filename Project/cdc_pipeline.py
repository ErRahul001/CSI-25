from pyspark.sql import SparkSession
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

spark = SparkSession.builder.appName("CDC_Pipeline").getOrCreate()
jdbcUrl = dbutils.widgets.get("sourceJdbc")
jdbcUser = dbutils.widgets.get("Rahul")
jdbcPass = dbutils.widgets.get("qt52tq334cs")
cdcTables = ["Customer", "Product", "Orders", "Inventory"]

for tbl in cdcTables:
    df = spark.read.format("jdbc") \
        .option("url", jdbcUrl) \
        .option("dbtable", f"(SELECT * FROM cdc.fn_cdc_get_all_changes_dbo_{tbl}(sys.fn_cdc_get_min_lsn('{tbl}'), sys.fn_cdc_get_max_lsn(), 'all')) AS cdc_{tbl}") \
        .option("user", jdbcUser) \
        .option("password", jdbcPass) \
        .load()
    df.createOrReplaceTempView(f"cdc_{tbl}")
    deltaPath = f"/mnt/delta/{tbl}"
    spark.sql(f"""
        MERGE INTO delta.`{deltaPath}` AS target
        USING (SELECT * FROM cdc_{tbl}) AS source
        ON target.{tbl[:-1]}ID = source.{tbl[:-1]}ID
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
    """)

ts = datetime.now().strftime("%Y%m%d_%H%M")
out_path = f"/mnt/processed/{ts}"
for tbl in cdcTables:
    spark.table(tbl).coalesce(1).write.mode("overwrite").option("header", "true").csv(f"{out_path}/{tbl}")

sender = "rahulbeingrahul@gmail.com"
receiver = "milansaxena2001@gamil.com"
body = f"CDC pipeline completed successfully at {ts}. Output path: {out_path}"

msg = MIMEMultipart()
msg["Subject"] = f"CDC Success {ts}"
msg["From"] = sender
msg["To"] = receiver
msg.attach(MIMEText(body, "plain"))

context = ssl.create_default_context()
with smtplib.SMTP("smtp", 587) as server:
    server.starttls(context=context)
    server.login("rahul", "34twgqn53")
    server.sendmail(sender, receiver, msg.as_string())
