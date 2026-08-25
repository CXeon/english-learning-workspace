#!/usr/bin/env python3
"""Conservative public-repository checks with no third-party dependencies."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 5 * 1024 * 1024
BLOCKED_PARTS = {"private", ".git", ".env", ".idea", ".vscode", "__pycache__"}
BLOCKED_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".mobileprovision"}
BLOCKED_NAMES = {"id_rsa", "id_dsa", "credentials", "credentials.json"}
ASSET_SUFFIXES = {".aiff", ".wav", ".mp3", ".m4a", ".mp4", ".mov", ".webm"}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "authorization bearer": re.compile(r"Authorization\s*:\s*Bearer\s+\S+", re.I),
}
LESSON_FIELDS = {
    "id:",
    "date:",
    "type:",
    "status:",
    "source_kind:",
    "public_release:",
    "copyright_status:",
    "contains_personal_voice:",
}


def staged_paths() -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / name.decode() for name in result.stdout.split(b"\0") if name]


def working_paths() -> list[Path]:
    return [path for path in ROOT.rglob("*") if path.is_file()]


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def has_blocked_part(path: Path) -> bool:
    return any(part in BLOCKED_PARTS - {".git"} for part in path.parts)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_lesson_metadata(path: Path, text: str, failures: list[str]) -> None:
    if not (path.name == "lesson.md" and "lessons" in path.parts):
        return
    if not text.startswith("---\n"):
        failures.append(f"{relative(path)}: lesson.md must start with YAML front matter")
        return
    front_matter = text.split("---", 2)[1]
    missing = [field for field in LESSON_FIELDS if field not in front_matter]
    if missing:
        failures.append(f"{relative(path)}: missing public metadata: {', '.join(sorted(missing))}")


def check_asset_manifest(path: Path, manifest: str, failures: list[str]) -> None:
    if path.suffix.lower() not in ASSET_SUFFIXES:
        return
    if relative(path) not in manifest:
        failures.append(f"{relative(path)}: binary asset must be listed in assets/asset-manifest.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staged", action="store_true", help="check only staged additions/modifications")
    args = parser.parse_args()

    paths = staged_paths() if args.staged else working_paths()
    failures: list[str] = []
    warnings: list[str] = []
    manifest_path = ROOT / "assets" / "asset-manifest.md"
    manifest = manifest_path.read_text(encoding="utf-8") if manifest_path.exists() else ""

    for path in paths:
        if not path.exists():
            continue
        if ".git" in path.relative_to(ROOT).parts:
            continue
        rel = relative(path)
        if has_blocked_part(path.relative_to(ROOT)):
            failures.append(f"{rel}: blocked private or local path")
            continue
        if path.name in BLOCKED_NAMES or path.suffix.lower() in BLOCKED_SUFFIXES:
            failures.append(f"{rel}: blocked sensitive filename or extension")
        if path.stat().st_size > MAX_BYTES:
            failures.append(f"{rel}: exceeds public binary limit of 5 MB")

        text = read_text(path)
        if text is not None:
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    failures.append(f"{rel}: possible {label}")
            check_lesson_metadata(path, text, failures)
            if "lessons" in path.parts and ("private reflection" in text.lower() or "私人日记" in text):
                warnings.append(f"{rel}: review whether this text is suitable for a public repository")
        check_asset_manifest(path, manifest, failures)

    for warning in warnings:
        print(f"WARN: {warning}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"PASS: public audit checked {len(paths)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
