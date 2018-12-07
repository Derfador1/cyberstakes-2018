#!/usr/bin/env python3

import base64


def func10(var):
    print(92)
    return xorfunc(var, 92)

def func11(var):
	print(222)
	return xorfunc(var, 222)

def func12(o):
    print(26)
    return xorfunc(o, 26)

def func13(o):
    print(183)
    return xorfunc(o, 183)

def func14(o):
    print(245)
    return xorfunc(o, 245)

def func15(o):
    print(254)
    return xorfunc(o, 254)

def func16(o):
    print(161)
    return xorfunc(o, 161)

def func17(o):
    print(196)
    return xorfunc(o, 196)

def func18(o):
    print(38)
    return xorfunc(o, 38)

def func19(o):
    print(200)
    return xorfunc(o, 200)

def func20(o):
    print(194)
    return xorfunc(o, 194)

def func21(o):
    print(170)
    return xorfunc(o, 170)

def func22(o):
    print(43)
    return xorfunc(o, 43)

def func23(o):
    print(104)
    return xorfunc(o, 104)

def func24(o):
    print(103)
    return xorfunc(o, 103)

def func25(o):
    print(253)
    return xorfunc(o, 253)

def func26(o):
    print(152)
    return xorfunc(o, 152)

def func27(o):
    print(183)
    return xorfunc(o, 183)

def func28(o):
    print(215)
    return xorfunc(o, 215)

def func29(o):
    print(221)
    return xorfunc(o, 221)

def func30(o):
    print(97)
    return xorfunc(o, 97)

def func31(o):
    print(60)
    return xorfunc(o, 60)

def func32(o):
    print(197)
    return xorfunc(o, 197)

def func33(o):
    print(145)
    return xorfunc(o, 145)

def func34(o):
    print(74)
    return xorfunc(o, 74)

def one_func_to_rule_them_all(o):
	return xorfunc(o)


def xorfunc(one):
    return [ var_to_chr(x ^ 92 ^ 222 ^ 26 ^ 183 ^ 245 ^ 254 ^ 161 ^ 196 ^ 38 ^ 200 ^ 194 ^ 170 ^ 43 ^ 104 ^ 103 ^ 253 ^ 152 ^ 183 ^ 215 ^ 221 ^ 97 ^ 60 ^ 197 ^ 145 ^ 74) for x in one ]

def var_to_ord(var):
    print("Ord var", var)
    return ord(var)

def var_to_chr(var):
    print(var)
    return chr(var)

def lenfunc(var):
    return len(var)


def joiner(var):
    return ''.join(one_func_to_rule_them_all(var))



#eo = base64.b64encode(bytes(joiner(open("flag.txt", "r").read().strip()), 'utf-8')).decode('utf-8')
#eo = base64.b64decode(bytes(joiner(open("reverse_flag.txt", "r").read().strip()), 'utf-8'))

eo = joiner(base64.b64decode(open("reverse_flag.txt", "rb").read().strip()))


print("The flag has been protected: {}".format(eo))