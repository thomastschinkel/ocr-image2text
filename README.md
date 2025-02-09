# OCR-Image2Text

ocr-image2text is a Python script that extracts text from images using OCR technology. It uses the OCR.space API and supports many languages.

## Features

* **language support:** Recognize text in many different languages. List below ↓
* **Simple CLI tool:** Extract text from images within the command line.
* **Overlay support:** Optionally overlays the OCR result on the image.
* **Error handling:** Clear error messages if the process would fail.
* **File saving:** Optionally saves the OCR result in a text.txt file.

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
- **And many more..**  

## Installation

### Requirements

- **Python 3.x** 
- **requests** Python library 

### Clone Repository

Clone this repository on your pc:

```bash
git clone https://github.com/thomastschinkel/ocr-image2text.git
cd ocr-image2text
```

### Dependencies

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### API Key

To use the OCR API, you have to get an API key from the website [OCR.space API](https://ocr.space/ocrapi/freekey). Follow the instructions to get the free API key. When you have it, set it in the Code

## Usage

The script will ask for the:

1. **Image path:** Full path to the image you want to extract the text, or just the image file, if the image is in the project folder. 
2. **Language code:** The language code for OCR AI. For example, 'eng' for English, 'ger' for German, etc. If no one is provided, the default is english.

## License

This project is licensed with the MIT License, see the [LICENSE](LICENSE) file for more details.


If you have contributions or improvements, please fork the Git or submit a pull request.
