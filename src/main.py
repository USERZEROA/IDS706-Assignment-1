"""Simple welcome application for IDS 706 Data Engineering."""


def normalize_name(name):
    """Clean a user-provided name and provide a default for empty input."""
    cleaned_name = name.strip()
    return cleaned_name if cleaned_name else "Guest"


def welcome_message(name):
    """Return a welcome message for the provided name."""
    display_name = normalize_name(name)
    return f"{display_name}, welcome to IDS 706 Data Engineering!"


if __name__ == "__main__":
    # Get the user's name and display the generated welcome message.
    name = input("Enter your name: ")
    print(welcome_message(name))
