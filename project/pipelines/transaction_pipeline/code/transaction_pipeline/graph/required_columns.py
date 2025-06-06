from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from transaction_pipeline.config.ConfigStore import *
from transaction_pipeline.functions import *

def required_columns(spark: SparkSession, rename_schema_columns: DataFrame) -> DataFrame:
    return rename_schema_columns.select(
        (monotonically_increasing_id() + lit(1)).alias("loyaltyTransactionID"), 
        col("activity_date"), 
        col("transaction_id"), 
        col("transaction_amount"), 
        col("expiry_date").alias("ledgerPointsExpiryTimestamp").alias("expiry_date"), 
        col("points").alias("ledgerPoints").alias("points"), 
        col("last_modified_date").alias("transactionTimestamp").alias("last_modified_date")
    )
