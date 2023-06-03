from api.split_document.pdf_splitter import split_pdf
from api.split_document.text_splitter import split_text
from api.split_document.docx_splitter import split_docx
from api.split_document.pptx_splitter import split_pptx

from api.exceptions import DocumentSplitException


class DocumentSplitter:
    """DocumentSplitter is a class that splits a document into chunks of text"""

    def __init__(self):
        self.file_type = None
        self.document_content = None
        self.document_chunks = None

    def split(self, document_content: str, document_type: str):
        """
        Split a document into chunks of text
        Args:
            document_content: The content of the document
            document_type: The type of document (e.g. PDF, DOCX, TXT, PPTX)
        Returns:
            A list of text chunks
        """

        self.document_content = document_content
        self.file_type = document_type

        if self.file_type == 'application/pdf':
            document_chunks = split_pdf(self.document_content)
        elif self.file_type == 'text/plain':
            document_chunks = split_text(self.document_content)
        elif self.file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            document_chunks = split_docx(self.document_content)
        elif self.file_type == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
            document_chunks = split_pptx(self.document_content)
        else:
            raise DocumentSplitException()

        return document_chunks
