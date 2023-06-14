
# 将PDF平均分割成n份

# import os
# from PyPDF2 import PdfReader, PdfWriter
# import sys
# sys.setrecursionlimit(10000000)  # 将递归深度设置为10000
# 
# # 设置输入文件和输出目录
# input_file = 'refman-8.0-en.pdf'
# output_dir = ''
# 
# # 读取输入文件
# with open(input_file, 'rb') as f:
#     pdf_reader = PdfReader(f)
# 
#     # 计算输出文件的数量
#     # num_pages = pdf_reader.getNumPages()
#     num_pages = len(pdf_reader.pages)
#     num_outputs = 6
# 
#     # 分割PDF文件
#     for i in range(num_outputs):
#         start_page = i * (num_pages // num_outputs)
#         end_page = (i + 1) * (num_pages // num_outputs)
#         output_file = os.path.join(output_dir, f'output_{i}.pdf')
#         with open(output_file, 'wb') as out:
#             pdf_writer = PdfWriter()
#             for page in range(start_page, end_page):
#                 pdf_writer.add_page(pdf_reader.pages[page])
#             pdf_writer.write(out)
