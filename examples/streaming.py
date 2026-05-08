"""Streaming example — real-time token-by-token output."""

from xalen import XALEN

client = XALEN(api_key="xln_live_your_key_here")

stream = client.chat.completions.create(
    model="vedika-fast",
    messages=[{"role": "user", "content": "Give me a brief birth chart reading for someone born Jan 15, 1990 at 2:30 PM in Mumbai"}],
    stream=True,
    max_tokens=512,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()
