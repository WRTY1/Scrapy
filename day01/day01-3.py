def listcalc(list1:list):
    str1 = list1[1]
    if str1 == '+': return int(list1[0])+int(list1[2])
    if str1 == '-': return int(list1[0])-int(list1[2])
    if str1 == '*': return int(list1[0])*int(list1[2])
    if str1 == '/': return int(list1[0])/int(list1[2])

numInput = input('请输入算式:')
numList = list(numInput)
if(len(numList)-1):
    print("计算结果是:",listcalc(numList))
