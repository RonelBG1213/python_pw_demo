import pytest
from pathlib import Path
from main.utils.pdf_assert import PDFAssert
import re

class TestPDFAssertions:

    @pytest.mark.pdf_verification
    def test_pdf_text_exists(self):
        pdf_path = "main/resources/sample_report.pdf"
        PDFAssert.assert_text_exists(pdf_path, "Quality Assurance")
        PDFAssert.assert_text_exists(pdf_path, "Quality Assurance", case_sensitive=False)

    @pytest.mark.pdf_verification
    def test_pdf_page_count(self):
        pdf_path = "main/resources/sample_report.pdf"
        PDFAssert.assert_page_count(pdf_path, expected_pages=11)

    @pytest.mark.pdf_verification
    def test_pdf_text_on_specific_page(self):
        pdf_path = "main/resources/sample_report.pdf"
        PDFAssert.assert_text_on_page(pdf_path, page_number=1, expected_text="Title Page")
        PDFAssert.assert_text_on_page(pdf_path, page_number=2, expected_text="Summary")

    @pytest.mark.pdf_verification
    def test_pdf_regex_pattern(self):
        pdf_path = "main/resources/sample_report.pdf"
        matches = PDFAssert.assert_regex_pattern(pdf_path, r"\d{4}-\d{2}-\d{2}")  # Date pattern
        assert len(matches) > 0, "No dates found in PDF"

    @pytest.mark.pdf_verification
    def test_pdf_text_not_exists(self):
        pdf_path = "main/resources/sample_report.pdf"
        PDFAssert.assert_text_not_exists(pdf_path, "Error")
        PDFAssert.assert_text_not_exists(pdf_path, "CONFIDENTIAL")

    @pytest.mark.pdf_verification
    def test_pdf_metadata_extraction(self):
        pdf_path = "main/resources/sample_report.pdf"

        metadata = PDFAssert.get_metadata(pdf_path)
        assert metadata['page_count'] > 0
        assert 'file_size' in metadata
        print(f"PDF metadata: {metadata}")

    @pytest.mark.pdf_verification
    def test_pdf_search_with_context(self):
        pdf_path = "main/resources/sample_report.pdf"

        matches = PDFAssert.search_text_with_context(pdf_path, "important", context_chars=30)
        for match in matches:
            print(f"Found at position {match['position']}: {match['context']}")

    @pytest.mark.pdf_verification
    def test_pdf_full_text_extraction(self):
        pdf_path = "main/resources/sample_report.pdf"

        full_text = PDFAssert.extract_text(pdf_path)
        assert len(full_text) > 0, "PDF appears to be empty"
        print(f"PDF contains {len(full_text)} characters")

