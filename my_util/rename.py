import os
import re
from pprint import pprint

class RenameFile:
    '''
        批量重命名文件
        重命名规则是根据传入文件名列表和原文件名列表的信息比对，加入新的信息
        原文件名列表：['a.txt', 'b.txt']
        传入文件名列表：['a,1', 'b,2']
        更改后文件名列表：['a-1.txt', 'b-2.txt']
        例如：a.txt ->  a-1.txt
        dirname: 当前文件路径下的文件夹
    '''

    def __init__(self, dirname):
        self.dirname = dirname

    def get_relative_filename(self, filename):
        '''根据传入文件名获取当前文件相对路径文件名'''
        return os.path.join(self.dirname, filename)

    def get_relative_filenames(self):
        '''获取要重命名的文件名列表'''
        filenames = os.listdir(self.dirname)
        relative_filenames = [
            self.get_relative_filename(name) for name in filenames]
        return relative_filenames

    def rename_to(self, *names):
        '''根据传入的新的文件名列表开始重命名'''
        #relative_filenames = self.get_relative_filenames()
        filenames = os.listdir(self.dirname)
        for filename in filenames:
            filename_noext, ext = filename.rsplit('.', 1)
            for name in names:
                if filename_noext in name:
                    o_filename = self.get_relative_filename(filename)
                    t_filename = self.get_relative_filename(
                        '{}.{}'.format(name, ext))
                    os.rename(o_filename, t_filename)


# 要重命名其下文件的文件夹
rename_dir = 'rename_data'
rename_file = RenameFile(rename_dir)
# 改成以下文件名
##names = [
##    '赵晨曦411002198806262015',
##    '朱之谨411002199801010101',
##]
# 从文件中读取所需要的数据
with open('a.txt', 'r', encoding='utf-8') as f:
    names = f.readlines()
new_names = [re.sub(r'\\n|\\t', '', name) for name in names]
rename_file.rename_to(*new_names)
