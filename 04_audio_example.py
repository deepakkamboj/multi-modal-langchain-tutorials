"""Example 4: Working with Audio Files"""

import base64
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize audio-capable model
model = ChatOpenAI(model="gpt-4o-audio-preview")

# Path to your audio file
audio_path = "path/to/your/audio.mp3"

# Read and encode audio
with open(audio_path, "rb") as audio_file:
    encoded_audio = base64.b64encode(audio_file.read()).decode("utf-8")

# Create message with audio
message = HumanMessage(
    content=[
        {"type": "text", "text": "Transcribe and summarize this audio."},
        {
            "type": "media",
            "data": encoded_audio,
            "mime_type": "audio/mpeg",
        },
    ]
)

# Invoke model
response = model.invoke([message])
print(f"Response: {response.content}")
