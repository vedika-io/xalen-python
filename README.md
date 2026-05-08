# XALEN Python SDK

The official Python SDK for the XALEN AI API. Drop-in replacement for the OpenAI SDK — just change the base URL.

## Installation

```bash
pip install xalen
```

## Quick Start

```python
from xalen import XALEN

client = XALEN(api_key="xln_live_your_key_here")

response = client.chat.completions.create(
    model="vedika-standard",
    messages=[
        {"role": "user", "content": "What is Shakata Yoga?"}
    ]
)
print(response.choices[0].message.content)
```

## Async Usage

```python
from xalen import AsyncXALEN

client = AsyncXALEN()

response = await client.chat.completions.create(
    model="vedika-fast",
    messages=[{"role": "user", "content": "Analyze my birth chart"}]
)
```

## Environment Variable

Set `XALEN_API_KEY` to avoid passing the key explicitly:

```bash
export XALEN_API_KEY=xln_live_your_key_here
```

## API Base URL

Default: `https://api.xalen.io/v1`

## Documentation

Full API docs: [xalen.io/docs](https://xalen.io/docs)

## License

MIT
