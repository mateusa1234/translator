from googletrans import LANGUAGES, Translator

def main():
    translator = Translator()
    
    # Print supported languages
    print("Supported languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")
    
    # Prompt user to select source and target languages
    source_lang = input("Enter the source language code: ")
    target_lang = input("Enter the target language code: ")
    text_to_translate = input("Enter the text to translate: ")
    
    # Perform translation
    translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
    
    # Print the translated text
    print(f"Translated text: {translated_text.text}")

if __name__ == "__main__":
    main()
