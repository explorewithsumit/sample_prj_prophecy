from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from transaction_pipeline.config.ConfigStore import *
from transaction_pipeline.functions import *

def transfromation(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.withColumnRenamed("lm_offer_id", "offer_id")
    df2 = df1.withColumnRenamed("lm_transaction_id", "transaction_id")

    return df2.withColumnRenamed("transactionjournal_name", "journal_name")
