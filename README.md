# Document Converter

Welcome to the **Document Converter**! This tool provides a seamless experience for converting documents between various formats with high accuracy and efficiency. Whether you're dealing with PDFs, Word documents, spreadsheets, or images, the Document Converter has you covered.

---

## 🚀 Features

### 🔄 Multi-Format Conversion
- **Input Formats**: PDF, DOCX, XLSX, PNG, JPG, TXT, HTML
- **Output Formats**: PDF, DOCX, XLSX, TXT, HTML, PNG, JPG

### 🌟 Advanced Capabilities
- **Optical Character Recognition (OCR)** for image-based text extraction.
- **Batch Conversion** to handle multiple files at once.
- **Preserves Formatting** to ensure your converted documents look professional.
- **Customizable Options** for resolution, page range, and more.

### 📊 Visualization Tools
- Real-time progress indicators.
- Conversion success/failure statistics.
- Side-by-side comparison of original and converted documents.

---

## 🛠️ Installation

### Prerequisites
- **Python 3.8+**
- Required Libraries: `pandas`, `pytesseract`, `Pillow`, `docx`, `xlsxwriter`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/document_converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd document_converter
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚦 Usage

### Command-Line Interface
Run the following command to convert a document:
```bash
python converter.py --input <input_file> --output <output_file> --format <output_format>
```
Example:
```bash
python converter.py --input example.pdf --output example.docx --format docx
```

### Graphical User Interface (GUI)
Launch the GUI application for a user-friendly experience:
```bash
python gui.py
```
- Drag and drop files for quick processing.
- Configure settings with intuitive sliders and dropdowns.

---

## 🖼️ Screenshots

### Main GUI
![Main Interface](docs/screenshots/main_gui.png)

### Conversion in Progress
![Progress Screen](docs/screenshots/progress_screen.png)

### Side-by-Side Comparison
![Comparison View](docs/screenshots/comparison_view.png)

---

## 🌐 API Integration

Integrate the Document Converter into your existing systems using the REST API.

### Endpoints
#### Convert File
```
POST /convert
```
- **Headers**: `Content-Type: multipart/form-data`
- **Body**: Input file and desired output format.

---

## ⚙️ Configuration

Customize the converter by editing the `config.json` file:
```json
{
    "ocr_language": "eng",
    "max_batch_size": 10,
    "default_output_format": "pdf"
}
```

---

## 🧩 Future Enhancements
- Support for additional formats like ePub and Markdown.
- AI-powered suggestions for optimal output settings.
- Cloud-based conversion for enhanced performance.

---

## 🛡️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Contributions
We welcome contributions! Please fork the repository and submit a pull request. Check the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📞 Support
For issues or feature requests, please open an issue on [GitHub](https://github.com/yourusername/document_converter/issues) or contact us at support@documentconverter.com.

---

**Happy Converting!**

