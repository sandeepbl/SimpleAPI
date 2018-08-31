# Simple API server 

## Run Instructions:

- Create and Activate Virtual Environment if required

- Install requirements with the  command:

  `pip install -r requirements.txt`

- Run api server with the command:
  
  `python api.py`

- use curl command as below for GET:
    
  `curl "http://localhost:9999/api"`

- use curl command as below for POST:
    
  `curl -X POST -H "Content-Type: application/json" -d '{"input":"string"}' "http://localhost:9999/api"`

> Note: No error handling or unit tests included.
