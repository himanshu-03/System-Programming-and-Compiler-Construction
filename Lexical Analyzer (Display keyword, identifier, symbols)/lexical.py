import re
keyword = ['break','case','char','const','countinue','default','do','int','else','enum','extern','float','for','goto','if','long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
built_in_functions = ['clrscr()','printf()','scanf()','getch()','main()']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=']
specialsymbol = ['@','#','$','_','!']
separator = [',',':',';','\n','\t','{','}','(',')','[',']']

with open('lexical.c', 'r') as file:
    source_code = file.read()

splitCode = source_code.split() 
length = len(splitCode)    

for i in range(0,length):

    if splitCode[i] in operators:
        print("Operators         --> ",splitCode[i])
        continue
    if splitCode[i] in specialsymbol:
        print("Special Operator  -->",splitCode[i])
        continue
    if splitCode[i] in built_in_functions:
        print("Built_in Function -->",splitCode[i])
        continue
    if splitCode[i] in separator:
        print("Separator         -->",splitCode[i])
        continue
    if re.match(r'(#include*).*', splitCode[i]):
        print ("Preprocessor Directives -->", splitCode[i])
        continue
    if re.match(r'^[-+]?[0-9]+(\.[0-9]+)?$',splitCode[i]):
        print("Numerals          --> ",splitCode[i])
        continue
    if splitCode[i] in keyword:
        print("Keyword           -->",splitCode[i])
        continue
    else:
        print("Identifier        -->",splitCode[i])
