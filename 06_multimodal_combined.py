"""Example 6: Combining Multiple Modalities"""

import base64
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Initialize model
model = ChatOpenAI(model="gpt-4o")

# Example: Analyze inspection with text notes + image
image_url = "https://example.com/bridge-inspection.jpg"

# Create multimodal message
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Inspection Notes: Visible crack on girder section 3. "
                    "Need assessment before reopening lane. "
                    "Please analyze the image and provide recommendations."
        },
        {
            "type": "image_url",
            "image_url": image_url
        },
    ]
)

# Invoke model
response = model.invoke([message])
print(f"Analysis: {response.content}")

# ----- Alternative: Local image + audio combination -----

def analyze_multimodal_inspection(image_path: str, audio_path: str):
    """Combine local image and audio for comprehensive analysis."""

    # Encode image
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

    # Encode audio
    with open(audio_path, "rb") as audio_file:
        encoded_audio = base64.b64encode(audio_file.read()).decode("utf-8")

    # First: Analyze image
    image_message = HumanMessage(
        content=[
            {"type": "text", "text": "Describe any structural issues visible."},
            {
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{encoded_image}"
            },
        ]
    )

    image_analysis = model.invoke([image_message]).content

    # Second: Transcribe audio
    audio_message = HumanMessage(
        content=[
            {"type": "text", "text": "Transcribe this inspection audio."},
            {
                "type": "media",
                "data": encoded_audio,
                "mime_type": "audio/mpeg",
            },
        ]
    )

    audio_model = ChatOpenAI(model="gpt-4o-audio-preview")
    audio_transcript = audio_model.invoke([audio_message]).content

    # Third: Synthesize findings
    synthesis_message = HumanMessage(
        content=f"""Based on the following inspection data, provide a comprehensive report:

Visual Analysis: {image_analysis}

Audio Notes: {audio_transcript}

Provide:
1. Summary of findings
2. Risk assessment
3. Recommended actions
"""
    )

    final_report = model.invoke([synthesis_message]).content
    return final_report

# Usage (uncomment with real file paths):
# report = analyze_multimodal_inspection("inspection.jpg", "notes.mp3")
# print(report)
