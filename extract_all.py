import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
from tqdm import tqdm

# If tesseract is not in your PATH, uncomment and set the path:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path, output_path):
    print(f"Processing {pdf_path}...")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    
    with open(output_path, "w", encoding="utf-8") as f:
        for page_num in tqdm(range(total_pages), desc=f"OCR {os.path.basename(pdf_path)}"):
            page = doc.load_page(page_num)
            
            # Render page to an image (increase DPI for better OCR)
            # Matrix(2, 2) means 2x zoom, roughly 144 DPI
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Perform OCR
            text = pytesseract.image_to_string(img, lang='tam')
            
            # Write page header and text
            f.write(f"\n--- Page {page_num + 1} ---\n")
            f.write(text)
            f.write("\n")
            
    doc.close()
    print(f"Finished. Text saved to {output_path}")

def main():
    data_dir = "data"
    output_dir = "output"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    pdf_files = [
        "tt-part-1.pdf",
        "tt-part-2.pdf",
        "tt-part-3.pdf"
    ]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(data_dir, pdf_file)
        output_file = pdf_file.replace(".pdf", ".txt")
        output_path = os.path.join(output_dir, output_file)
        
        if os.path.exists(pdf_path):
            extract_text_from_pdf(pdf_path, output_path)
        else:
            print(f"File not found: {pdf_path}")

if __name__ == "__main__":
    main()
