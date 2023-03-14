# -*- coding: utf-8 -*-
import os


def renameFilesSortedByTime(dirPath=""):
    mlist = []

    # 获得文件名列表
    files = os.listdir(dirPath)

    # 获得名称带时间戳的新文件名列表
    for filename in files:
        # 获得文件的最后修改时间
        createTime = os.path.getmtime(dirPath + filename)

        # 将最后修改时间戳作为文件名的前缀，得到新的文件名，加入列表
        mlist.append(str(int(createTime)) + "-" + filename)

    # 重新给列表排序，这次所有文件按修改时间排序了
    mlist = sorted(mlist)

    # 遍历修改时间戳为序号
    for i in range(len(mlist)):

        # 截取获得原先的文件名
        oldName = mlist[i][11:]

        # 将时间戳部分修改为序号，得到新的文件名
        newName = mlist[i][11:]
        if (i + 1) < 10:
            newName = "00" + str(i + 1) + newName
        elif (i + 1) > 9 and (i + 1) < 100:
            newName = "0" + str(i + 1) + newName
        else:
            newName = str(i + 1) + newName
        # print(newName, oldName)

        # 重命名文件，按修改时间排序并加序号前缀
        os.rename(dirPath + oldName, dirPath + newName)


if __name__ == '__main__':
    renameFilesSortedByTime("./")
    print("Job Done!")
