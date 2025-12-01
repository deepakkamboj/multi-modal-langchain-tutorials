"""Example 3: Working with Local Images (Base64)"""

import base64
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# Path to your local image
image_path = "path/to/your/image.jpg"

# Read and encode image
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Create message with base64 image
message = HumanMessage(
    content=[
        {"type": "text", "text": "What do you see in this image?"},
        {
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{encoded_image}"
        },
    ]
)

# Invoke model
response = model.invoke([message])
print(f"Response: {response.content}")
