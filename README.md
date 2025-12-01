# Chapter 4 Code Examples: Multimodal LangChain Pipelines

This directory contains complete, production-ready code examples for building multimodal LangChain pipelines that process text, image, and audio data.

## File Overview

### Working with Different Media Types

#### `image_url_example.py`
Demonstrates how to pass image URLs to multimodal models for analysis.

**Key Concepts:**
- Image URL handling
- Direct URL passing to models
- GPT-4o-mini vision capabilities

**Usage:**
```bash
python image_url_example.py
```

#### `image_local_base64.py`
Shows how to work with local image files using base64 encoding.

**Key Concepts:**
- Base64 encoding for local files
- Data URI format for images
- Local file processing

**Usage:**
```bash
python image_local_base64.py
```

#### `audio_example.py`
Demonstrates audio file processing with multimodal models.

**Key Concepts:**
- Audio base64 encoding
- Media type handling
- MIME type specification
- GPT-4o-audio-preview usage

**Usage:**
```bash
python audio_example.py
```

#### `video_example.py`
Shows how to pass video files to multimodal models.

**Key Concepts:**
- Video base64 encoding
- Video MIME types
- Direct video analysis

**Usage:**
```bash
python video_example.py
```

### Core Concepts

#### `multimodal_inspection_summarizer.py`
Demonstrates how to combine text notes with visual evidence to generate maintenance summaries using multimodal prompts.

**Key Concepts:**
- Multimodal message construction
- Combining text and image inputs
- Production prompt engineering

**Usage:**
```bash
python multimodal_inspection_summarizer.py
```

#### `image_captioning.py`
Shows how to use Vision-Language Models (V-LLMs) to generate descriptive captions for images that can be indexed for retrieval.

**Key Concepts:**
- OCR extraction
- Vision model integration
- Document creation from images

**Usage:**
```bash
python image_captioning.py
```

#### `multimodal_embeddings.py`
Demonstrates generating aligned embeddings across text, image, and audio modalities for unified vector retrieval.

**Key Concepts:**
- Multimodal embedding models
- Cross-modal similarity computation
- Semantic alignment

**Usage:**
```bash
python multimodal_embeddings.py
```

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
