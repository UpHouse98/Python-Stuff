url_to_site = 'http://www.pythonchallenge.com/'

#0
#instead of 0 in url put 2**38
def function0():
    print(2**38)

#1
def function1():
    var = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle.sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.lmu ynnjw ml rfc spj.'
    x = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    y = 'c d e f g h i j k l m n o p q r s t u v w x y z a b'
    print(var.translate(var.maketrans(x, y)))
    var = 'http://www.pythonchallenge.com/pc/def/map.html'
    print(var.translate(var.maketrans(x, y)))
    # ocr

#2
#find rare characters in the mess below:
def function2():
    filem = open('D:\\Learn\\myfile.txt')
    content = filem.read()
    print(set(content))

    a_string = content
    for i in '$^]_}@*[&)(!+#{%\n':
        a_string = a_string.replace(i,'')
    print(a_string)
    # equality

#3




