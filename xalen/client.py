"""XALEN API Client — OpenAI-compatible wrapper for faith-tech AI infrastructure."""

import os
from typing import Optional
from openai import OpenAI, AsyncOpenAI


class XALEN(OpenAI):
    """Synchronous XALEN client. Drop-in replacement for OpenAI SDK.

    Args:
        api_key: Your XALEN API key (xln_live_...). Falls back to XALEN_API_KEY env var.
        base_url: API endpoint. Defaults to https://api.xalen.io/v1
        **kwargs: All other OpenAI client arguments are supported.

    Example:
        >>> from xalen import XALEN
        >>> client = XALEN(api_key="xln_live_...")
        >>> response = client.chat.completions.create(
        ...     model="vedika-standard",
        ...     messages=[{"role": "user", "content": "Analyze this birth chart..."}]
        ... )
        >>> print(response.choices[0].message.content)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.xalen.io/v1",
        **kwargs
    ):
        api_key = api_key or os.environ.get("XALEN_API_KEY")
        if not api_key:
            raise ValueError(
                "XALEN API key required. Pass api_key= or set XALEN_API_KEY env var. "
                "Get your key at https://xalen.io/dashboard"
            )
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)


class AsyncXALEN(AsyncOpenAI):
    """Async XALEN client for high-throughput applications.

    Same interface as XALEN but with async/await support.

    Example:
        >>> from xalen import AsyncXALEN
        >>> client = AsyncXALEN(api_key="xln_live_...")
        >>> response = await client.chat.completions.create(
        ...     model="vedika-fast",
        ...     messages=[{"role": "user", "content": "Quick horoscope analysis"}]
        ... )
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.xalen.io/v1",
        **kwargs
    ):
        api_key = api_key or os.environ.get("XALEN_API_KEY")
        if not api_key:
            raise ValueError(
                "XALEN API key required. Pass api_key= or set XALEN_API_KEY env var. "
                "Get your key at https://xalen.io/dashboard"
            )
        super().__init__(api_key=api_key, base_url=base_url, **kwargs)
