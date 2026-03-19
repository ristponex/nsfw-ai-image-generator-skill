# 🔞 NSFW AI Image Generator Skill

**Generate uncensored AI images with 30+ models — Flux, Seedream, Ideogram, Imagen & more**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Models](https://img.shields.io/badge/models-30+-green.svg)](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)

> 🌍 Language: **English** | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

---

A Claude Code skill that generates uncensored NSFW AI images through the Atlas Cloud API. Access 30+ state-of-the-art image generation models — including Flux 2 Pro, Seedream V5, Ideogram V3, Imagen 4 Ultra, and more — without running local GPU hardware or dealing with complex setup.

## ✨ Why This Skill?

### 🔓 Uncensored Generation
No content filters, no prompt rewriting, no invisible safety classifiers silently modifying your output. You write the prompt, the model generates exactly what you describe.

### 🖼️ 30+ Image Models via One API
Switch between Flux, Seedream, Ideogram, Imagen, HunyuanImage, and dozens more without managing separate accounts, API keys, or SDKs. One unified interface for all of them.

### 💰 From $0.003/Image — Cheapest NSFW AI
Flux Schnell starts at roughly $0.003 per image. No monthly subscriptions, no token packs, no minimum spend. You pay only for what you generate.

### 🤖 AI Agent Ready
Built as a Claude Code skill. Your AI agent can discover models, check parameter schemas, and generate images autonomously — no human-in-the-loop required for the API calls.

### 🔒 Privacy First
Images are generated server-side via API and delivered directly to you. No prompts are stored, no generated images are logged, no training on your data.

---

## 📦 Installation

### Step 1: Add the Skill

```bash
npx skills add ristponex/nsfw-ai-image-generator-skill
```

### Step 2: Get Your API Key

Sign up at [Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill) to get a free API key. New accounts include free credits — no credit card required.

### Step 3: Set Environment Variable

**Mac / Linux:**
```bash
export ATLAS_CLOUD_API_KEY=your_api_key_here
```

To persist across sessions, add the line above to your `~/.bashrc`, `~/.zshrc`, or `~/.profile`.

**Windows (PowerShell):**
```powershell
$env:ATLAS_CLOUD_API_KEY = "your_api_key_here"
```

**Windows (CMD):**
```cmd
set ATLAS_CLOUD_API_KEY=your_api_key_here
```

**Or use a `.env` file** in the project root:
```env
ATLAS_CLOUD_API_KEY=your_api_key_here
```

---

## 🖼️ Popular Models

| Model | ID | Quality | Price |
|---|---|---|---|
| **Flux 2 Pro** | `black-forest-labs/flux-2-pro` | Best overall quality | ~$0.05/img |
| **Flux Schnell** | `black-forest-labs/flux-1.1-schnell` | Fast, budget-friendly | ~$0.003/img |
| **Ideogram V3** | `ideogram-ai/ideogram-v3` | Best text rendering | ~$0.04/img |
| **Imagen 4 Ultra** | `google/imagen-4-ultra` | Photorealistic | ~$0.08/img |
| **Seedream V5** | `bytedance/seedream-v5.0` | High detail, vibrant | ~$0.03/img |

> These are the most popular models. Atlas Cloud offers 30+ image models total — run `uv run scripts/generate.py models` or use `atlas_list_models` to see them all.

### Model Selection Guide

| Use Case | Recommended Model | Why |
|---|---|---|
| General high quality | Flux 2 Pro | Best balance of quality and speed |
| Bulk generation on budget | Flux Schnell | $0.003/img, 2-3s per image |
| Images with text/logos | Ideogram V3 | Industry-leading text rendering |
| Photorealistic portraits | Imagen 4 Ultra | Google's best photorealism model |
| Anime / illustration | Seedream V5 | Excellent at stylized content |

---

## 🚀 Usage

### With Claude Code (Recommended)

Once the skill is installed, simply ask Claude to generate images:

```
> Generate a fantasy landscape with dramatic lighting using Flux Pro

> Create a photorealistic portrait with Imagen 4 Ultra

> Generate 4 variations of a cyberpunk cityscape with Seedream
```

Claude will automatically:
1. Look up available models via `atlas_list_models`
2. Check the model's parameter schema via `atlas_get_model_info`
3. Call the generation script with the right parameters
4. Save the output images to your local machine

### Direct CLI Usage

**Generate an image:**
```bash
uv run scripts/generate.py generate "a surreal underwater city with bioluminescent architecture" --model flux-pro
```

**Use a specific model ID:**
```bash
uv run scripts/generate.py generate "portrait of a woman in golden hour light" --model black-forest-labs/flux-2-pro
```

**Set image size:**
```bash
uv run scripts/generate.py generate "wide cinematic landscape" --model flux-pro --size 1920x1080
```

**Set aspect ratio:**
```bash
uv run scripts/generate.py generate "vertical fashion photo" --model ideogram --aspect-ratio 9:16
```

**Generate multiple images:**
```bash
uv run scripts/generate.py generate "abstract art" --model flux-schnell --count 4
```

**Custom output directory:**
```bash
uv run scripts/generate.py generate "your prompt" --model flux-pro -o ./my-images
```

**Pass extra model-specific parameters:**
```bash
uv run scripts/generate.py generate "your prompt" --model flux-pro --extra '{"guidance_scale": 7.5}'
```

**List all available models:**
```bash
uv run scripts/generate.py models
```

### Model Shortcuts

For convenience, you can use short names instead of full model IDs:

| Shortcut | Full Model ID |
|---|---|
| `flux-pro` | `black-forest-labs/flux-2-pro` |
| `flux-schnell` | `black-forest-labs/flux-1.1-schnell` |
| `ideogram` | `ideogram-ai/ideogram-v3` |
| `imagen` | `google/imagen-4-ultra` |
| `seedream` | `bytedance/seedream-v5.0` |

---

## 💰 Price Comparison vs Alternatives

| Platform | Flux Pro | Monthly Cost | NSFW Support | Notes |
|---|---|---|---|---|
| **Atlas Cloud** | ~$0.05/img | Pay per use | ✅ Yes | 30+ models, no subscription |
| Midjourney | N/A | $10–60/mo | ❌ No | Subscription only, censored |
| DALL-E 3 | ~$0.04/img | Pay per use | ❌ No | Heavily censored |
| Stable Diffusion (local) | Free | Need GPU ($500+) | ✅ Yes | Requires setup & hardware |
| RunwayML | N/A | $12–76/mo | ❌ No | Focused on video |
| Leonardo AI | N/A | $10–48/mo | ❌ No | Limited free tier |

### Why Atlas Cloud Wins for NSFW

- **No subscription lock-in** — Pay $0.003–$0.08 per image, nothing more
- **No GPU required** — All rendering happens on cloud infrastructure
- **No censorship** — Generate what you want without prompt policing
- **Model variety** — 30+ models through one API key, switch anytime
- **No waitlists** — Sign up and start generating immediately
- **Free credits on signup** — Test before spending anything
- **API-first design** — Easy to integrate into any workflow or application

---

## 🔧 Local Alternatives

If you prefer running models on your own GPU, here are popular open-source options for uncensored image generation:

### Flux Uncensored V2 LoRA
- **Source:** [enhanceaiteam/Flux-Uncensored-V2](https://huggingface.co/enhanceaiteam/Flux-Uncensored-V2) on HuggingFace
- **Requirements:** 24GB+ VRAM (RTX 4090 or A100)
- **Pros:** High quality, based on Flux architecture
- **Cons:** Requires significant VRAM, LoRA fine-tune only

### CHROMA
- **Source:** [lodestones/Chroma](https://huggingface.co/lodestones/Chroma)
- **License:** Apache 2.0
- **Requirements:** 16GB+ VRAM
- **Pros:** Open license, good general quality
- **Cons:** Less mature than Flux-based models

### Z-Image-Turbo
- **Source:** Alibaba (open source, 6B parameters)
- **Requirements:** 12GB+ VRAM
- **Pros:** Fast inference, smaller model size
- **Cons:** Less photorealistic than larger models

### ComfyUI + NSFW Checkpoints
- **Setup:** [ComfyUI](https://github.com/comfyanonymous/ComfyUI) with models from Civitai
- **Popular checkpoints:**
  - Juggernaut XL — photorealistic, versatile
  - Pony Diffusion V6 XL — anime/stylized
  - RealVisXL — photorealism focused
- **Requirements:** 8GB+ VRAM (SDXL-based)
- **Pros:** Huge community, thousands of LoRAs/checkpoints
- **Cons:** Complex workflow setup, manual model management

### Civitai Models
- **Source:** [civitai.com](https://civitai.com)
- **Pros:** Largest model repository, community ratings, preview images
- **Cons:** Need to download individually, manage versions, run locally

### When to Use Local vs This Skill

| Factor | Local (ComfyUI, etc.) | This Skill (Atlas Cloud) |
|---|---|---|
| Cost per image | Free (after GPU purchase) | $0.003–$0.08 |
| Setup time | Hours–days | 2 minutes |
| GPU required | Yes (8–24GB VRAM) | No |
| Model updates | Manual download | Automatic |
| Batch generation | Limited by VRAM | Unlimited |
| Internet required | No (after setup) | Yes |
| Claude Code integration | Manual | Built-in |

**This skill is the easiest way to generate NSFW AI images — no GPU setup, no model downloads, no dependency hell.** If you already have a powerful GPU and enjoy tinkering, the local options above are great. If you want results in 2 minutes, install this skill.

---

## 🛠️ Requirements

- **Python 3.10+**
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — fast Python package runner
- **Atlas Cloud API key** — [get one free](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)

Dependencies (`requests`, `pillow`) are managed automatically by `uv` — no manual pip install needed.

---

## 📁 Project Structure

```
nsfw-ai-image-generator-skill/
├── SKILL.md              # Skill metadata (used by Claude Code)
├── scripts/
│   └── generate.py       # Main generation script
├── .env.example          # Environment variable template
├── LICENSE               # MIT License
├── README.md             # This file
├── README_zh.md          # 中文说明
├── README_ja.md          # 日本語ドキュメント
└── README_ko.md          # 한국어 문서
```

---

## ❓ FAQ

### Is this free?
New Atlas Cloud accounts get free credits. After that, you pay per image — starting at $0.003 for Flux Schnell. No subscription, no minimum spend.

### Which model should I use?
- **Best quality:** Flux 2 Pro ($0.05/img)
- **Cheapest:** Flux Schnell ($0.003/img)
- **Best text in images:** Ideogram V3 ($0.04/img)
- **Most photorealistic:** Imagen 4 Ultra ($0.08/img)

### Can I use this without Claude Code?
Yes. The `scripts/generate.py` script works standalone via the command line. See the [CLI Usage](#direct-cli-usage) section.

### What image sizes are supported?
Depends on the model. Most support standard sizes like 1024x1024, 1024x1536, 1920x1080, etc. Use `atlas_get_model_info` or check the model's documentation for supported sizes.

### How long does generation take?
- **Flux Schnell:** 2–4 seconds
- **Flux 2 Pro:** 5–15 seconds
- **Ideogram V3:** 10–20 seconds
- **Imagen 4 Ultra:** 15–30 seconds
- **Seedream V5:** 5–15 seconds

### Is my data private?
Yes. Atlas Cloud does not store your prompts or generated images after delivery. No data is used for model training.

### Can I generate any content?
This skill provides uncensored access to image generation models. You are responsible for complying with applicable laws in your jurisdiction. The models will generate what you prompt without content filtering.

### What output formats are supported?
Images are delivered as PNG or JPG depending on the model. The script auto-detects the format from the API response.

### Can I use my own fine-tuned models?
If your model is hosted on Atlas Cloud, yes. Pass the full model ID with the `--model` flag.

### Does this work with other AI coding assistants?
The skill is designed for Claude Code, but the `scripts/generate.py` script is a standalone Python tool. You can call it from any environment that runs Python.

### What happens if a generation fails?
The script will display the error message from the API. Common causes: invalid model ID, unsupported parameters, or insufficient credits. You are not charged for failed generations.

### How do I see all available models?
```bash
uv run scripts/generate.py models
```
Or in Claude Code, ask: "What image models are available on Atlas Cloud?"

---

## 🤝 Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- [Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill) — Get your API key
- [Atlas Cloud Documentation](https://docs.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill) — Full API docs
- [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills) — Learn about skills

---

<p align="center">
  <b>Start generating uncensored AI images in under 2 minutes.</b><br><br>
  <a href="https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill">Get Your Free API Key →</a>
</p>
