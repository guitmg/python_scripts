import os

os.chdir('./files_to_rename')

for file in os.listdir():
    f_name, f_ext = os.path.splitext(file)
    f_head, f_course, f_num = f_name.split('-')
    f_head = f_head.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    f_ext = f_ext.strip()
    final_name = '{}-{}{}'.format(f_num, f_head, f_ext)
    os.rename(file, final_name)

