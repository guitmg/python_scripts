import os

#chance dir to where the files are
os.chdir('./files_to_rename')

for file in os.listdir():
    #spliting the extention from the rest of the file name
    f_name, f_ext = os.path.splitext(file)
    #spliting the parts of the file name
    f_head, f_course, f_num = f_name.split('-')
    #removing empity spaces before and after the object
    f_head = f_head.strip()
    f_course = f_course.strip()
    # here we strip and format the numbers to have two digits
    f_num = f_num.strip()[1:].zfill(2)
    f_ext = f_ext.strip()
    # creating the new file name
    final_name = '{}-{}{}'.format(f_num, f_head, f_ext)
    # renaming the file
    os.rename(file, final_name)

