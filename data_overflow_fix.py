# coding:utf-8

import os

os.chdir(r'D:\pys')  # 修改当前工作目录到D:\pys，其中r代表raw string

'''
项目中要求处理大量txt中的数据，数据分为五列，第二至四列中如果有大于1的数据，就将其改为1
背景是分布于[0, 1]的坐标点

代码思路是利用dir *.txt /b >0.txt批处理，将该目录下所有txt文件名写入0.txt中，随后在0.txt中删除“0.txt”行（一般为第一个），剩余的就是所有txt文件的名称
随后，先依次读取0.txt的每行以获得目标待检查txt名称，再逐行读取之，以检测目标txt中是否有数据大于1，有则修改为1，并写入新的字符串中
最后将字符串写入原有txt并覆盖之，即完成了数据的检测与修改
'''

flag = 0  # 定义全局变量flag以显示某txt文件有无溢出数据


def data_fix(s):
    global flag
    flag = 0
    txt1 = open(s, 'r')  # 以只读方式打开文件，文件的指针将会放在文件的开头
    txt1_new = ''  # 新建txt1_new以写入某个txt中的修改后数据
    for line in txt1.readlines():
        line_list = line.split()
        i = 1
        txt1_new = txt1_new + line_list[0] + ' '  # list的第一项不是坐标点，不需要进行判断
        while i < 4:
            if line_list[i] > "1":  # line_list[i]均为字符串，不能和数字1直接比较。字符串之间的比较即为比较二者首位的ascii码
                line_list[i] = "1"
                flag = flag + 1
            txt1_new = txt1_new + line_list[i] + ' '
            i = i + 1
        if line_list[4] > "1":
            line_list[4] = "1"
            flag = flag + 1
        txt1_new = txt1_new + line_list[4] + '\n'  # 列表最后一个数据与下一行之间是\n分隔，因此单独处理
    txt1.close()

    txt1 = open(s, 'w')  # w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，则创建新文件。
    txt1.write(txt1_new)  # 将txt中的全部原有数据用txt1_new代替
    txt1.close()


txt_list = open('0.txt', 'r')
for txt_name in txt_list.readlines():  # 依次读取每行
    txt_name = txt_name.strip()  # 方法x.strip()删去txt_name的头尾两行指定字符，若未指定则默认删除空白符（包括'\n', '\r',  '\t',  ' ')
    # txt_name = txt_name.replace('\n', '')  # 将txt_name中的所有\n替换为''，即删除
    try:
        data_fix(txt_name)
        if flag != 0:
            print(txt_name + "中有" + str(flag) + "个数据错误")
    except:
        print(txt_name + "处理错误！")
txt_list.close()
