import PyPDF2
import sys
sys.setrecursionlimit(10000000)  # 将递归深度设置为10000

# 打开要分割的PDF文件
pdf_file = open('refman-8.0-en.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 获取PDF文件的总页数
# num_pages = pdf_reader.getNumPages()
num_pages = len(pdf_reader.pages)
print(num_pages)
# 将PDF文件的前一半页码存储在一个新的PDF文件中
pdf_writer = PyPDF2.PdfWriter()
for page in range(num_pages // 2):
    pdf_writer.add_page(pdf_reader.pages[page])
with open('mysqlfile_part1.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)
    
# 将PDF文件的后一半页码存储在另一个新的PDF文件中
pdf_writer = PyPDF2.PdfWriter()
for page in range(num_pages // 2, num_pages):
    pdf_writer.add_page(pdf_reader.pages[page])
with open('mysqlfile_part2.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)

# 关闭文件
pdf_file.close()
