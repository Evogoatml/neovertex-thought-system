"""Command line interface for producing ready-to-use NEXUS_FORGE prompts."""

from __future__ import annotations

import argparse
import sys

from .config import ForgeConfig, MODES, OUTPUTS
from .prompt import render_prompt


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="nexus-forge",
        description="Build a configured NEXUS_FORGE v2 prompt. This tool does not call an AI provider.",
    )
    parser.add_argument("--config", help="optional JSON settings file")
    parser.add_argument("--mode", choices=MODES, help="reasoning mode")
    parser.add_argument("--hardening", type=int, choices=range(4), help="hardening level (0-3)")
    parser.add_argument("--output", choices=OUTPUTS, help="response format preference")
    parser.add_argument("--think-depth", type=int, choices=range(1, 6), help="exploration depth (1-5)")
    parser.add_argument("--task", help="optional task text appended as untrusted user input")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        config = ForgeConfig.from_json_file(args.config) if args.config else ForgeConfig()
        overrides = {
            key: value
            for key, value in {
                "mode": args.mode,
                "hardening": args.hardening,
                "output": args.output,
                "think_depth": args.think_depth,
            }.items()
            if value is not None
        }
        config = ForgeConfig(**{**config.__dict__, **overrides})
        sys.stdout.write(render_prompt(config, args.task))
        return 0
    except ValueError as exc:
        parser.error(str(exc))
    return 2
