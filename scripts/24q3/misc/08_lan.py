from lingua import Language, LanguageDetectorBuilder


def main():
    languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()

    text_to_detect = "languages are awesome"
    detected_language = detector.detect_language_of(text_to_detect)

    print(f"'{text_to_detect}' is detected as '{detected_language}'")


if __name__ == "__main__":
    main()
