class UnknownFileTypeException(Exception):
    """
    Exception raised when a file is uploaded with an unknown file type
    """
    def __init__(self):
        self.message = 'Unknown file type, please upload a PDF, DOCX, TXT or PPTX file'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
