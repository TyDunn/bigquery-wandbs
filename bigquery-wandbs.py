from google.cloud import bigquery
import os
import wandb

# BigQuery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="secrets.json"

bqclient = bigquery.Client()

query = "SELECT * FROM zinc-mantra-353207.demo_18b0_spotify.streaming_history LIMIT 1000"

dataframe = (
    bqclient.query(query)
    .result()
    .to_dataframe(create_bqstorage_client=True)
)
print(dataframe.head())

# Weights & Biases

wandb.init(project="bigquery-wandbs")

wandb.log({"table": dataframe})