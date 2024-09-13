import os

files = os.listdir('D:\\я программист\\pythonProject\\txt\\f')
rewrite = {}
for file in files:
    with open(f"D:\\я программист\\pythonProject\\txt\\f/{file}", encoding='utf-8') as f:
        read_f = f.readlines()
        count = len(read_f)
        rewrite[count] = f"{file}\n{count}\n{"\n".join(read_f)}\n"
with open('end.txt', 'w', encoding='utf-8') as w:
    for key in sorted(rewrite.keys()):
        w.write(rewrite[key])

# with open ('1.txt', encoding = 'utf-8') as file_1:
#     lines_1 = file_1.readlines()
#     num_1 = len(lines_1)
#     str_1 = ' '.join(lines_1)
#
# with open ('2.txt', encoding = 'utf-8') as file_2:
#     lines_2 = file_2.readlines()
#     num_2 = len(lines_2)
#     str_2 = ' '.join(lines_2)
#
# with open ('3.txt', encoding = 'utf-8') as file_3:
#     lines_3 = file_3.readlines()
#     num_3 = len(lines_3)
#     str_3 = ' '.join(lines_3)
#
# with open('end.txt', 'w', encoding = 'utf-8') as f:
#     if num_1 < num_2 and num_1 < num_3:
#         f.write(f'1.txt\n {num_1}\n {str_1}\n')
#     elif num_2 < num_1 and num_2 < num_3:
#         f.write(f'2.txt\n {num_2}\n {str_2}\n')
#     elif num_3 < num_1 and num_3 < num_2:
#         f.write(f'3.txt\n {num_3}\n {str_3}\n')
#
# with open('end.txt', 'a', encoding = 'utf-8') as f:
#     if num_1 > num_2 and num_1 < num_3:
#         f.write(f'1.txt\n {num_1}\n {str_1}\n')
#     elif num_2 > num_1 and num_2 < num_3:
#         f.write(f'2.txt\n {num_2}\n {str_2}\n')
#     elif num_3 > num_1 and num_3 < num_2:
#         f.write(f'3.txt\n {num_3}\n {str_3}\n')
#
# with open('end.txt', 'a', encoding = 'utf-8') as f:
#     if num_1 > num_2 and num_1 > num_3:
#         f.write(f'1.txt\n {num_1}\n {str_1}\n')
#     elif num_2 > num_1 and num_2 > num_3:
#         f.write(f'2.txt\n {num_2}\n {str_2}\n')
#     elif num_3 > num_1 and num_3 > num_2:
#         f.write(f'3.txt\n {num_3}\n {str_3}\n')
