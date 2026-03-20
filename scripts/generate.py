#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "requests>=2.31",
#   "pillow>=10.0",
# ]
# ///

"""
NSFW AI 图像生成脚本 — 通过 Atlas Cloud API 调用无审查图像模型
支持 Flux Uncensored, Seedream, Z-Image-Turbo, HunyuanImage 等
AI Agent 应先通过 MCP 工具 (atlas_list_models) 查询可用模型
"""

import argparse
import os
import sys
import time
import json
import requests
from pathlib import Path


API_BASE = "https://api.atlascloud.ai/api/v1/model"

# 热门 NSFW 图像模型（仅作参考，实际可传入任意模型 ID）
POPULAR_MODELS = {
    "nano-banana": "google/nano-banana-2/text-to-image",
    "seedream": "bytedance/seedream-v5.0-lite",
    "seedream-v4.5": "bytedance/seedream-v4.5",
    "qwen-image": "alibaba/qwen-image/text-to-image-max",
    "z-image": "z-image/turbo",
    "wan-image": "alibaba/wan-2.6/text-to-image",
}


def get_api_key():
    """获取 API Key"""
    key = os.environ.get("ATLAS_CLOUD_API_KEY") or os.environ.get("ATLASCLOUD_API_KEY")
    if not key:
        for env_file in [".env", os.path.expanduser("~/.env")]:
            if os.path.exists(env_file):
                with open(env_file) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith(("ATLAS_CLOUD_API_KEY=", "ATLASCLOUD_API_KEY=")):
                            key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
            if key:
                break
    if not key:
        print("Error: Atlas Cloud API Key not found")
        print()
        print("Setup:")
        print("  export ATLAS_CLOUD_API_KEY=your_key")
        print()
        print("Get your free API key: https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill")
        print("Free credits included, no credit card required.")
        sys.exit(1)
    return key


def submit_request(model_path, payload, api_key):
    """提交生成请求"""
    url = f"{API_BASE}/{model_path}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    if resp.status_code != 200:
        print(f"API error ({resp.status_code}): {resp.text[:500]}")
        sys.exit(1)
    data = resp.json()
    if data.get("code") and data.get("code") != 200:
        print(f"API error: {data.get('message', 'Unknown error')}")
        sys.exit(1)
    request_id = data.get("data", {}).get("id") or data.get("request_id")
    if not request_id:
        print(f"Unexpected response: {json.dumps(data, indent=2)}")
        sys.exit(1)
    return request_id


def poll_result(request_id, api_key, max_wait=300):
    """轮询生成结果"""
    url = f"{API_BASE}/result/{request_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            resp = requests.get(url, headers=headers, timeout=30)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            time.sleep(3)
            continue
        if resp.status_code != 200:
            time.sleep(3)
            continue
        raw = resp.json()
        data = raw.get("data", raw)
        status = data.get("status", "")
        if status in ("completed", "succeeded"):
            return data.get("outputs") or data.get("output") or []
        if status == "failed":
            error = data.get("error") or data.get("message") or "Unknown error"
            print(f"\nGeneration failed: {error}")
            sys.exit(1)
        elapsed = int(time.time() - start_time)
        print(f"\r  Waiting... {elapsed}s", end="", flush=True)
        time.sleep(3)
    print(f"\nTimeout: no result after {max_wait}s")
    sys.exit(1)


def download_file(url, output_path):
    """下载文件"""
    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)


def cmd_generate(args):
    """生成图像"""
    api_key = get_api_key()
    output_dir = Path(args.output) if args.output else Path("./output")
    output_dir.mkdir(parents=True, exist_ok=True)

    model = POPULAR_MODELS.get(args.model, args.model)

    print(f"  Model: {model}")
    print(f"  Prompt: {args.prompt[:80]}...")

    payload = {"model": model, "prompt": args.prompt}
    if args.size:
        payload["image_size"] = args.size
    if args.aspect_ratio:
        payload["aspect_ratio"] = args.aspect_ratio
    if args.count:
        payload["num_images"] = args.count
    if args.extra:
        payload.update(json.loads(args.extra))

    print("\n  Submitting request...")
    request_id = submit_request("generateImage", payload, api_key)
    print(f"  Request ID: {request_id}")

    outputs = poll_result(request_id, api_key)
    if not outputs:
        print("\nNo images generated")
        sys.exit(1)

    urls = outputs if isinstance(outputs, list) else [outputs]
    print(f"\n  Downloading {len(urls)} image(s)...")
    for i, url in enumerate(urls):
        if isinstance(url, dict):
            url = url.get("url") or str(url)
        ext = ".png" if ".png" in url else ".jpg"
        filename = f"image_{int(time.time())}_{i}{ext}"
        filepath = str(output_dir / filename)
        download_file(url, filepath)
        print(f"  Saved: {filepath}")

    print(f"\nDone! {len(urls)} image(s) saved to {output_dir}")


def cmd_models(args):
    """查询可用模型"""
    print()
    print("=" * 75)
    print("  NSFW AI Image Models via Atlas Cloud")
    print("=" * 75)
    print()
    print("  Popular Image Models:")
    print()
    print(f"  {'Shortcut':<15} {'Model ID':<45}")
    print(f"  {'─'*15} {'─'*45}")
    for name, model_id in POPULAR_MODELS.items():
        print(f"  {name:<15} {model_id}")
    print()
    print("  You can pass ANY model ID with --model.")
    print("  Use Atlas Cloud MCP tools (atlas_list_models) to discover all available models.")
    print()

    print("  Fetching full model list from API...")
    try:
        resp = requests.get("https://api.atlascloud.ai/api/v1/models", timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            models = data.get("data", [])
            image_models = [m for m in models if m.get("type", "").lower() == "image"]
            print(f"  Found {len(image_models)} image models on Atlas Cloud")
            print()
            if image_models:
                print(f"  {'Model ID':<50} {'Name':<30}")
                print(f"  {'─'*50} {'─'*30}")
                for m in image_models[:20]:
                    mid = m.get("model", "")
                    name = m.get("displayName", "")
                    print(f"  {mid:<50} {name:<30}")
                if len(image_models) > 20:
                    print(f"  ... and {len(image_models) - 20} more")
    except Exception:
        print("  Could not fetch model list.")

    print()
    print("  Get your API key: https://www.atlascloud.ai?utm_source=github&utm_campaign=nsfw-ai-image-generator-skill")
    print("  Free credits included. No credit card required.")
    print()


def main():
    parser = argparse.ArgumentParser(description="NSFW AI Image Generator via Atlas Cloud")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("generate", help="Generate an image")
    p.add_argument("prompt", help="Text prompt")
    p.add_argument("--model", default="nano-banana", help="Model ID or shortcut (default: nano-banana)")
    p.add_argument("--size", help="Image size (e.g. 1024x1024)")
    p.add_argument("--aspect-ratio", help="Aspect ratio (e.g. 1:1, 16:9)")
    p.add_argument("--count", type=int, help="Number of images")
    p.add_argument("--extra", help="Extra params as JSON")
    p.add_argument("-o", "--output", help="Output directory")

    sub.add_parser("models", help="List available image models")

    args = parser.parse_args()
    if args.command == "generate":
        cmd_generate(args)
    elif args.command == "models":
        cmd_models(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
