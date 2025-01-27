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

3. **Docker** (Optional):
   - Install Docker from [Docker's official website](https://www.docker.com/).

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

## Usage

### 1. Detect Faces

Send a POST request to the `/detect-faces` endpoint with an image file. You can use tools like `curl`, Postman, or any HTTP client library in your preferred programming language.

#### Example Using `curl`:

```bash
curl -X POST -F "image=@path_to_your_image.jpg" http://127.0.0.1:8000/detect-faces
```

#### Example Response:

```json
[
    {
        "face_id": "c5c24a82-6845-4031-9d5d-978df587f4d1",
        "age": 25.5,
        "gender": "female",
        "emotion": {
            "anger": 0.0,
            "contempt": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "happiness": 1.0,
            "neutral": 0.0,
            "sadness": 0.0,
            "surprise": 0.0
        },
        "glasses": "NoGlasses",
        "hair": {
            "bald": 0.0,
            "invisible": false,
            "hair_color": [
                {"color": "brown", "confidence": 1.0}
            ]
        },
        "smile": 0.99,
        "face_rectangle": {
            "top": 100,
            "left": 150,
            "width": 200,
            "height": 200
        }
    }
]
```

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
