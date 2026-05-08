"""Basic chat completion example using XALEN SDK."""

from xalen import XALEN

client = XALEN(api_key="xln_live_your_key_here")

response = client.chat.completions.create(
    model="vedika-standard",
    messages=[
        {"role": "system", "content": "You are a knowledgeable Vedic astrology assistant."},
        {"role": "user", "content": "What is Gajakesari Yoga and when does it form?"}
    ],
    temperature=0.7,
    max_tokens=1024,
)

print(response.choices[0].message.content)
print(f"\nTokens: {response.usage.total_tokens} | Cost: ${response.usage.total_tokens * 0.0000006:.6f}")
