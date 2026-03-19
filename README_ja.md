# 🔞 NSFW AI 画像生成 Skill

**30以上のモデルで無検閲AI画像を生成 — Flux、Seedream、Ideogram、Imagenなど**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Models](https://img.shields.io/badge/models-30+-green.svg)](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)

> 🌍 言語: [English](README.md) | [中文](README_zh.md) | **日本語** | [한국어](README_ko.md)

---

Atlas Cloud APIを通じて無検閲のNSFW AI画像を生成するClaude Codeスキルです。ローカルGPU不要で、Flux 2 Pro、Seedream V5、Ideogram V3、Imagen 4 Ultraなど30以上の画像生成モデルにアクセスできます。

## ✨ 特徴

- 🔓 **無検閲生成** — コンテンツフィルターなし、プロンプト書き換えなし
- 🖼️ **30以上の画像モデル** — 一つのAPIで全モデルにアクセス
- 💰 **$0.003/枚から** — Flux Schnellなら業界最安クラス、従量課金
- 🤖 **AIエージェント対応** — Claude Codeネイティブスキル
- 🔒 **プライバシー重視** — プロンプト・生成画像の保存なし

---

## 📦 インストール

### ステップ1：スキルを追加

```bash
npx skills add ristponex/nsfw-ai-image-generator-skill
```

### ステップ2：APIキーを取得

[Atlas Cloud](https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill)で無料アカウントを作成。新規登録で無料クレジット付与、クレジットカード不要。

### ステップ3：環境変数を設定

**Mac / Linux：**
```bash
export ATLAS_CLOUD_API_KEY=your_api_key_here
```

**Windows (PowerShell)：**
```powershell
$env:ATLAS_CLOUD_API_KEY = "your_api_key_here"
```

---

## 🖼️ 人気モデル

| モデル | ID | 特徴 | 価格 |
|---|---|---|---|
| **Flux 2 Pro** | `black-forest-labs/flux-2-pro` | 最高品質 | ~$0.05/枚 |
| **Flux Schnell** | `black-forest-labs/flux-1.1-schnell` | 高速・低価格 | ~$0.003/枚 |
| **Ideogram V3** | `ideogram-ai/ideogram-v3` | テキスト描画最強 | ~$0.04/枚 |
| **Imagen 4 Ultra** | `google/imagen-4-ultra` | フォトリアル | ~$0.08/枚 |
| **Seedream V5** | `bytedance/seedream-v5.0` | 高精細・鮮明 | ~$0.03/枚 |

---

## 🚀 使い方

### Claude Codeで使用（推奨）

スキルインストール後、Claudeに直接指示：

```
> Flux Proでサイバーパンク都市を生成して

> Imagen 4 Ultraでリアルなポートレートを生成

> Seedreamでアニメ風イラストを4枚生成
```

### コマンドラインで使用

```bash
# 画像生成
uv run scripts/generate.py generate "プロンプト" --model flux-pro

# サイズ指定
uv run scripts/generate.py generate "風景画" --model flux-pro --size 1920x1080

# 複数枚生成
uv run scripts/generate.py generate "抽象アート" --model flux-schnell --count 4

# モデル一覧
uv run scripts/generate.py models
```

---

## 💰 価格比較

| プラットフォーム | Flux Pro | 月額 | NSFW対応 |
|---|---|---|---|
| **Atlas Cloud** | ~$0.05/枚 | 従量課金 | ✅ 対応 |
| Midjourney | 利用不可 | $10–60/月 | ❌ |
| DALL-E 3 | ~$0.04/枚 | 従量課金 | ❌ 検閲あり |
| ローカルSD | 無料 | GPU必要 | ✅ 対応 |

---

## 🔧 ローカル代替手段

自前のGPUがある場合の選択肢：

- **Flux Uncensored V2 LoRA** — [HuggingFace](https://huggingface.co/enhanceaiteam/Flux-Uncensored-V2)、VRAM 24GB以上必要
- **CHROMA** — [lodestones/Chroma](https://huggingface.co/lodestones/Chroma)、Apache 2.0ライセンス
- **Z-Image-Turbo** — Alibaba製、6Bパラメータ、高速推論
- **ComfyUI + Juggernaut XL / Pony Diffusion** — 大規模コミュニティ
- **Civitaiモデル** — 最大のモデルリポジトリ

**このスキルが最も簡単 — GPU不要、モデルDL不要、2分で画像生成開始。**

---

## ❓ よくある質問

**無料ですか？** 新規アカウントに無料クレジット付与。その後は従量課金（$0.003/枚〜）。

**どのモデルがおすすめ？** 品質重視ならFlux 2 Pro、コスト重視ならFlux Schnell、テキスト入りならIdeogram V3。

**生成時間は？** Flux Schnell 2-4秒、Flux Pro 5-15秒、Imagen 4 Ultra 15-30秒。

**データは安全ですか？** Atlas Cloudはプロンプトや生成画像を保存しません。モデル学習にも使用されません。

**Claude Code以外で使えますか？** はい。`scripts/generate.py`はスタンドアロンのPythonスクリプトとしてコマンドラインで実行できます。

**対応出力フォーマットは？** PNGまたはJPG、モデルにより異なります。スクリプトが自動検出します。

**生成に失敗したら？** APIからのエラーメッセージが表示されます。失敗した生成には課金されません。

---

## 📄 ライセンス

MIT License — [LICENSE](LICENSE)を参照。

---

<p align="center">
  <b>2分で無検閲AI画像生成を開始</b><br><br>
  <a href="https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill">無料APIキーを取得 →</a>
</p>
