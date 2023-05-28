from fastapi import File

from api.load_document.pdf_loader import load_pdf
from api.load_document.docx_loader import load_docx
from api.load_document.pptx_loader import load_pptx
from api.load_document.text_loader import load_text

from api.exceptions import UnknownFileTypeException


class DocumentLoader:
    def __init__(self):
        self.file = None
        self.file_type = None
        self.file_content = None

    def load(self, file: str, file_type: str):

        self.file = file
        self.file_type = file_type

        if self.file_type == 'application/pdf':
            self.file_content = load_pdf(self.file)
        elif self.file_type == 'text/plain':
            self.file_content = load_text(self.file)
        elif self.file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            self.file_content = load_docx(self.file)
        elif self.file_type == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
            self.file_content = load_pptx(self.file)
        else:
            raise UnknownFileTypeException()

        return self.file_content
