# encoding=utf-8

"""
json格式文件操作:读取、写入、解析定位
author：LBL
date:2023-2-9
"""
import csv  # python使用csv类操作csv文件


def write_csv(f_name):
    """ 写入列表到csv文件,row写入一行，rows写入多行 """
    with open(f_name, "w", newline="") as f:            # 1、打开csv文件，需要指定newline为空不然会多换一行
        csv_writer = csv.writer(f)                      # 2、创建csv.writer对象，指定该文件对象
        # writerow一次写一行
        csv_writer.writerow(["name", "age", "city"])    # 写入表头
        csv_writer.writerow(["zhangsan", 1, "NJ"])      # 写入数据
        # writerows()可一次写多行数据
        data = [("z1", 2, "NJ"),("z2", 3, "NJ"),("z3", 4, "NJ")]
        csv_writer.writerows(data)


def read_csv():
    """ 读取csv文件，转化为列表 """
    with open("b.csv", "r") as f:        # 1、打开csv文件
        csv_reader = csv.reader(f)          # 2、创建csv.reader对象，指定该文件对象
        my_list = list(csv_reader)          # 3、将csv.reader对象转换为列表，每行为一个列表元素
        print(my_list)                      # 4、打印列表
        # [['name', 'age', 'gender'], ['zhangsan', '10', '1'], ['lisi', '13', '1'], ['cuihua', '24', '0']]


# 程序主入口
if __name__ == "__main__":
    # csv文件又称逗号分隔符文件，是一种常见的简单的文件格式。可用excel或文本编辑器txt打开
    write_csv("b.csv")
    read_csv()


    # 了解：字典格式也可直接写入csv文件，DicWriter
    csv_header = ['no', 'language', 'score', 'grade']
    csv_data = [
        {'no': '1', 'language': 'python', 'score': '100', 'grade': 'A'},
        {'no': '2', 'language': 'php', 'score': '96', 'grade': 'B'},
        {'no': '3', 'language': 'java', 'score': '98', 'grade': 'A+'}
    ]
    with open("c.csv", 'w', newline="") as f:
        f_csv = csv.DictWriter(f, csv_header)
        # 写入头部，注意是writeheader()
        f_csv.writeheader()
        # 写入数据，注意是rows()
        f_csv.writerows(csv_data)
        print('写入完成！')



