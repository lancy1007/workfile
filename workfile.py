import os
import glob
import shutil

goal_dir=r"C:\Users\13691\Desktop\file"
mkdir_path=r"C:\Users\13691\Desktop\total"

if not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

file_num = 0
dir_num = 0

for file in glob.glob('{}/**/*'.format(goal_dir), recursive=True):
    if os.path.isfile(file):
        filename = os.path.basename(file)
        if '.' in filename:
            suffix = filename.split('.')[-1]
        else:
            suffix = 'others'
        if not os.path.exists('{}/{}'.format(mkdir_path, suffix)):
            os.mkdir('{}/{}'.format(mkdir_path, suffix))
            dir_num += 1
               # 等价于 dir_num = dir_num + 1
        shutil.copy(file, '{}/{}'.format(mkdir_path, suffix))
        file_num += 1

print('file_num: {}'.format(file_num))
print('dir_num: {}'.format(dir_num))
