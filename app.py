"""Small demo app for the Gitflow workflow project."""


def greeting(name: str = "Gitflow") -> str:
    """Return a friendly greeting for a supplied name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        cleaned_name = "Gitflow"
    return f"Hello, {cleaned_name}! Your CI pipeline is ready."


def main() -> None:
    """Run the demo from the command line."""
    print(greeting())


if __name__ == "__main__":
    main()
