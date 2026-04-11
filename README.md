# Real-Time Weather Data Pipeline using Airflow, dbt and Docker

## Overview

An end-to-end data engineering pipeline that extracts weather data from the Weatherstack API, loads it into PostgreSQL, transforms it using dbt, and serves analytics-ready data for reporting.

The pipeline is orchestrated using Apache Airflow and fully containerized with Docker.

---

## Tech Stack

* Python
* PostgreSQL
* Apache Airflow
* dbt
* Docker & Docker Compose
* Apache Superset

---

## Pipeline Architecture

```
Weatherstack API
      ↓
Python Scripts (Extract & Load)
      ↓
PostgreSQL (Raw Layer)
      ↓
dbt (Staging → Mart)
      ↓
Superset Dashboard
```

---

## Pipeline Flow

* Extract weather data from API using Python
* Load raw data into PostgreSQL
* Transform data using dbt (staging and mart layers)
* Orchestrate workflows using Airflow DAGs
* Visualize insights in Superset

---

## Project Structure

```
.
├── scripts/
│   ├── api_request.py
│   └── insert_records.py
│
├── airflow/
│   └── dags/
│       └── orchestrator.py
│
├── dbt/
│   └── my_project/
│       └── models/
│           ├── source/
│           ├── staging/
│           │   └── stg_weather_data.sql
│           └── mart/
│               ├── daily_average.sql
│               └── weather_report.sql
```

---

## Outputs

* Weather report
* Daily average metrics
* Real-time dashboard

---

## How to Run

```bash
git clone https://github.com/omaarelsherif/Real-Time-Weather-Data-Pipeline-using-Airflow-dbt-Docker.git
cd Real-Time-Weather-Data-Pipeline-using-Airflow-dbt-Docker
docker-compose up -d
```

Access:

* Airflow: http://localhost:8000
* Superset: http://localhost:8088

---

## Notes

* Add your Weatherstack API key before running
* Ensure Docker is installed
