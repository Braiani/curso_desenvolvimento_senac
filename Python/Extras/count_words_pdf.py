import pdfplumber

def count_table_rows_in_pdf(pdf_path, pages=None):
    count = 0
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if pages and page.page_number < pages[0]:
                continue
            elif pages and page.page_number > pages[1]:
                break

            print(f'Page {page.page_number}')
            tables = page.extract_tables()
            for table in tables:
                count += len(table) - 1  # Subtract 1 to exclude the header row
            
    return count

pdf_path = 'Path/to/file.pdf'
# pages = (2,3)
pages = None
count = count_table_rows_in_pdf(pdf_path, pages=pages)
print(f'There\'re {count} rows in all tables on this PDF.')
print(f'Existem {count} linhas em todas as tabelas dentro desse PDF.')