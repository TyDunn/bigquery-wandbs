# BigQuery + Weights & Biases

0. You need a BigQuery database with your [Spotify archive](https://www.spotify.com/us/account/privacy/)

1. Create a virtual environment
```
python3 -m venv env
```

2. Activate virtual environment
```
source env/bin/activate
```

3. Install Weights & Biases + Google BigQuery library
```
pip3 install wandb 'google-cloud-bigquery[bqstorage,pandas]'
```

4. [Set up authentication for BigQuery](https://cloud.google.com/docs/authentication/getting-started)

5. Copy your JSON credentials here
```
vim secrets.json
```

6. Log into Weights & Biases
```
wandb login
```

7. Run your application
```
python3 bigquery-wandbs.py
```