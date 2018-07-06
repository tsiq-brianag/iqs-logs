from pyspark.sql.types import *

def accesslog():
  return StructType([
    StructField("trace_token", StringType(), True),
    StructField("ip_address", StringType(), True),
    StructField("cn_header", StringType(), True),
    StructField("entity", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("method", StringType(), True),
    StructField("endpoint", StringType(), True),
    StructField("protocol", StringType(), True),
    StructField("response_code", StringType(), True),
    StructField("response_size", StringType(), True)])
