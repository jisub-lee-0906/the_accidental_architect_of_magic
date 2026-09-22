from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (ROOT / "game" / "script.rpy").read_text(encoding="utf-8")
ASSETS = (ROOT / "game" / "generated_assets.rpy").read_text(encoding="utf-8")


def test_script_scene_and_sprite_names_are_declared():
    declared = set(re.findall(r"^image\s+([^=]+?)\s*=", ASSETS, re.MULTILINE))
    referenced = set(re.findall(r"^\s*(?:scene|show)\s+([A-Za-z0-9_]+)", SCRIPT, re.MULTILINE))
    assert referenced <= declared


def test_script_control_flow_targets_exist():
    labels = set(re.findall(r"^label\s+([A-Za-z0-9_]+):", SCRIPT, re.MULTILINE))
    targets = set(re.findall(r"^\s*(?:jump|call)\s+([A-Za-z0-9_]+)", SCRIPT, re.MULTILINE))
    assert targets <= labels
