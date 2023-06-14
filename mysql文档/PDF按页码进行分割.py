import os
from PyPDF2 import PdfReader, PdfWriter
import sys
sys.setrecursionlimit(10000000)  # 将递归深度设置为10000

# 按页码分割PDF文件
def split_pdf_by_page(filename, max_pages):
    # 读取PDF文件
    pdf_reader = PdfReader(open(filename, 'rb'))
    # 获取PDF文件总页数
    # num_pages = pdf_reader.getNumPages()
    num_pages = len(pdf_reader.pages)
    # 循环分割PDF文件
    for i in range(0, num_pages, max_pages):
        # 创建一个新的PDF文件写入器
        pdf_writer = PdfWriter()
        # 分割PDF文件
        for j in range(i, min(i+max_pages, num_pages)):
            pdf_writer.add_page(pdf_reader.pages[j])
        # 写入分割后的PDF文件
        output_filename = os.path.splitext(filename)[0] + '_part{}.pdf'.format(i//max_pages+1)
        with open(output_filename, 'wb') as f:
            pdf_writer.write(f)

# 以299页为最大值分割PDF文件
split_pdf_by_page('refman-8.0-en.pdf', 299)
