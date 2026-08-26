"""Tests for the IDS 706 welcome application."""

from src.main import normalize_name, welcome_message


def test_welcome_message():
    """Verify the standard welcome message."""
    assert welcome_message("Ammy") == "Ammy, welcome to IDS 706 Data Engineering!"


def test_welcome_message_trims_whitespace():
    """Verify that unnecessary whitespace is removed from names."""
    assert (
        welcome_message("  Haiwei  ") == "Haiwei, welcome to IDS 706 Data Engineering!"
    )


def test_welcome_message_empty_name():
    """Verify that an empty name falls back to Guest."""
    assert welcome_message("   ") == "Guest, welcome to IDS 706 Data Engineering!"


def test_normalize_name():
    """Verify name normalization independently."""
    assert normalize_name("  Haiwei  ") == "Haiwei"
