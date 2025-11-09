from fastapi import APIRouter, HTTPException
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
import os
import json
import time
from pathlib import Path
from google import genai
from google.genai import types

router = APIRouter(
    prefix="/api/v1/analyze",
    tags=["analyze"]
)

# Get API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# JSON database path
DB_PATH = Path(__file__).parent.parent.parent / "data" / "analysis.json"


def load_db():
    """Load analysis database from JSON file"""
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)


def save_db(data):
    """Save analysis database to JSON file"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)


def analyze_video_with_retry(video_path: str, max_retries: int = 2) -> dict:
    """
    Analyze video using Gemini Flash with retry logic
    max_retries: 2 means 3 total attempts (1 initial + 2 retries)
    """
    prompt = """Analyze this video and extract the following information in JSON format:
{
  "trend_name": "The name of the trend shown in the video",
  "why_trending": "Explanation of why this content is trending",
  "category": "The category this trend belongs to"
}

Provide ONLY the JSON object, no additional text."""

    # Read the video file
    video = types.Video.from_file(video_path)

    for attempt in range(max_retries + 1):
        try:
            response = client.models.generate_content(
                model='gemini-flash-latest',
                contents=[prompt, video]
            )

            # Parse the JSON response
            response_text = response.text.strip()
            # Remove markdown code blocks if present
            if response_text.startswith("```"):
                response_text = response_text.split("```")[1]
                if response_text.startswith("json"):
                    response_text = response_text[4:]
                response_text = response_text.strip()

            result = json.loads(response_text)

            # Add video reference
            result["video_reference"] = video_path

            return result

        except Exception as e:
            if attempt < max_retries:
                # Wait before retrying (exponential backoff)
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            else:
                # All retries exhausted, raise error
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to analyze video after {max_retries + 1} attempts: {str(e)}"
                )


@router.post("/", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    """Analyze video and extract trend information using Gemini Flash"""

    # Validate video path exists
    if not os.path.exists(request.video_path):
        raise HTTPException(status_code=404, detail=f"Video file not found: {request.video_path}")

    # Analyze video with retry logic
    analysis_result = analyze_video_with_retry(request.video_path, max_retries=2)

    # Load existing database
    db = load_db()

    # Add new analysis to database
    db.append(analysis_result)

    # Save to database
    save_db(db)

    return AnalyzeResponse(
        status="success",
        message="Analysis saved"
    )
