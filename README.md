# Invoice Data Extraction System

A Python-based invoice processing application that extracts structured information from invoice images using OpenCV-based image preprocessing, Tesseract OCR, and regular-expression-based parsing, and stores the extracted records in MySQL.

## Overview

The system automates the extraction of important invoice information from uploaded invoice images.

The processing pipeline is:

Invoice Image
↓
OpenCV Image Preprocessing
↓
Tesseract OCR
↓
Text Extraction
↓
Regex-based Field Extraction
↓
Validation
↓
MySQL Storage

The system extracts the following fields:

- Invoice Number
- Invoice Date
- Vendor Name
- Total Amount

## Features

- Upload invoice images through a Flask web interface
- Image preprocessing using OpenCV
- OCR-based text extraction using Tesseract
- Regex-based extraction of invoice fields
- Support for multiple invoice field-label patterns
- Basic validation of extracted values
- Store extracted invoice data in MySQL
- Display extracted invoice information through an HTML interface

## Technologies Used

- Python
- Flask
- OpenCV
- Tesseract OCR
- Pytesseract
- Regular Expressions
- MySQL
- HTML
- CSS

## Image Processing Pipeline

Invoice images can contain noise, low contrast, small text, or inconsistent backgrounds.

To improve the OCR input, OpenCV is used for preprocessing:

1. Read the invoice image
2. Resize the image
3. Convert the image to grayscale
4. Reduce image noise
5. Apply thresholding to improve text/background separation
6. Apply morphological processing
7. Pass the processed image to Tesseract OCR

This preprocessing is performed before OCR rather than directly passing the original image to Tesseract.

## Data Extraction

The extracted OCR text is processed using regular expressions.

### Invoice Number

The parser supports patterns such as:

- Invoice Number
- Invoice No
- Invoice #

### Invoice Date

The parser supports patterns such as:

- Invoice Date
- Issue Date
- Date

### Total Amount

The parser supports patterns such as:

- Total Amount
- Grand Total
- Amount Due

### Vendor Name

The parser searches the initial lines of the OCR output for company-related keywords such as:

- Pvt
- Ltd
- LLP
- Private
- Technologies
- Solutions
- Corporation
- Inc

If a matching company name is not found, the parser falls back to the first available non-empty line.

## Challenges and Solutions

### 1. Inconsistent Image Quality

Invoice images may contain noise, uneven backgrounds, low contrast, or small text.

**Solution:**  
OpenCV preprocessing is applied before OCR using grayscale conversion, resizing, noise reduction, thresholding, and morphological operations.

### 2. OCR Output Inconsistency

OCR output can vary depending on image quality and invoice formatting.

**Solution:**  
Regex-based parsing is used to identify required fields from the OCR text instead of relying on one exact text format.

### 3. Different Invoice Field Labels

Different invoices may use different labels for the same information.

For example:

- Invoice Number
- Invoice No
- Invoice #

**Solution:**  
Multiple regular-expression patterns are used for each supported field.

### 4. Structured Data Storage

Raw OCR output is unstructured and difficult to use directly.

**Solution:**  
The extracted fields are converted into structured records and stored in MySQL.

## Project Structure

```text
Invoice-Data-Extraction-System/
│
├── app.py
├── db.py
├── requirements.txt
│
├── src/
│   ├── ocr_test.py
│   └── invoice_parse.py
│
├── templates/
│   └── index.html
│
├── data/
│   └── sample_data/
│
└── test/
    └── temp.py
