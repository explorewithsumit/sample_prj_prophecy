from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from transaction_pipeline.config.ConfigStore import *
from transaction_pipeline.functions import *

def source_sample(spark: SparkSession) -> DataFrame:
    from prophecy.utils import synthetic_data_generator
    from pyspark.sql import functions as F
    import json

    return synthetic_data_generator\
        .FakeDataFrame(spark, 10000)\
        .addColumn(
          "activity_date",
          synthetic_data_generator.random_datetime(F.lit("2021-05-01 00:00:00"), F.lit("2025-05-01 00:00:00")),
          data_type = TimestampType(),
          nulls = 0
        )\
        .addColumn("lm_offer_id", synthetic_data_generator.random_uuid(), data_type = StringType(), nulls = 0)\
        .addColumn(
          "transaction_amount",
          synthetic_data_generator.random_float(F.lit(1.0), F.lit(10000.0), F.lit(2)),
          data_type = FloatType(),
          nulls = 0
        )\
        .addColumn("lm_transaction_id", synthetic_data_generator.random_uuid(), data_type = StringType(), nulls = 0)\
        .addColumn("transactionjournal_name", synthetic_data_generator.random_full_name(), data_type = StringType(), nulls = 0)\
        .addColumn("voucher_code", synthetic_data_generator.random_uuid(), data_type = StringType(), nulls = 0)\
        .addColumn("product_sku", synthetic_data_generator.random_uuid(), data_type = StringType(), nulls = 0)\
        .addColumn(
          "expiry_date",
          synthetic_data_generator.random_datetime(F.lit("2025-06-01 00:00:00"), F.lit("2027-06-01 00:00:00")),
          data_type = TimestampType(),
          nulls = 0
        )\
        .addColumn("points", synthetic_data_generator.random_int(F.lit(1), F.lit(5000)), data_type = IntegerType(), nulls = 0)\
        .addColumn("customer_id", synthetic_data_generator.random_uuid(), data_type = StringType(), nulls = 0)\
        .addColumn(
          "last_modified_date",
          synthetic_data_generator.random_datetime(F.lit("2022-01-01 00:00:00"), F.lit("2025-06-01 00:00:00")),
          data_type = TimestampType(),
          nulls = 0
        )\
        .addColumn("product_name", synthetic_data_generator.random_full_name(), data_type = StringType(), nulls = 0)\
        .build()
