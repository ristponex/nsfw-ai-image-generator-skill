# 🔞 NSFW AI 이미지 생성기 Skill

**30개 이상의 모델로 무검열 AI 이미지 생성 — Flux, Seedream, Ideogram, Imagen 등**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Models](https://img.shields.io/badge/models-30+-green.svg)](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)

> 🌍 언어: [English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | **한국어**

---

Atlas Cloud API를 통해 무검열 NSFW AI 이미지를 생성하는 Claude Code 스킬입니다. 로컬 GPU 없이 Flux 2 Pro, Seedream V5, Ideogram V3, Imagen 4 Ultra 등 30개 이상의 이미지 생성 모델을 사용할 수 있습니다.

## ✨ 특징

- 🔓 **무검열 생성** — 콘텐츠 필터 없음, 프롬프트 수정 없음
- 🖼️ **30개 이상의 이미지 모델** — 하나의 API로 모든 모델 접근
- 💰 **$0.003/장부터** — Flux Schnell 기준, 종량제 과금
- 🤖 **AI 에이전트 지원** — Claude Code 네이티브 스킬
- 🔒 **프라이버시 우선** — 프롬프트/생성 이미지 저장 없음

---

## 📦 설치

### 1단계: 스킬 추가

```bash
npx skills add ristponex/nsfw-ai-image-generator-skill
```

### 2단계: API 키 발급

[Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)에서 무료 계정 생성. 신규 가입 시 무료 크레딧 제공, 신용카드 불필요.

### 3단계: 환경변수 설정

**Mac / Linux:**
```bash
export ATLAS_CLOUD_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:ATLAS_CLOUD_API_KEY = "your_api_key_here"
```

---

## 🖼️ 인기 모델

| 모델 | ID | 특징 | 가격 |
|---|---|---|---|
| **Flux 2 Pro** | `black-forest-labs/flux-2-pro` | 최고 품질 | ~$0.05/장 |
| **Flux Schnell** | `black-forest-labs/flux-1.1-schnell` | 빠르고 저렴 | ~$0.003/장 |
| **Ideogram V3** | `ideogram-ai/ideogram-v3` | 텍스트 렌더링 최강 | ~$0.04/장 |
| **Imagen 4 Ultra** | `google/imagen-4-ultra` | 포토리얼리스틱 | ~$0.08/장 |
| **Seedream V5** | `bytedance/seedream-v5.0` | 고해상도, 선명 | ~$0.03/장 |

---

## 🚀 사용법

### Claude Code에서 사용 (권장)

스킬 설치 후 Claude에게 직접 요청:

```
> Flux Pro로 사이버펑크 도시 이미지 생성해줘

> Imagen 4 Ultra로 사실적인 인물 사진 생성

> Seedream으로 애니메이션 스타일 일러스트 4장 생성
```

### 커맨드라인 사용

```bash
# 이미지 생성
uv run scripts/generate.py generate "프롬프트" --model flux-pro

# 크기 지정
uv run scripts/generate.py generate "풍경화" --model flux-pro --size 1920x1080

# 여러 장 생성
uv run scripts/generate.py generate "추상 아트" --model flux-schnell --count 4

# 모델 목록 조회
uv run scripts/generate.py models
```

---

## 💰 가격 비교

| 플랫폼 | Flux Pro | 월 비용 | NSFW 지원 |
|---|---|---|---|
| **Atlas Cloud** | ~$0.05/장 | 종량제 | ✅ 지원 |
| Midjourney | 불가 | $10–60/월 | ❌ |
| DALL-E 3 | ~$0.04/장 | 종량제 | ❌ 검열 있음 |
| 로컬 SD | 무료 | GPU 필요 | ✅ 지원 |

---

## 🔧 로컬 대안

자체 GPU가 있는 경우 선택지:

- **Flux Uncensored V2 LoRA** — [HuggingFace](https://huggingface.co/enhanceaiteam/Flux-Uncensored-V2), VRAM 24GB 이상 필요
- **CHROMA** — [lodestones/Chroma](https://huggingface.co/lodestones/Chroma), Apache 2.0 라이선스
- **Z-Image-Turbo** — Alibaba, 6B 파라미터, 빠른 추론
- **ComfyUI + Juggernaut XL / Pony Diffusion** — 대규모 커뮤니티
- **Civitai 모델** — 최대 모델 저장소

**이 스킬이 가장 간편합니다 — GPU 불필요, 모델 다운로드 불필요, 2분 만에 이미지 생성 시작.**

---

## ❓ 자주 묻는 질문

**무료인가요?** 신규 계정에 무료 크레딧 제공. 이후 종량제 ($0.003/장~).

**어떤 모델을 써야 하나요?** 품질: Flux 2 Pro, 비용: Flux Schnell, 텍스트 포함: Ideogram V3.

**생성 시간은?** Flux Schnell 2-4초, Flux Pro 5-15초, Imagen 4 Ultra 15-30초.

**데이터는 안전한가요?** Atlas Cloud는 프롬프트나 생성 이미지를 저장하지 않습니다. 모델 학습에도 사용되지 않습니다.

**Claude Code 없이 사용 가능한가요?** 네. `scripts/generate.py`는 독립적인 Python 스크립트로 커맨드라인에서 실행할 수 있습니다.

**출력 형식은?** PNG 또는 JPG, 모델에 따라 다릅니다. 스크립트가 자동 감지합니다.

**생성 실패 시?** API에서 오류 메시지가 표시됩니다. 실패한 생성에는 요금이 부과되지 않습니다.

---

## 📄 라이선스

MIT License — [LICENSE](LICENSE) 참조.

---

<p align="center">
  <b>2분 만에 무검열 AI 이미지 생성 시작</b><br><br>
  <a href="https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill">무료 API 키 발급 →</a>
</p>
