
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.face_detection import detect_faces
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

@app.post("/detect-faces")
async def detect_faces_api(image: UploadFile = File(...)):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    try:
        # Save the uploaded file temporarily
        with open("temp_image.jpg", "wb") as buffer:
            buffer.write(await image.read())

        # Detect faces
        result = detect_faces("temp_image.jpg")

        # Clean up
        os.remove("temp_image.jpg")

        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
