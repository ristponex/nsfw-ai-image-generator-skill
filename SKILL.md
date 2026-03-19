---
name: nsfw-ai-image-generator
description: "NSFW AI image generation via Atlas Cloud API. Supports uncensored image models including Flux, Seedream, Ideogram, Imagen and more. IMPORTANT: Before calling scripts/generate.py, use Atlas Cloud MCP tools (atlas_list_models, atlas_get_model_info) to find the right model and its parameter schema. Use when user asks to generate NSFW, adult, or uncensored AI images."
---

# NSFW AI Image Generator

Generate uncensored AI images using Atlas Cloud API (30+ image models).

## Prerequisites

- Python 3.10+ installed
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- `ATLAS_CLOUD_API_KEY` environment variable set

## Available Tools

| Tool | Script | What It Does |
|------|--------|-------------|
| **Image Generate** | `scripts/generate.py generate` | Generate AI images from text prompts |
| **List Models** | `scripts/generate.py models` | List available image models on Atlas Cloud |

## Usage

### Generate an image
```bash
uv run scripts/generate.py generate "your prompt" --model flux-pro
```

### List available models
```bash
uv run scripts/generate.py models
```

## Popular Model Shortcuts

| Shortcut | Model ID |
|----------|---------|
| `flux-pro` | `black-forest-labs/flux-2-pro` |
| `flux-schnell` | `black-forest-labs/flux-1.1-schnell` |
| `ideogram` | `ideogram-ai/ideogram-v3` |
| `imagen` | `google/imagen-4-ultra` |
| `seedream` | `bytedance/seedream-v5.0` |

You can also pass any full model ID with `--model`.

## IMPORTANT for AI Agents

Before calling this script, you MUST first use Atlas Cloud MCP tools:
1. Call `atlas_list_models` with type="Image" to see all available image models
2. Call `atlas_get_model_info` with the chosen model ID to get its parameter schema
3. Then call `scripts/generate.py generate` with the correct `--model` and parameters
