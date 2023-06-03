class DocumentSplitException(Exception):
    """
    Exception raised when a file is uploaded with an unknown file type
    """
    def __init__(self):
        self.message = 'Document could not be split'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
