"""Tests for the demo application."""

from src.app import greeting


def test_greeting_uses_supplied_name() -> None:
    assert greeting("Sahil") == "Hello, Sahil! Your CI pipeline is ready."


def test_greeting_strips_whitespace() -> None:
    assert greeting("  Python  ") == "Hello, Python! Your CI pipeline is ready."


def test_greeting_falls_back_for_empty_name() -> None:
    assert greeting("   ") == "Hello, Gitflow! Your CI pipeline is ready."


def test_greeting_default_name() -> None:
    assert greeting() == "Hello, Gitflow! Your CI pipeline is ready."
