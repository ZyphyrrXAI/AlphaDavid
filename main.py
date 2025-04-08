# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import tempfile
from fastapi.responses import FileResponse

import some_fake_ai_music_library as ai  # Placeholder: Replace with real AI engine

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LyricsInput(BaseModel):
    lyrics: str
    genre: Optional[str] = "pop"

@app.post("/generate")
async def generate_music(data: LyricsInput):
    # AI Music Generator Logic
    filename = tempfile.mktemp(suffix=".mp3")

    # ⚠️ Placeholder for AI engine:
    ai.generate_music_from_lyrics(data.lyrics, filename, genre=data.genre)

    return FileResponse(path=filename, media_type="audio/mpeg", filename="alpha-david-track.mp3")
