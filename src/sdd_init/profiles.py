"""Scaffold profiles: named, ordered lists of template layers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Profile:
    name: str
    description: str
    layers: tuple[str, ...]


PROFILES = {
    p.name: p
    for p in [
        Profile("full", "Full scaffold: product, architecture, conventions, glossary, ADRs, specs, skills", ("base", "full")),
    ]
}
DEFAULT_PROFILE = "full"


def get_profile(name: str) -> Profile:
    try:
        return PROFILES[name]
    except KeyError:
        valid = ", ".join(PROFILES)
        raise ValueError(f"Unknown profile '{name}'. Valid profiles: {valid}") from None
