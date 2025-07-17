class Document:
    def __init__(self, title):
        self.title = title

    def print_preview(self):
        pass

class WordDocument(Document):
    def print_preview(self):
        return f"Previewing Word document: {self.title}"

class PdfDocument(Document):
    def print_preview(self):
        return f"Previewing PDF: {self.title}"

docs = [WordDocument("Report.docx"), PdfDocument("Invoice.pdf")]
for d in docs:
    print(d.print_preview())
