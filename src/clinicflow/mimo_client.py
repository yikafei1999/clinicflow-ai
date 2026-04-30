from __future__ import annotations

import os
from typing import Any, Dict


class MiMoClient:
    """Small placeholder client for future MiMo API integration."""

    def __init__(self, api_key: str | None = None, base_url: str | None = None) -> None:
        self.api_key = api_key or os.getenv("MIMO_API_KEY")
        self.base_url = base_url or os.getenv("MIMO_BASE_URL", "https://platform.xiaomimimo.com")

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def summarize_case(self, prompt: str) -> Dict[str, Any]:
        raise NotImplementedError(
            "MiMo API integration is intentionally stubbed in this prototype. "
            "Replace this method with a real request once API credentials are available."
        )
