import PyPDF2
import os
import re
from pathlib import Path
from typing import List, Optional, Union
import logging

logger = logging.getLogger(__name__)

class PDFAssert:
    """
    Utility class for PDF file assertions and content validation.
    Provides methods to extract, search, and validate PDF content.
    """

    @staticmethod
    def extract_text(pdf_path: Union[str, Path]) -> str:
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text_content = ""

                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text_content += page.extract_text() + "\n"

                logger.info(f"Successfully extracted text from PDF: {pdf_path}")
                return text_content.strip()

        except Exception as e:
            logger.error(f"Failed to extract text from PDF {pdf_path}: {str(e)}")
            raise Exception(f"Unable to read PDF file: {str(e)}")

    @staticmethod
    def get_page_count(pdf_path: Union[str, Path]) -> int:

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                page_count = len(pdf_reader.pages)
                logger.info(f"PDF {pdf_path} has {page_count} pages")
                return page_count

        except Exception as e:
            logger.error(f"Failed to get page count from PDF {pdf_path}: {str(e)}")
            raise Exception(f"Unable to read PDF file: {str(e)}")

    @staticmethod
    def extract_text_from_page(pdf_path: Union[str, Path], page_number: int) -> str:

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)

                if page_number < 1 or page_number > len(pdf_reader.pages):
                    raise ValueError(f"Invalid page number {page_number}. PDF has {len(pdf_reader.pages)} pages.")

                page = pdf_reader.pages[page_number - 1]  # Convert to 0-based index
                text_content = page.extract_text()

                logger.info(f"Successfully extracted text from page {page_number} of PDF: {pdf_path}")
                return text_content.strip()

        except Exception as e:
            logger.error(f"Failed to extract text from page {page_number} of PDF {pdf_path}: {str(e)}")
            raise Exception(f"Unable to read PDF page: {str(e)}")

    @staticmethod
    def assert_text_exists(pdf_path: Union[str, Path], expected_text: str, case_sensitive: bool = True) -> bool:
        content = PDFAssert.extract_text(pdf_path)

        if not case_sensitive:
            content = content.lower()
            expected_text = expected_text.lower()

        if expected_text in content:
            logger.info(f"Text '{expected_text}' found in PDF: {pdf_path}")
            return True
        else:
            error_msg = f"Text '{expected_text}' not found in PDF: {pdf_path}"
            logger.error(error_msg)
            raise AssertionError(error_msg)

    @staticmethod
    def assert_text_not_exists(pdf_path: Union[str, Path], unexpected_text: str, case_sensitive: bool = True) -> bool:
        content = PDFAssert.extract_text(pdf_path)

        if not case_sensitive:
            content = content.lower()
            unexpected_text = unexpected_text.lower()

        if unexpected_text not in content:
            logger.info(f"Text '{unexpected_text}' correctly not found in PDF: {pdf_path}")
            return True
        else:
            error_msg = f"Unexpected text '{unexpected_text}' found in PDF: {pdf_path}"
            logger.error(error_msg)
            raise AssertionError(error_msg)

    @staticmethod
    def assert_regex_pattern(pdf_path: Union[str, Path], pattern: str, flags: int = 0) -> List[str]:
        content = PDFAssert.extract_text(pdf_path)
        matches = re.findall(pattern, content, flags)

        if matches:
            logger.info(f"Regex pattern '{pattern}' found {len(matches)} matches in PDF: {pdf_path}")
            return matches
        else:
            error_msg = f"Regex pattern '{pattern}' not found in PDF: {pdf_path}"
            logger.error(error_msg)
            raise AssertionError(error_msg)

    @staticmethod
    def assert_page_count(pdf_path: Union[str, Path], expected_pages: int) -> bool:
        actual_pages = PDFAssert.get_page_count(pdf_path)

        if actual_pages == expected_pages:
            logger.info(f"PDF {pdf_path} has correct page count: {expected_pages}")
            return True
        else:
            error_msg = f"PDF {pdf_path} page count mismatch. Expected: {expected_pages}, Actual: {actual_pages}"
            logger.error(error_msg)
            raise AssertionError(error_msg)

    @staticmethod
    def assert_text_on_page(pdf_path: Union[str, Path], page_number: int, expected_text: str, case_sensitive: bool = True) -> bool:
        page_content = PDFAssert.extract_text_from_page(pdf_path, page_number)

        if not case_sensitive:
            page_content = page_content.lower()
            expected_text = expected_text.lower()

        if expected_text in page_content:
            logger.info(f"Text '{expected_text}' found on page {page_number} of PDF: {pdf_path}")
            return True
        else:
            error_msg = f"Text '{expected_text}' not found on page {page_number} of PDF: {pdf_path}"
            logger.error(error_msg)
            raise AssertionError(error_msg)

    @staticmethod
    def get_metadata(pdf_path: Union[str, Path]) -> dict:
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                metadata = {}

                if pdf_reader.metadata:
                    for key, value in pdf_reader.metadata.items():
                        # Remove the leading slash from metadata keys
                        clean_key = key.lstrip('/')
                        metadata[clean_key] = value

                metadata['page_count'] = len(pdf_reader.pages)
                metadata['file_size'] = pdf_path.stat().st_size

                logger.info(f"Successfully extracted metadata from PDF: {pdf_path}")
                return metadata

        except Exception as e:
            logger.error(f"Failed to extract metadata from PDF {pdf_path}: {str(e)}")
            raise Exception(f"Unable to read PDF metadata: {str(e)}")

    @staticmethod
    def search_text_with_context(pdf_path: Union[str, Path], search_text: str, context_chars: int = 50, case_sensitive: bool = True) -> List[dict]:
        content = PDFAssert.extract_text(pdf_path)
        search_content = content if case_sensitive else content.lower()
        search_term = search_text if case_sensitive else search_text.lower()

        matches = []
        start_pos = 0

        while True:
            pos = search_content.find(search_term, start_pos)
            if pos == -1:
                break

            # Calculate context boundaries
            context_start = max(0, pos - context_chars)
            context_end = min(len(content), pos + len(search_text) + context_chars)

            match_info = {
                'position': pos,
                'matched_text': content[pos:pos + len(search_text)],
                'context': content[context_start:context_end],
                'context_start': context_start,
                'context_end': context_end
            }

            matches.append(match_info)
            start_pos = pos + 1

        logger.info(f"Found {len(matches)} occurrences of '{search_text}' in PDF: {pdf_path}")
        return matches