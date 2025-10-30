## Run model.py API
    Terminal 1: uvicorn predict:app --reload --host 0.0.0.0 --port 9696
    Terminal 2: python predict-test.py

## Docker
  Pull Base Image
    
    docker pull agrigorev/zoomcamp-model:2025
  List Images

    docker images
  Build Images
  
    docker build -t zoomcamp-fastapi .
  Run Images
  
    docker run -it --rm -p 9696:9696 zoomcamp-fastapi
  Test Locally
  
    Testing API: python predict-test.py
