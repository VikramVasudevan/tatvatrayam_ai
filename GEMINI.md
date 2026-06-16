# Tatvatrayam AI

## Project Objective
The objective of this project is to extract scripture data from PDF files located in the `data/` folder and save them as text files.

## Data Sources
- `data/tt-part-1.pdf`
- `data/tt-part-2.pdf`
- `data/tt-part-3.pdf`

## Technical Constraints
- The PDFs are not directly copy-pastable (likely scanned images or complex encoding).
- High-fidelity text extraction is required for scripture analysis.

## Workflow
1. **Research:** Completed. Determined that OCR is required due to non-standard encoding in the source PDFs.
2. **Implementation:** Completed. Developed a Python script using `PyMuPDF` and `pytesseract` to process all pages.
3. **Validation:** Completed. Verified that the OCR output correctly captures the Tamil scripture text.

## Results
- Extracted text files are located in the `output/` folder:
  - `output/tt-part-1.txt`
  - `output/tt-part-2.txt`
  - `output/tt-part-3.txt`

## Usage
To re-run the extraction or process new files added to the `data/` folder (with updates to `extract_all.py`):

1. **Install Dependencies:**
   ```bash
   pip install pymupdf pytesseract pillow tqdm
   ```

2. **Run the Script:**
   ```bash
   python extract_all.py
   ```

*Note: Ensure Tesseract OCR is installed on your system with the Tamil (`tam`) language pack.*
