# 数字写入文件
from math import sqrt


# 先定义一个函数，判断素数的函数
def is_prime(n):
    for factor in range(2, int(sqrt(n) + 1)):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('../data/number_1_99.txt', '../data/number_100_999.txt', '../data/number_1000_9999.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print("写入文件时发生错误")

    finally:
        for fs in fs_list:
            fs.close()
    print("操作完成")


if __name__ == "__main__":
    main()
