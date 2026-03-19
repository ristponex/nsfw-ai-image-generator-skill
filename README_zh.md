# 🔞 NSFW AI 图像生成器 Skill

**通过 30+ 模型生成无审查 AI 图像 — Flux、Seedream、Ideogram、Imagen 等**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Models](https://img.shields.io/badge/模型-30+-green.svg)](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)

> 🌍 语言: [English](README.md) | **中文** | [日本語](README_ja.md) | [한국어](README_ko.md)

---

一个 Claude Code 技能，通过 Atlas Cloud API 生成无审查的 NSFW AI 图像。无需本地 GPU，一个 API 即可访问 Flux 2 Pro、Seedream V5、Ideogram V3、Imagen 4 Ultra 等 30+ 主流图像生成模型。

## ✨ 为什么选择这个 Skill？

- 🔓 **无审查生成** — 无内容过滤、无提示词改写，忠实生成你描述的内容
- 🖼️ **30+ 图像模型** — Flux、Seedream、Ideogram、Imagen 等，统一接口调用
- 💰 **最低 $0.003/张** — Flux Schnell 价格极低，按量计费，无订阅
- 🤖 **AI Agent 就绪** — Claude Code 原生技能，AI 自主发现模型并生成图像
- 🔒 **隐私优先** — 不存储提示词和生成图片，不用于模型训练

---

## 📦 安装

### 第 1 步：添加 Skill

```bash
npx skills add ristponex/nsfw-ai-image-generator-skill
```

### 第 2 步：获取 API Key

前往 [Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill) 注册，新账户赠送免费额度，无需绑定信用卡。

### 第 3 步：设置环境变量

**Mac / Linux：**
```bash
export ATLAS_CLOUD_API_KEY=your_api_key_here
```

**Windows (PowerShell)：**
```powershell
$env:ATLAS_CLOUD_API_KEY = "your_api_key_here"
```

**或使用 `.env` 文件：**
```env
ATLAS_CLOUD_API_KEY=your_api_key_here
```

---

## 🖼️ 热门模型

| 模型 | ID | 特点 | 价格 |
|---|---|---|---|
| **Flux 2 Pro** | `black-forest-labs/flux-2-pro` | 综合质量最佳 | ~$0.05/张 |
| **Flux Schnell** | `black-forest-labs/flux-1.1-schnell` | 快速低价 | ~$0.003/张 |
| **Ideogram V3** | `ideogram-ai/ideogram-v3` | 文字渲染最强 | ~$0.04/张 |
| **Imagen 4 Ultra** | `google/imagen-4-ultra` | 照片级真实感 | ~$0.08/张 |
| **Seedream V5** | `bytedance/seedream-v5.0` | 高细节、色彩鲜艳 | ~$0.03/张 |

---

## 🚀 使用方法

### 在 Claude Code 中使用（推荐）

安装技能后，直接向 Claude 描述需求：

```
> 用 Flux Pro 生成一张赛博朋克城市夜景

> 用 Imagen 4 Ultra 生成写实人像

> 用 Seedream 生成 4 张动漫风格插画
```

### 命令行使用

```bash
# 生成图像
uv run scripts/generate.py generate "你的提示词" --model flux-pro

# 指定尺寸
uv run scripts/generate.py generate "宽幅风景" --model flux-pro --size 1920x1080

# 批量生成
uv run scripts/generate.py generate "抽象艺术" --model flux-schnell --count 4

# 查看可用模型
uv run scripts/generate.py models
```

---

## 💰 价格对比

| 平台 | Flux Pro 价格 | 月费 | NSFW 支持 |
|---|---|---|---|
| **Atlas Cloud** | ~$0.05/张 | 按量计费 | ✅ 支持 |
| Midjourney | 不可用 | $10–60/月 | ❌ |
| DALL-E 3 | ~$0.04/张 | 按量计费 | ❌ 审查严格 |
| 本地 Stable Diffusion | 免费 | 需 GPU | ✅ 支持 |

---

## 🔧 本地替代方案

如果你有自己的 GPU，以下是常见的本地无审查方案：

- **Flux Uncensored V2 LoRA** — [HuggingFace](https://huggingface.co/enhanceaiteam/Flux-Uncensored-V2)，需 24GB+ 显存
- **CHROMA** — [lodestones/Chroma](https://huggingface.co/lodestones/Chroma)，Apache 2.0 协议
- **Z-Image-Turbo** — 阿里巴巴开源，6B 参数，推理速度快
- **ComfyUI + Juggernaut XL / Pony Diffusion** — 社区生态丰富
- **Civitai 模型** — 最大的模型仓库，社区评分和预览

**本 Skill 是最简单的方式 — 无需 GPU、无需下载模型、2 分钟即可出图。**

---

## ❓ 常见问题

**免费吗？** 新账户赠送免费额度，之后按量计费，最低 $0.003/张。

**用哪个模型？** 质量选 Flux 2 Pro，省钱选 Flux Schnell，文字选 Ideogram V3。

**能不用 Claude Code 吗？** 可以，`scripts/generate.py` 支持独立命令行运行。

**生成要多久？** Flux Schnell 2-4 秒，Flux Pro 5-15 秒，Imagen 4 Ultra 15-30 秒。

**数据安全吗？** Atlas Cloud 不存储你的提示词和生成图片，不用于模型训练。

**支持什么输出格式？** PNG 或 JPG，取决于模型，脚本自动检测。

---

## 📄 许可证

MIT License — 详见 [LICENSE](LICENSE)。

---

<p align="center">
  <b>2 分钟内开始生成无审查 AI 图像</b><br><br>
  <a href="https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill">获取免费 API Key →</a>
</p>
