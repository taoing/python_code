# -*- coding: utf-8 -*-

# 递归: 整数转换为任意禁止字符串

def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]

    else:
        return to_str(n//base, base) + to_str(n%base, base)