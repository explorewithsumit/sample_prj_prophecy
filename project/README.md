## Pipelines

### 1. **transaction_pipeline**
**Code Overview:**
The pipeline begins by establishing a Spark session and configuring necessary parameters, including parallelism and Hive support. It then initializes the pipeline by loading customer and order data into DataFrames. The data is processed through a series of transformations, culminating in a summary of total spending by each customer. The pipeline also incorporates metrics collection to monitor performance and ensure the integrity of the data processing.

---

## Datasets

1. **transaction_data**
Records of loyalty transactions, capturing details on points earned, transaction amounts, and expiry dates to enhance customer engagement strategies.

2. **source_sample**
Customer transaction records detailing offers, voucher usage, and points earned, supporting insights into customer engagement and promotional effectiveness.