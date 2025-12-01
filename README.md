# Mastering Multimodal AI with LangChain

This repository contains complete code examples demonstrating how to build multimodal AI applications using LangChain. The examples cover text, image, audio, and video processing with practical patterns you can use in production.

## 📖 Article

This code accompanies the Medium article: [Mastering Multimodal AI with LangChain](https://medium.com/@deepakkamboj/mastering-multimodal-ai-with-langchain-58c7fd0ed2d2)

## 🎯 Overview

Modern AI systems can now interpret images, transcribe audio, analyze videos, and process documents beyond just text. This repository demonstrates practical implementations of multimodal AI capabilities using LangChain, showing you how to:

- Process different types of media (text, images, audio, video)
- Combine multiple modalities in a single workflow
- Build production-ready multimodal applications
- Follow best practices for multimodal AI development

## 📂 Code Examples

### `01_text_example.py`

**Text-only baseline pattern**

Demonstrates the fundamental pattern for working with LangChain chat models using text inputs.

**Key Concepts:**

- Basic HumanMessage structure
- ChatOpenAI model initialization
- Simple text processing workflow

**Usage:**

```bash
python 01_text_example.py
```

### `02_image_url_example.py`

**Image processing from URLs**

Shows how to analyze images from public URLs using multimodal models.

**Key Concepts:**

- Content blocks with image URLs
- Multimodal message construction
- GPT-4o-mini vision capabilities
- Combining text prompts with image inputs

**Usage:**

```bash
python 02_image_url_example.py
```

### `03_image_local_example.py`

**Local image handling with base64**

Demonstrates processing local image files by encoding them as base64 strings.

**Key Concepts:**

- Base64 encoding for local files
- Data URI format for images
- Handling private/sensitive images
- File size considerations

**Usage:**

```bash
python 03_image_local_example.py
```

### `04_audio_example.py`

**Audio transcription and analysis**

Shows how to process audio files for transcription and content analysis.

**Key Concepts:**

- Audio base64 encoding
- Media type handling with MIME types
- GPT-4o-audio-preview model usage
- Audio format support (MP3, WAV)

**Usage:**

```bash
python 04_audio_example.py
```

### `05_video_example.py`

**Video content understanding**

Demonstrates video file processing for temporal and visual analysis.

**Key Concepts:**

- Video base64 encoding
- Video MIME type specification
- Temporal content analysis
- Motion and scene detection

**Usage:**

```bash
python 05_video_example.py
```

### `06_multimodal_combined.py`

**Combined workflow orchestration**

Shows how to combine multiple modalities in a single practical application, such as infrastructure inspection analysis.

**Key Concepts:**

- Multi-modal input combination
- Sequential analysis patterns
- Real-world workflow implementation
- Comprehensive analysis synthesis

**Usage:**

```bash
python 06_multimodal_combined.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Clone this repository:

```bash
git clone https://github.com/deepakkamboj/multi-modal-langchain-tutorials.git
cd multi-modal-langchain-tutorials
```

2. Create and activate a virtual environment:

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your-actual-api-key-here
```

**Alternative:** Set the API key directly in your terminal session:

**Windows (PowerShell):**

```bash
$env:OPENAI_API_KEY='your-api-key-here'
```

**macOS/Linux:**

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Running Examples

Each example is self-contained and can be run independently:

```bash
python 01_text_example.py
python 02_image_url_example.py
python 03_image_local_example.py
python 04_audio_example.py
python 05_video_example.py
python 06_multimodal_combined.py
```

## 🔑 Key Concepts

### Content Blocks

Structured objects that specify both the type and content of each input component, allowing you to mix text, images, audio, and other media in a single message.

### Multimodal Models

- **GPT-4o-mini**: Best for text and image processing
- **GPT-4o**: Supports text, images, and video
- **GPT-4o-audio-preview**: Includes audio transcription and analysis

### Input Methods

- **URLs**: Most efficient for publicly accessible media
- **Base64 Encoding**: Required for local/private files (increases size by ~33%)

## 💡 Best Practices

1. **Choose the right model**: Different providers support different modalities
2. **Optimize media size**: Compress files before encoding, prefer URLs when possible
3. **Structure prompts clearly**: Provide explicit instructions for each input type
4. **Handle errors gracefully**: Implement fallbacks for unsupported formats
5. **Consider costs**: Multimodal requests typically cost more than text-only
6. **Test with real data**: Use actual user uploads and varied file formats

## 🎓 Learning Path

Start with the simpler examples to understand core patterns:

1. Begin with `01_text_example.py` to understand the baseline
2. Progress to `02_image_url_example.py` for single-modality multimodal
3. Explore `03_image_local_example.py` for file handling
4. Try `04_audio_example.py` and `05_video_example.py` for other media types
5. Study `06_multimodal_combined.py` for production patterns

## 🔮 Extension Challenges

Ready to deepen your understanding? Try these:

1. **Add video keyframe analysis**: Extract keyframes at intervals and analyze separately
2. **Implement streaming**: Use streaming responses for progressive display
3. **Add geographic search**: Filter results based on location metadata
4. **Build a multimodal RAG system**: Combine retrieval with multimodal analysis

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI Vision API](https://platform.openai.com/docs/guides/vision)
- [OpenAI Audio API](https://platform.openai.com/docs/guides/audio)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Deepak Kamboj**

- Medium: [@deepakkamboj](https://medium.com/@deepakkamboj)
- GitHub: [@deepakkamboj](https://github.com/deepakkamboj)

---

⭐ If you find this repository helpful, please give it a star!

### Advanced Workflows

#### `langgraph_multimodal_workflow.py`

Production-grade multimodal workflow using LangGraph with vision analysis, incident summarization, and automatic human escalation.

**Key Concepts:**

- LangGraph state management
- Conditional routing
- Human-in-the-loop patterns
- Severity assessment

**Usage:**

```bash
python langgraph_multimodal_workflow.py
```

### Data Management

#### `incremental_indexing.py`

Handles document updates in a vector indexer with deduplication and version management.

**Key Concepts:**

- Unique chunk ID generation
- Update vs. insert logic
- Deduplication strategies
- Vector store operations

**Usage:**

```bash
python incremental_indexing.py
```

#### `parallel_multimodal_indexing.py`

Complete multimodal indexing pipeline with parallel processing across all modalities using LCEL.

**Key Concepts:**

- RunnableParallel orchestration
- Concurrent modality processing
- Batch insertion
- Performance optimization

**Usage:**

```bash
python parallel_multimodal_indexing.py
```

### Observability

#### `observability_tracing.py`

Demonstrates LangSmith tracing and custom metrics for production monitoring.

**Key Concepts:**

- LangSmith integration
- Per-modality metrics
- Error tracking
- Cost attribution

**Usage:**

```bash
export LANGCHAIN_API_KEY="your-api-key"
export LANGCHAIN_PROJECT="multimodal-demo"
python observability_tracing.py
```

## Installation

Install required dependencies:

```bash
pip install langchain langchain-openai langchain-community chromadb pillow pytesseract openai
```

For additional examples:

```bash
pip install langgraph langsmith opencv-python moviepy
```

## Configuration

Set your API keys:

```bash
export OPENAI_API_KEY="your-openai-api-key"
export LANGCHAIN_API_KEY="your-langsmith-api-key"  # Optional, for tracing
export LANGCHAIN_PROJECT="your-project-name"        # Optional, for tracing
```

## Running Examples

Each example is self-contained and can be run independently:

```bash
# Media type examples (from screenshots)
python image_url_example.py
python image_local_base64.py
python audio_example.py
python video_example.py

# Basic multimodal example
python multimodal_inspection_summarizer.py

# Advanced pipeline
python parallel_multimodal_indexing.py
```

## Integration with Chapter Content

These examples support the concepts taught in Chapter 4:

- **Section 4.1**: `multimodal_inspection_summarizer.py`, `image_captioning.py`
- **Section 4.2**: `image_captioning.py` (preprocessing)
- **Section 4.3**: `multimodal_embeddings.py`
- **Section 4.4**: `langgraph_multimodal_workflow.py`, `incremental_indexing.py`, `parallel_multimodal_indexing.py`
- **Section 4.5**: `multimodal_embeddings.py` (retrieval concepts)
- **Production patterns**: `observability_tracing.py`

## Architecture Patterns

These examples demonstrate several production patterns:

1. **Parallel Processing**: Use `RunnableParallel` to process modalities concurrently
2. **Incremental Updates**: Manage document versions and deduplication
3. **Graph Orchestration**: Use LangGraph for complex conditional workflows
4. **Observability**: Track metrics and traces for production monitoring
5. **Error Handling**: Implement retry strategies per modality

## Extending the Examples

To adapt these examples for your use case:

1. **Custom Loaders**: Replace placeholder loaders with actual OCR (pytesseract) and Whisper implementations
2. **Vector Stores**: Swap Chroma with Pinecone, Weaviate, or other production vector databases
3. **Embedding Models**: Use specialized multimodal embeddings (CLIP, ImageBind)
4. **Monitoring**: Integrate with your observability stack (Datadog, Prometheus)

## Troubleshooting

### Common Issues

**ImportError for langsmith:**

```bash
pip install langsmith
```

**Missing API keys:**
Ensure `OPENAI_API_KEY` is set in your environment.

**Vector store errors:**
Chroma requires a local directory. The examples create this automatically, but you may need write permissions.

**Image processing errors:**
For actual OCR, install tesseract:

```bash
# macOS
brew install tesseract

# Ubuntu
sudo apt-get install tesseract-ocr

# Windows
# Download from https://github.com/UB-Mannheim/tesseract/wiki
```

## Performance Considerations

- **Parallel Processing**: Reduces total indexing time from O(n) to O(max(modality_times))
- **Batch Operations**: Use batch embedding and insertion for better throughput
- **Caching**: Implement content hashing to avoid reprocessing identical files
- **Rate Limiting**: Add exponential backoff for API calls

## Security Notes

- Store API keys in environment variables, never in code
- Redact sensitive information before sending to external APIs
- Implement access controls for vector stores
- Log all operations for audit trails
- Use HTTPS for image URLs

## License

These examples are provided as educational materials for the book "Building LangChain Agents" and are available under the MIT License.

## Support

For questions or issues:

- Reference Chapter 4 in the book
- Check the troubleshooting section above
- Review LangChain documentation: https://docs.langchain.com/
