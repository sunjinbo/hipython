import os
import time


# 需要备份的文件与目录应在一份列表中予以指定
source = 'D:\\sunjinbo\\Pictures'


# 备份必须存储在一个主备份目录中
target_dir = 'D:\\backup'


# 备份文件将打包压缩成 zip 文件
# zip 压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)


# 我们使用在任何 GNU/Linux 或 Unix 发行版中都会默认提供的标准 zip 命令进行打包
zip_command = 'zip -r {0} {1}'.format(target, source)

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

