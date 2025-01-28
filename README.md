# Face Detection API with Azure Face API

## Overview

The **Face Detection API** is a Python-based application that integrates with the Azure Face API to detect faces in images and retrieve detailed attributes such as:
- Age
- Gender
- Emotions (anger, contempt, disgust, fear, happiness, neutral, sadness, surprise)
- Glasses type
- Hair color and style
- Smile intensity

This project leverages FastAPI for building a high-performance web API and includes Docker support for seamless deployment.

## Features

- **Face Detection**: Upload an image, and the API will return detailed face attributes and face bounding box information.
- **Attribute Detection**: Get precise details about facial features and emotions.
- **Containerized Deployment**: Easily deploy the API using Docker.
- **Azure Integration**: Leverages Microsoft Azure's Face API for reliable and robust face detection.
- **Azure Container Registry (ACR) Support**: Push and manage Docker images in ACR for efficient Azure deployments.

## How It Works

1. **Image Upload**: Users send an image file to the API endpoint.
2. **Azure Face API Interaction**: The uploaded image is processed using Azure Face API, which returns detailed face attributes.
3. **Response Generation**: The API formats the Azure Face API response and returns it to the user in a structured JSON format.

---

## Prerequisites

1. **Azure Face API Subscription**:
   - Create an Azure account at [Azure Portal](https://portal.azure.com/).
   - Navigate to the Azure Cognitive Services and create a Face API resource.
   - Retrieve the **endpoint** and **API key** from the Azure Portal.

2. **Python Environment**:
   - Python 3.9 or higher is required.

3. **Docker**:
   - Install Docker from [Docker's official website](https://www.docker.com/).

4. **Azure CLI** (if using Azure Container Registry):
   - Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/face-detection-api.git
cd face-detection-api
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
AZURE_FACE_API_ENDPOINT=your_azure_face_api_endpoint
AZURE_FACE_API_KEY=your_azure_face_api_key
```

Replace `your_azure_face_api_endpoint` and `your_azure_face_api_key` with the values from your Azure Face API resource.

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the API

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The API will now be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Docker Deployment

### 1. Build the Docker Image

Build the Docker image using the provided `Dockerfile`:

```bash
docker build -t face-detection-api .
```

### 2. Run the Docker Container

Run the Docker container:

```bash
docker run -p 8000:8000 --env-file .env face-detection-api
```

The API will now be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Azure Container Registry (ACR) Deployment

### 1. Create an Azure Container Registry

1. Go to the [Azure Portal](https://portal.azure.com/).
2. Create a new **Container Registry** resource.
3. Note the **Login Server** (e.g., `myacrname.azurecr.io`).

### 2. Push the Docker Image to ACR

1. Log in to Azure:

   ```bash
   az login
   ```

2. Log in to your ACR:

   ```bash
   az acr login --name <your-acr-name>
   ```

3. Tag your Docker image:

   ```bash
   docker tag face-detection-api <your-acr-name>.azurecr.io/face-detection-api:v1
   ```

4. Push the image to ACR:

   ```bash
   docker push <your-acr-name>.azurecr.io/face-detection-api:v1
   ```

### 3. Deploy Using Azure Services

- **Azure App Service**:
  Use the image in ACR to create a web app.
- **Azure Kubernetes Service (AKS)**:
  Orchestrate and manage the container using Kubernetes.
- **Azure Container Instances (ACI)**:
  Run the container directly:

  ```bash
  az container create --resource-group <resource-group>       --name face-detection-api       --image <your-acr-name>.azurecr.io/face-detection-api:v1       --dns-name-label <unique-name>       --ports 8000
  ```

---

## File Structure

```
face-detection-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   └── face_detection.py # Azure Face API interaction logic
│
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
├── LICENSE              # License information
└── .env                 # Environment variables
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Marco Di Bella
