"""Example 2: Working with Images from URL"""

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# Create message with image URL
message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe this image in detail."},
        {
            "type": "image_url",
            "image_url": "https://static.desygner.com/wp-content/uploads/sites/13/2022/05/04150103/Free-Stock-Photos-03.jpg"
        },
    ]
)

# Invoke model
response = model.invoke([message])
print(f"Response: {response.content}")
