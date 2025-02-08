# OCR-Image2Text

ocr-image2text is a Python script to extract text from images using the OCR technology. It supports many languages.

## Features

* **language support:** Recognize text in many different languages.
* **Simple CLI tool:** Extract text from images with the command line.
* **Overlay support:** Optionally overlays the OCR result on the image.
* **Error handling:** Clear error messages if the process would fail.

## Supported Languages

- **English (eng)**
- **German (ger)**
- **Spanish (spa)**
- **French (fra)**
- **Italian (ita)**
- **Portuguese (por)**
- **Dutch (nld)**
- **Russian (rus)**
- **Chinese (chi_sim)**
- **Japanese (jpn)**
- **Korean (kor)**
- **Arabic (ara)**
- **Hindi (hin)**
- **Turkish (tur)**
- **And many more!**  

## Installation

### Requirements

- **Python 3.x** 
- **requests** Python library 

### Clone Repository

Clone this repository on your pc:

```bash
git clone https://github.com/thomastschinkel/OCR-ImageToText-AI.git
cd OCR-ImageToText-AI
```

### Dependencies

Install used Python dependencies:

```bash
pip install -r requirements.txt
```

### API Key

To use the OCR API, you need an API key from the website [OCR.space API](https://ocr.space/ocrapi/freekey). Follow the instructions to get the free API key. When you have it, set it in the Code

## Usage

The script will ask for the:

1. **Image path:** Full path to the image you want to extract the text.
2. **Language code:** The language code for OCR AI. For example, 'eng' for English, 'ger' for German, etc. If no one is provided, the default is english.

### Example

```bash
Enter the full path to the image: /path/to/image.png
Enter the language code (example: 'eng', 'ger', 'spa', 'fra'): eng
```

After that, the script will process the image and provide you the Text.

```
=== Result ===
This is the text from the image.
```

## License

This project is licensed with the MIT License, see the [LICENSE](LICENSE) file for more details.


If you have contributions or improvements, please fork the Git or submit a pull request.
