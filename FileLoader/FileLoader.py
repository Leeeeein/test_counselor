import PyPDF2


def read_pdf_with_pypdf2(file_path):
    with open(file_path, 'rb') as fp:
        read_pdf = PyPDF2.PdfReader(fp)
        number_of_pages = len(read_pdf.pages)
        list_of_pages = []
        for i in range(number_of_pages):
            page = read_pdf.pages[i]
            list_of_pages.append(page.extract_text())
    return list_of_pages

def index_2_pages(page_content):
    dic = {}
    cnt = 0
    for page in page_content:
        dic[cnt] = page
        cnt += 1
    return dic

