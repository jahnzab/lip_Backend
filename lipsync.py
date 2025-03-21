# #sudo apt update
# #sudo apt install python3.8 python3.8-venv python3.8-dev  #ubuntu

# #python3.8 -m venv enyv
# #source enyv/bin/activate

# # .....>   to remove previous swap and make new 
# #sudo swapoff -a
# #sudo rm -f /swapfile
# #sudo fallocate -l 4G /swapfile
# # sudo chmod 600 /swapfile
# # sudo mkswap /swapfile
# # sudo swapon /swapfile


# #-------------->to increse speed use this
# # sadtalker_cmd = [
# #     "python", f"{SADTALKER_DIR}/inference.py",
# #     "--driven_audio", audio_path,
# #     "--source_image", img_path,
# #     "--result_dir", OUTPUT_DIR,
# #     "--size", "256",  # Reduce face resolution for faster processing
# #     "--still",  # Reduce unnecessary head movement
# #     "--preprocess", "crop"  # Avoid extra processing
# # ]



# #sudo apt update
# #sudo apt install python3.8 python3.8-venv python3.8-dev  #ubuntu

# #python3.8 -m venv enyv
# #source enyv/bin/activate

# # .....>   to remove previous swap and make new 
# #sudo swapoff -a
# #sudo rm -f /swapfile
# #sudo fallocate -l 4G /swapfile
# # sudo chmod 600 /swapfile
# # sudo mkswap /swapfile
# # sudo swapon /swapfile


# #-------------->to increse speed use this
# # sadtalker_cmd = [
# #     "python", f"{SADTALKER_DIR}/inference.py",
# #     "--driven_audio", audio_path,
# #     "--source_image", img_path,
# #     "--result_dir", OUTPUT_DIR,
# #     "--size", "256",  # Reduce face resolution for faster processing
# #     "--still",  # Reduce unnecessary head movement
# #     "--preprocess", "crop"  # Avoid extra processing
# # ]



# # import os
# # import uuid
# # import aiofiles
# # import requests
# # import subprocess
# # from fastapi import FastAPI, File, UploadFile, Form, HTTPException
# # from fastapi.responses import FileResponse
# # from fastapi.staticfiles import StaticFiles
# # from typing import Optional
# # from fastapi.middleware.cors import CORSMiddleware
# # from gtts import gTTS
# # import glob


# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Define directories
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# # SADTALKER_DIR = os.path.join(BASE_DIR, "SadTalker")

# # # Ensure the output directory exists
# # os.makedirs(OUTPUT_DIR, exist_ok=True)

# # # Mount static directory to serve generated files
# # app.mount("/output", StaticFiles(directory=OUTPUT_DIR), name="output")

# # @app.post("/generate_audio/")
# # async def generate_audio(text: str = Form(...)):
# #     """Convert text to speech using gTTS."""
# #     if not text:
# #         raise HTTPException(status_code=400, detail="Text input is required for TTS.")

# #     audio_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}.mp3")

# #     try:
# #         tts = gTTS(text, lang="en")  # Convert text to speech
# #         tts.save(audio_path)  # Save as an MP3 file
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

# #     return {"audio_url": f"http://localhost:8000/output/{os.path.basename(audio_path)}"}


# # @app.post("/generate_video/")
# # async def generate_video(
# #     image: UploadFile = File(...),
# #     audio: Optional[UploadFile] = File(None),
# #     text: Optional[str] = Form(None),
# # ):
# #     """Generate talking avatar video using SadTalker."""
# #     if not image:
# #         raise HTTPException(status_code=400, detail="Image file is required.")

# #     # Save uploaded image
# #     img_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}_{image.filename}")
# #     async with aiofiles.open(img_path, 'wb') as out_file:
# #         await out_file.write(await image.read())

# #     audio_path = None

# #     # If an audio file is uploaded (real-time recording or existing file)
# #     if audio:
# #         audio_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}_{audio.filename}")
# #         async with aiofiles.open(audio_path, 'wb') as out_file:
# #             await out_file.write(await audio.read())

# #     # If text is provided, generate TTS audio using gTTS
# #     elif text:
# #         audio_path = os.path.join(OUTPUT_DIR, f"{uuid.uuid4()}.mp3")
# #         try:
# #             tts = gTTS(text, lang="en")
# #             tts.save(audio_path)
# #         except Exception as e:
# #             raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

# #     # Ensure there's an audio source
# #     if not audio_path:
# #         raise HTTPException(status_code=400, detail="Either an audio file or text input is required.")

# #     # Generate video using SadTalker
# #     sadtalker_cmd = [
# #         "python", f"{SADTALKER_DIR}/inference.py",
# #         "--driven_audio", audio_path,
# #         "--source_image", img_path,
# #         "--result_dir", OUTPUT_DIR,
# #     ]

# #     try:
# #         subprocess.run(sadtalker_cmd, check=True)
# #     except subprocess.CalledProcessError:
# #         raise HTTPException(status_code=500, detail="SadTalker failed to generate video.")

# #     # Find the latest generated video
# #     video_files = glob.glob(os.path.join(OUTPUT_DIR, "*.mp4"))
# #     if not video_files:
# #         raise HTTPException(status_code=500, detail="Video file not found.")

# #     latest_video_path = max(video_files, key=os.path.getctime)
# #     video_filename = os.path.basename(latest_video_path)

# #     return {"video_url": f"http://localhost:8000/output/{video_filename}"}

# # @app.get("/download/{file_name}")
# # async def download_file(file_name: str):
# #     """Download generated audio or video files."""
# #     file_path = os.path.join(OUTPUT_DIR, file_name)
    
# #     if not os.path.exists(file_path):
# #         raise HTTPException(status_code=404, detail="File not found")

# #     return FileResponse(file_path)


# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)


# # import os
# # import uuid
# # import aiofiles
# # import subprocess
# # from fastapi import FastAPI, File, UploadFile, Form, HTTPException
# # from fastapi.responses import FileResponse
# # from fastapi.staticfiles import StaticFiles
# # from typing import Optional
# # from fastapi.middleware.cors import CORSMiddleware
# # from gtts import gTTS
# # import glob

# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Define directories
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# # SADTALKER_DIR = os.path.join(BASE_DIR, "SadTalker")

# # # Ensure output directory exists
# # os.makedirs(OUTPUT_DIR, exist_ok=True)

# # # Serve generated files
# # app.mount("/output", StaticFiles(directory=OUTPUT_DIR), name="output")


# # @app.post("/generate_audio/")
# # async def generate_audio(text: str = Form(...)):
# #     """Convert text to speech using gTTS."""
# #     if not text:
# #         raise HTTPException(status_code=400, detail="Text input is required for TTS.")

# #     audio_filename = f"{uuid.uuid4()}.mp3"
# #     audio_path = os.path.join(OUTPUT_DIR, audio_filename)

# #     try:
# #         tts = gTTS(text, lang="en")
# #         tts.save(audio_path)
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

# #     return {
# #         "audio_url": f"http://localhost:8000/output/{audio_filename}",
# #         "file_name": audio_filename,
# #     }


# # @app.post("/generate_video/")
# # async def generate_video(
# #     image: UploadFile = File(...),
# #     audio: Optional[UploadFile] = File(None),
# #     text: Optional[str] = Form(None),
# # ):
# #     """Generate talking avatar video using SadTalker."""
# #     if not image:
# #         raise HTTPException(status_code=400, detail="Image file is required.")

# #     # Save uploaded image
# #     img_filename = f"{uuid.uuid4()}_{image.filename}"
# #     img_path = os.path.join(OUTPUT_DIR, img_filename)
# #     async with aiofiles.open(img_path, "wb") as out_file:
# #         await out_file.write(await image.read())

# #     audio_path = None

# #     # If an audio file is uploaded
# #     if audio:
# #         audio_filename = f"{uuid.uuid4()}_{audio.filename}"
# #         audio_path = os.path.join(OUTPUT_DIR, audio_filename)
# #         async with aiofiles.open(audio_path, "wb") as out_file:
# #             await out_file.write(await audio.read())

# #     # If text is provided, generate TTS
# #     elif text:
# #         audio_filename = f"{uuid.uuid4()}.mp3"
# #         audio_path = os.path.join(OUTPUT_DIR, audio_filename)
# #         try:
# #             tts = gTTS(text, lang="en")
# #             tts.save(audio_path)
# #         except Exception as e:
# #             raise HTTPException(status_code=500, detail=f"GTTS generation failed please upload a good quality image: {str(e)}")

# #     # Ensure an audio source exists
# #     if not audio_path or not os.path.exists(audio_path):
# #         raise HTTPException(status_code=400, detail="Valid audio file or text input is required.")

# #     # Generate video using SadTalker
# #     sadtalker_cmd = [
# #         "python", f"{SADTALKER_DIR}/inference.py",
# #         "--driven_audio", audio_path,
# #         "--source_image", img_path,
# #         "--result_dir", OUTPUT_DIR,
# #     ]

# #     try:
# #         subprocess.run(sadtalker_cmd, check=True)
# #     except subprocess.CalledProcessError:
# #         raise HTTPException(status_code=500, detail="SadTalker failed to generate video.")

# #     # Get the latest MP4 file
# #     video_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*.mp4")), key=os.path.getctime, reverse=True)
# #     if not video_files:
# #         raise HTTPException(status_code=500, detail="Video generation failed.")

# #     video_filename = os.path.basename(video_files[0])

# #     return {"video_url": f"http://localhost:8000/output/{video_filename}"}


# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="0.0.0.0", port=8000)




# import os
# import uuid
# import aiofiles
# import subprocess
# import glob
# import asyncio
# from fastapi import FastAPI, File, UploadFile, Form, HTTPException
# from fastapi.responses import JSONResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
# from gtts import gTTS

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Define directories
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# SADTALKER_DIR = os.path.join(BASE_DIR, "SadTalker")

# # Ensure output directory exists
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# # Serve generated files
# app.mount("/output", StaticFiles(directory=OUTPUT_DIR), name="output")

# @app.post("/generate_audio/")
# async def generate_audio(text: str = Form(...)):
#     """Convert text to speech using gTTS."""
#     print(f"Received text: {text}")  # Debugging line

#     if not text:
#         raise HTTPException(status_code=400, detail="Text input is required for TTS.")

#     audio_filename = f"{uuid.uuid4()}.mp3"
#     audio_path = os.path.join(OUTPUT_DIR, audio_filename)

#     try:
#         tts = gTTS(text, lang="en")
#         tts.save(audio_path)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

#     return {
#         "audio_url": f"http://localhost:8000/output/{audio_filename}",
#         "file_name": audio_filename,
#     }

# @app.post("/generate_video/")
# async def generate_video(
#     image: UploadFile = File(...),
#     audio: UploadFile = File(None),
#     text: str = Form(None),
# ):
#     """Generate talking avatar video using SadTalker."""
#     if not image:
#         raise HTTPException(status_code=400, detail="Image file is required.")

#     # Save uploaded image
#     img_filename = f"{uuid.uuid4()}_{image.filename}"
#     img_path = os.path.join(OUTPUT_DIR, img_filename)
#     async with aiofiles.open(img_path, "wb") as out_file:
#         await out_file.write(await image.read())

#     audio_path = None

#     # If an audio file is uploaded
#     if audio:
#         audio_filename = f"{uuid.uuid4()}_{audio.filename}"
#         audio_path = os.path.join(OUTPUT_DIR, audio_filename)
#         async with aiofiles.open(audio_path, "wb") as out_file:
#             await out_file.write(await audio.read())

#     # If text is provided, generate TTS
#     elif text:
#         audio_filename = f"{uuid.uuid4()}.mp3"
#         audio_path = os.path.join(OUTPUT_DIR, audio_filename)
#         try:
#             tts = gTTS(text, lang="en")
#             tts.save(audio_path)
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

#     # Ensure an audio source exists
#     if not audio_path or not os.path.exists(audio_path):
#         raise HTTPException(status_code=400, detail="Valid audio file or text input is required.")

#     # Generate video using SadTalker
#     sadtalker_cmd = [
#         "python", f"{SADTALKER_DIR}/inference.py",
#         "--driven_audio", audio_path,
#         "--source_image", img_path,
#         "--result_dir", OUTPUT_DIR,
#     ]

#     try:
#         subprocess.run(sadtalker_cmd, check=True)
#     except subprocess.CalledProcessError:
#         raise HTTPException(status_code=500, detail="SadTalker failed to generate video.")

#     # Get the latest MP4 file
#     video_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*.mp4")), key=os.path.getctime, reverse=True)
#     if not video_files:
#         raise HTTPException(status_code=500, detail="Video generation failed.")

#     video_filename = os.path.basename(video_files[0])

#     return {"video_url": f"http://localhost:8000/output/{video_filename}"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
import os
import uuid
import aiofiles
import subprocess
import glob
import asyncio
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SADTALKER_DIR = os.path.join(BASE_DIR, "SadTalker")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Serve generated files
app.mount("/output", StaticFiles(directory=OUTPUT_DIR), name="output")

@app.post("/generate_audio/")
async def generate_audio(text: str = Form(...)):
    """Convert text to speech using gTTS."""
    print(f"Received text: {text}")  # Debugging line

    if not text:
        raise HTTPException(status_code=400, detail="Text input is required for TTS.")

    audio_filename = f"{uuid.uuid4()}.mp3"
    audio_path = os.path.join(OUTPUT_DIR, audio_filename)

    try:
        tts = gTTS(text, lang="en")
        tts.save(audio_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

    return {
        "audio_url": f"http://localhost:8000/output/{audio_filename}",
        "file_name": audio_filename,
    }

@app.post("/generate_video/")
async def generate_video(
    image: UploadFile = File(...),
    audio: UploadFile = File(None),
    text: str = Form(None),
):
    """Generate talking avatar video using SadTalker."""
    if not image:
        raise HTTPException(status_code=400, detail="Image file is required.")

    # Save uploaded image
    img_filename = f"{uuid.uuid4()}_{image.filename}"
    img_path = os.path.join(OUTPUT_DIR, img_filename)
    async with aiofiles.open(img_path, "wb") as out_file:
        await out_file.write(await image.read())

    audio_path = None

    # If an audio file is uploaded
    if audio:
        audio_filename = f"{uuid.uuid4()}_{audio.filename}"
        audio_path = os.path.join(OUTPUT_DIR, audio_filename)
        async with aiofiles.open(audio_path, "wb") as out_file:
            await out_file.write(await audio.read())

    # If text is provided, generate TTS
    elif text:
        audio_filename = f"{uuid.uuid4()}.mp3"
        audio_path = os.path.join(OUTPUT_DIR, audio_filename)
        try:
            tts = gTTS(text, lang="en")
            tts.save(audio_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"GTTS generation failed: {str(e)}")

    # Ensure an audio source exists
    if not audio_path or not os.path.exists(audio_path):
        raise HTTPException(status_code=400, detail="Valid audio file or text input is required.")

    # Generate video using SadTalker
    sadtalker_cmd = [
        "python", f"{SADTALKER_DIR}/inference.py",
        "--driven_audio", audio_path,
        "--source_image", img_path,
        "--result_dir", OUTPUT_DIR,
    ]

    try:
        subprocess.run(sadtalker_cmd, check=True)
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="SadTalker failed to generate video.")

    # Get the latest MP4 file
    video_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*.mp4")), key=os.path.getctime, reverse=True)
    if not video_files:
        raise HTTPException(status_code=500, detail="Video generation failed.")

    video_filename = os.path.basename(video_files[0])

    return {"video_url": f"http://localhost:8000/output/{video_filename}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

