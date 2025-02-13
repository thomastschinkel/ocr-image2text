# OCR-Image2Text

ocr-image2text is a python script recognizing text in images using OCR / OCR.space API. It supports multiple languages.

## Features

* **language support:** Recognize text in many different languages. See the List below ↓
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

To use the OCR-API visit the [OCR.space API](https://ocr.space/ocrapi/freekey) Website. Login and get a free API-Key.

## Usage

The script will ask for the:

1. **Image path:** Full path to the image you want to extract the text, or just the image file, if the image is in the project folder. 
2. **Language code:** The language code for OCR API. For example, 'eng' for English, 'ger' for German, etc. If no one is provided, the default is english.

## License

This project is licensed with the MIT License, see the [LICENSE](LICENSE) file for more details.


If you have contributions or improvements, please fork the Git or submit a pull request.
