"""Configuration and validation for the NEXUS_FORGE prompt controls."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

MODES = ("quick", "deep", "adversarial", "system_design")
OUTPUTS = ("minimal", "structured", "full")


@dataclass(frozen=True)
class ForgeConfig:
    mode: str = "deep"
    hardening: int = 1
    output: str = "structured"
    think_depth: int = 3

    def __post_init__(self) -> None:
        if self.mode not in MODES:
            raise ValueError(f"mode must be one of: {', '.join(MODES)}")
        if isinstance(self.hardening, bool) or not isinstance(self.hardening, int) or not 0 <= self.hardening <= 3:
            raise ValueError("hardening must be an integer from 0 to 3")
        if self.output not in OUTPUTS:
            raise ValueError(f"output must be one of: {', '.join(OUTPUTS)}")
        if isinstance(self.think_depth, bool) or not isinstance(self.think_depth, int) or not 1 <= self.think_depth <= 5:
            raise ValueError("think_depth must be an integer from 1 to 5")

    @classmethod
    def from_json_file(cls, path: str | Path) -> "ForgeConfig":
        """Load known settings from a JSON object; reject malformed or unknown fields."""
        config_path = Path(path)
        try:
            payload: Any = json.loads(config_path.read_text(encoding="utf-8"))
        except OSError as exc:
            raise ValueError(f"cannot read config file {config_path}: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON in config file {config_path}: {exc.msg}") from exc
        if not isinstance(payload, dict):
            raise ValueError("config file must contain a JSON object")
        allowed = {"mode", "hardening", "output", "think_depth"}
        unknown = sorted(set(payload) - allowed)
        if unknown:
            raise ValueError(f"unknown config key(s): {', '.join(unknown)}")
        try:
            return cls(**payload)
        except TypeError as exc:
            raise ValueError(f"invalid config: {exc}") from exc
