docker-compose build
docker-compose up

(Invoke-WebRequest -Uri "http://127.0.0.1:8002/compute-differences"  -Method POST  -Headers @{"Content-Type"="text/plain"}  -Body "2`nSun 10 May 2015 13:54:36 -0700`nSun 10 May 2015 13:54:36 -0000`nSat 02 May 2015 19:54:36 +0530`nFri 01 May 2015 13:54:36 -0000").content

{"id":"fca40ac6-b488-4d94-8b71-6d2bee306e31","result":["25200","88200"]}
