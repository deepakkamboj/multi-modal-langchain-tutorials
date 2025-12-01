"""Example 1: Working with Text Data"""

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize model
model = ChatOpenAI(model="gpt-4o-mini")

# Create text message
message = HumanMessage(
    content="Summarize the key features of multimodal AI systems."
)

# Invoke model
response = model.invoke([message])
print(f"Response: {response.content}")
