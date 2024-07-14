"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Create instances of ProgrammingLanguage and display their details."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983)

    languages = [python, ruby, visual_basic, java, cpp]

    print(f"{python}\n{ruby}\n{visual_basic}\n{java}\n{cpp}")

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == '__main__':
    main()

