event = int(input())
def toword(a):
    if a==1: return "one"
    elif a==2: return "two"
    elif a==3: return "thr"
    elif a==4: return "fou"
    elif a==5: return "fiv"
    elif a==6: return "six"
    elif a==7: return "sev"
    elif a==8: return "eig"
    elif a==9: return "nin"
    elif a==0: return "zer"

def tosum(sum):
    num = int(sum)
    if num == 0: return 0
    elif num%9 == 0: return 9
    else: return num%9

for i in range(event):
    a = [x for x in input().split()]
    b = a[0]
    name = a[1]
    d1 = 0
    if "." in b:
        d1 = b.index('.')
    d2 =len(b)
    l =d2-d1
    flag=0
    if (b[0] == '-'):
        flag = 1
        b= b[1:]
    try:
        b=float(b)
        result = True
    except:
        result = False
    if (result == False):
        if (i<t-1):
            print("Invalid")
        else:
            print("Invalid", end = "")
    else:
        sci =  format(b, f".{l}e")
        part = sci.split('e')
        number = part[0].split('.')
        k = int(part[1])
        if(flag == 1): 
            result = "-"
        else: result = ""
        result+= toword(int(number[0])) + "." + toword(tosum(number[1])) + "e"
        if(k>0):
            result+='+'
        elif(k<0):
            result+='-'
        result+ = toword(abs(int(part[1]))) + "@"
        if(k%2 !=0):
            for x in range (0, len(name),2):
                result+=name[x]
        else:
            for x in range (1, len(name),2):
                result+=name[x]
        if (i<t-1):
            print(result)
        else:
            print(result, end= "")