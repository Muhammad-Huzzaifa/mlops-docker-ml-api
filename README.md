# ML Docker Deployment (FastAPI + Scikit-learn)

This project demonstrates the deployment of a machine learning model using FastAPI and Docker. The model is trained on the California Housing dataset and exposed through a REST API.

---

## Project Structure

```

ml-docker-deployment/
│
├── app/
│   ├── main.py
│   ├── model.py
│
├── model/
│   ├── train.py
│   ├── model.pkl
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md

````

---

## Machine Learning Model

- Dataset: California Housing (from scikit-learn)
- Algorithm: Linear Regression
- Output: Predicted house price

### Train the Model

```bash
python model/train.py
````

This will generate the file `model/model.pkl`.

---

## API Endpoints

### Health Check

```
GET /
```

Response:

```json
{
  "message": "ML API is running"
}
```

---

### Prediction Endpoint

```
POST /predict
```

Example request body:

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.984,
  "AveBedrms": 1.023,
  "Population": 322,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

Example response:

```json
{
  "predicted_house_price": 4.5
}
```

---

## Run the API Locally

Install dependencies and start the server:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

---

## Docker Instructions

### Build Docker Image

```bash
docker build -t ml-api .
```

### List Docker Images

```bash
docker images
```

### Run Docker Container

```bash
docker run -d -p 8000:8000 ml-api
```

---

## Docker Hub Deployment

### Login to Docker Hub

```bash
docker login
```

### Tag the Image

```bash
docker tag ml-api <your-dockerhub-username>/ml-api
```

### Push the Image

```bash
docker push <your-dockerhub-username>/ml-api
```

---

## Pull and Run from Docker Hub

### Pull Image

```bash
docker pull <your-dockerhub-username>/ml-api
```

### Run Pulled Image

```bash
docker run -d -p 8000:8000 <your-dockerhub-username>/ml-api
```

---

## Testing the API

After running the container, open:

```
http://127.0.0.1:8000/docs
```

Use the `/predict` endpoint with the provided JSON input to get predictions.

## Notes

* Do not upload Docker images to GitHub
* Replace `<your-dockerhub-username>` with your actual Docker Hub username
* Ensure that `model.pkl` exists before running Docker

---

## Technologies Used

* Python 3.10
* FastAPI
* Scikit-learn
* Docker

---

## Conclusion

This project demonstrates how a machine learning model can be trained, exposed through an API, containerized using Docker, and deployed in a reproducible environment.
