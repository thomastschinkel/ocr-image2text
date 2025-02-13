import requests

def ocr_space_api(image_path, language='eng', api_key="K84147669788957", overlay=False):
    """ You can get a Free API Key on https://ocr.space/ocrapi/freekey """
    api_url = 'https://api.ocr.space/parse/image'
    payload = {
        'isOverlayRequired': overlay,
        'apikey': api_key,
        'language': language,
        'scale': True  # Optional, falls gewünscht
    }
    try:
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(api_url, data=payload, files=files, timeout=60)
    except Exception as e:
        return f"Error opening image: {e}"

    try:
        result = response.json()
    except Exception as e:
        return f"Error processing API response: {e}"

    if result.get("IsErroredOnProcessing"):
        error_message = result.get("ErrorMessage", ["Unknown error"])[0]
        return f"OCR error: {error_message}"

    parsed_results = result.get("ParsedResults")
    if parsed_results and len(parsed_results) > 0:
        return parsed_results[0].get("ParsedText")
    else:
        return "No text recognized."

def main():
    print("=== OCR Text Extractor ===")
    print("This tool extracts text from an image using the OCR.space API.")

    image_path = input("Enter the full path to the image: ").strip()
    language_input = input("Enter the language code (example: 'eng', 'ger', 'spa', 'fra'): ").strip().lower()

    language_code = language_input if language_input else 'eng'

    print("\nProcessing image...\n")
    extracted_text = ocr_space_api(image_path, language=language_code)
    print("=== Result ===")
    print(extracted_text)

    save_in_file = input("Want to save the extracted text in a file? Y/N: ").strip().lower()
    if save_in_file == "y":

        import os
        os.makedirs("output", exist_ok=True)
        with open("output/text.txt", "w") as file:
            file.write(extracted_text)
            print("Extracted text was saved in output/text.txt")

if __name__ == '__main__':
    main()
