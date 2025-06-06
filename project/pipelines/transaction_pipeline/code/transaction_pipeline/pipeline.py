from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from transaction_pipeline.config.ConfigStore import *
from transaction_pipeline.functions import *
from prophecy.utils import *
from transaction_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_source_sample = source_sample(spark)
    df_transfromation = transfromation(spark, df_source_sample)
    df_required_columns = required_columns(spark, df_transfromation)
    transaction_data(spark, df_required_columns)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("transaction_pipeline").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/transaction_pipeline")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/transaction_pipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()
