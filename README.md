# Mi_C3-Tasks
# FastAPI Time Difference API

This is a FastAPI application that calculates the absolute time differences between timestamp pairs provided in plain text input. 
The application processes timestamp pairs, computes the differences in seconds, and returns the results in JSON format.

## Requirements

- Python 3.11+
- Install the required Python packages:


pip install fastapi uvicorn


## Start the FastAPI Application:

Use uvicorn to run the FastAPI app locally:

uvicorn main:app --reload


## To test the API,
you can use the following PowerShell command to send a POST request to the /compute-differences endpoint with the timestamp pairs in the request body.

Open PowerShell and run the following script:

> $body = "2`nSun 10 May 2015 13:54:36 -0700`nSun 10 May 2015 13:54:36 -0000`nSat 02 May 2015 19:54:36 +0530`nFri 01 May 2026 13:54:36 -0000"

> (Invoke-WebRequest -Uri 'http://127.0.0.1:8000/compute-differences' -Method POST -Headers @{ "Content-Type" = "text/plain" } -Body $body).content


## The expected output will be:
["25200","347067000"]
