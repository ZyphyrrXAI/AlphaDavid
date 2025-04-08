# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import tempfile
from fastapi.responses import FileResponse
import subprocess
import os

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your GitHub.io URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LyricsInput(BaseModel):
    lyrics: str
    genre: Optional[str] = "pop"

@app.post("/generate")
async def generate_music(data: LyricsInput):
    # Save lyrics to a temporary text file
    lyrics_file = tempfile.mktemp(suffix=".txt")
    with open(lyrics_file, "w") as f:
        f.write(data.lyrics)

    # Create temporary mp3 output path
    output_file = tempfile.mktemp(suffix=".mp3")

    # Generate melody with AI music model (e.g., MusicGen CLI)
    try:
        subprocess.run([
            "python", "musicgen_cli.py",  # placeholder for the musicgen CLI or script
            "--lyrics", lyrics_file,
            "--output", output_file,
            "--genre", data.genre
        ], check=True)
    except Exception as e:
        return {"error": str(e)}

    return FileResponse(path=output_file, media_type="audio/mpeg", filename="alpha-david-track.mp3")
