from PyPDF2 import PdfFileReader, PdfFileWriter
import string
import random

class PDFMerger:

    pdfs_paths = []
    
    def add(self, pdfs_path):
        self.pdfs_paths.append(pdfs_path)

    def merge(self):
        pdf_writer = PdfFileWriter()

        for path in self.pdfs_paths:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        output = '/tmp/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) + '.pdf'

        with open(output, 'wb') as out:
            pdf_writer.write(out)
        
        return output
