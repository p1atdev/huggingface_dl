# huggingface_dl

A donwload tool for huggingface in CLI.

## Installation

```bash
pip install git+https://github.com/p1atdev/huggingface_dl
```

## Usage

**You need to login by `huggingface-cli login` before use.**

To download [Stability's Stable Diffusion v2.1 checkpoint](https://huggingface.co/stabilityai/stable-diffusion-2-1/blob/main/v2-1_768-ema-pruned.safetensors
):

```bash
hfdl download "https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors"
```

or you can also use

```bash
hfdl dl "https://huggingface.co/stabilityai/stable-diffusion-2-1/blob/main/v2-1_768-ema-pruned.safetensors"
```

To download all ControlNet v1.1 models:

```bash
hfdl download "https://huggingface.co/lllyasviel/ControlNet-v1-1"
```

or

```bash
hfdl download "https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main"
```

To specify output folder:

```bash
hfdl downlaod "https://huggingface.co/spaces/stabilityai/stable-diffusion" --output "./sd"
```

or

```bash
hfdl dl "https://huggingface.co/spaces/stabilityai/stable-diffusion" -o "./sd"
```

See `--help` for details. 
