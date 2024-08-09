import datetime
import os
import time

import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai import caching

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Download video file
# curl -O https://storage.googleapis.com/generativeai-downloads/data/Sherlock_Jr_FullMovie.mp4

path_to_video_file = "Sherlock_Jr_FullMovie.mp4"

# Upload the video using the Files API
video_file = genai.upload_file(path=path_to_video_file)

# Wait for the file to finish processing
while video_file.state.name == "PROCESSING":
    print("Waiting for video to be processed.")
    time.sleep(2)
    video_file = genai.get_file(video_file.name)

print(f"Video processing complete: {video_file.uri}")

# Create a cache with a 5 minute TTL
cache = caching.CachedContent.create(
    model="models/gemini-1.5-flash-001",
    display_name="sherlock jr movie",  # used to identify the cache
    system_instruction=(
        "You are an expert video analyzer, and your job is to answer "
        "the user's query based on the video file you have access to."
    ),
    contents=[video_file],
    ttl=datetime.timedelta(minutes=5),
)

# Construct a GenerativeModel which uses the created cache.
model = genai.GenerativeModel.from_cached_content(cached_content=cache)

# Query the model
response = model.generate_content(
    [
        (
            "Introduce different characters in the movie by describing "
            "their personality, looks, and names. Also list the timestamps "
            "they were introduced for the first time."
        )
    ]
)

print(response.usage_metadata)

# The output should look something like this:
#
# prompt_token_count: 696219
# cached_content_token_count: 696190
# candidates_token_count: 214
# total_token_count: 696433

print(response.text)
