"""Example 5: Working with Video Files"""

import base64
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize model
model = ChatOpenAI(model="gpt-4o")

# Path to your video file
video_path = "path/to/your/video.mp4"

# Read and encode video
with open(video_path, "rb") as video_file:
    encoded_video = base64.b64encode(video_file.read()).decode("utf-8")

# Create message with video
message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe what happens in this video."},
        {
            "type": "media",
            "data": encoded_video,
            "mime_type": "video/mp4",
        },
    ]
)

# Invoke model
response = model.invoke([message])
print(f"Response: {response.content}")
