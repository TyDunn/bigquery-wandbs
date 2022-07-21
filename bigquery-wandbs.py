from google.cloud import bigquery
import os
import wandb

# BigQuery

# set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="secrets.json"

# connect to BigQuery
bqclient = bigquery.Client()

# SQL query to grab 1000 streaming history entries
query = "SELECT * FROM zinc-mantra-353207.demo_18b0_spotify.streaming_history LIMIT 1000"

# query and convert to dataframe
dataframe = (
    bqclient.query(query)
    .result()
    .to_dataframe(create_bqstorage_client=True)
)

# to show that it worked in command line
print(dataframe.head())

# Weights & Biases

# intialize wandb project
wandb.init(project="bigquery-wandbs")

# add the data to wandb for visualization
wandb.log({"table": dataframe})