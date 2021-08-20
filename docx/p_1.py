import re

from docx import Document
file1 = Document('./test.docx')
print(file1)
print(file1.paragraphs[0:2])
for object1 in file1.paragraphs[1:2]:
    print(object1.text)

file2 = Document('./练习2.docx')
count = 0;
for object1 in file2.paragraphs:
    if '徐棚' in object1.text:
        count += 1
    print(object1.text)
print(count)
#读取表格
count_table = 0
for object1 in file2.tables:
    for rows in object1.rows: #按行便利
        for blanks in rows.cells:
            print(blanks.text)
            if "孙兴华"in blanks.text:
                count_table += 1
print(count_table)


file3 = Document('./练习3.docx')
for object1 in file3.paragraphs:
    if object1.style.name == 'Heading 1': #读取一级标题
        print(object1.text)

for object1 in file3.paragraphs:
    if re.match("^Heading \d+$",object1.style.name): #读取全部标题
        print(object1.text)

for object1 in file3.paragraphs:
    if object1.style.name == 'Normal': #读取正文
        print(object1.text)

#读取所有的存在的样式
from docx.enum.style import WD_STYLE_TYPE
from docx import Document
文件 = Document('./练习3.docx')
标题 = 文件.styles
for i in 标题:
    if i.type==WD_STYLE_TYPE.PARAGRAPH:
        print(i.name)


