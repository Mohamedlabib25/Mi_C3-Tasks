# Timestamp Difference API (FastAPI + Docker Compose)

This application exposes a FastAPI-based REST API to compute the absolute time differences (in seconds) between pairs of timezone-aware timestamps. The app is containerized and runs with Docker Compose using **two instances** of the same service for demonstration.

## 🐳 Prerequisites

- Docker
- Docker Compose
- PowerShell (for testing via `Invoke-WebRequest` on Windows)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://your-repo-url.git
cd your-repo-folder


## Build the Docker Images

docker-compose build


##  Run the Services
docker-compose up


This will start two containers:

app-1 accessible at http://127.0.0.1:8001/compute-differences

app-2 accessible at http://127.0.0.1:8002/compute-differences



## test

(Invoke-WebRequest -Uri "http://127.0.0.1:8002/compute-differences"  -Method POST  -Headers @{"Content-Type"="text/plain"}  -Body "2`nSun 10 May 2015 13:54:36 -0700`nSun 10 May 2015 13:54:36 -0000`nSat 02 May 2015 19:54:36 +0530`nFri 01 May 2015 13:54:36 -0000").content


## output
{"id":"fca40ac6-b488-4d94-8b71-6d2bee306e31","result":["25200","88200"]}
