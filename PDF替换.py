import PyPDF2
# 原始PDF
pdf_file = open('(替换)word版土建总包合同 表面技术（最终版）.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
page = pdf_reader.pages[149] # 第17页在Python中的索引是16  *
# print(page)
# 替换PDF
insert_file = open('20230530102047.pdf', 'rb')
insert_reader = PyPDF2.PdfReader(insert_file)
insert_page = insert_reader.pages[1]  #  *

# 替换
pdf_writer = PyPDF2.PdfWriter()
# for i in range(pdf_reader.getNumPages()):
for i in range(len(pdf_reader.pages)):
    if i == 149:    #  *
        pdf_writer.add_page(insert_page)
    else:
        pdf_writer.add_page(pdf_reader.pages[i])

output_file = open('(全部替换)word版土建总包合同 表面技术（最终版）.pdf', 'wb')
pdf_writer.write(output_file)
output_file.close()
pdf_file.close()
insert_file.close()


