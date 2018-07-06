#!/usr/bin/env python3

import re
import schemas


from pyspark import SparkContext
from pyspark.sql import Row, SQLContext

LOG_PATTERN  = '^(\S+) (\S+) (\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\S+) (\S+)'

def parse_line(line):
  match = re.search(LOG_PATTERN, line)

  if match:
    return Row(
        trace_token   = match.group(1),
        ip_address    = match.group(2),
        cn_header     = match.group(4),
        entity        = match.group(5),
        timestamp     = match.group(6),
        method        = match.group(7),
        endpoint      = match.group(8),
        protocol      = match.group(9),
        response_code = match.group(10),
        response_size = match.group(11))


def access_logs_to_parquet(log_path, log_output_path):
  sc = SparkContext()
  sqlContext = SQLContext(sc)

  rdd = sc.textFile(log_path).map(parse_line)
  df = sqlContext.createDataFrame(rdd, schemas.accesslog())
  df.write.parquet(log_output_path, mode='append')

def main(log_path="accesslog.log", log_output_path="accesslog.parquet"):
  access_logs_to_parquet(log_path, log_output_path)


if __name__ == "__main__":
  main()