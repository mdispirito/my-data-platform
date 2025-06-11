# My Data Platform
A data platform built with modern data engineering tools, just for fun.

# Usage
The application is completely containerized and split into services, as outlined in `compose.yaml`.

To start up the application containers:
```
docker-compose up
```

Then you can visit the app at:
```
localhost
```

To fetch some simple dummy data, vist:
```
localhost/nba-data
```
# Project status
There isn't much here yet, as I'm just doing some general setup.

To start with, I'm fetching some simple NBA data to begin playing with. I'll probably add/join other datasets in the future.

I'm using localstack to write it to a local S3 bucket for now. In the future I'll deploy to AWS using Terraform and create a persistent version of the platform.

# Rough project plan
This is a really rough outline of what I'm planning on doing. It'll almost definitely change over time.

Sample data collection
- [x] Set up nba_api and start pulling some data and writing to the console
- [ ] Set up a localstack S3 environment with Docker

Ingestion
- [ ] Hook the data ingestion up to the local s3 bucket
- [ ] Write the data to S3 using Iceberg table format
 
Infrastructure
- [ ] Create physical S3 buckets and other infra with Terraform
- [ ] Deploy to AWS

Transformations (details tbd)
- [ ] Write some transformations with SQL/DBT
- [ ] Write some transformations with PySpark

Orchestration
- [ ] Set up airflow to schedule some of the ingestion and transformation steps

Data Quality and Testing
- [ ] Set up a data quality check (AWS Glue?)
- [ ] Set up unit tests

Analytics Layer
- [ ] Set up a dashboard and general insights layer

Other
- [ ] Experiment with time travel using Iceberg tables
