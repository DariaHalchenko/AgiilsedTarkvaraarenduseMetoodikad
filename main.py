logs = []
def liitumine(a, b):
    logs.append('liitumine')
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a+b
print(liitumine(5,'5'))
def lahutamine(a, b):
    logs.append('lahutamine')
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a-b
print(lahutamine(5,5))
def korrutamine(a, b):
    logs.append('korrutamine')
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a*b
print(korrutamine(5,5))
def jagamine(a, b):
    try:
        logs.append('jagamine')
        if isinstance(a,str) or isinstance(b,str):
            print("vale andmed")
            return ""
        return a/b
    except ZeroDivisionError:
        print("ei saa jagada nullile")
print(jagamine(5,5))
def logsKuuvamine(logs):
    jag = 0
    korr = 0
    liit = 0
    lahut = 0
    for elem in logs:
        if elem == 'korrutamine':
            korr +=1
        elif elem == 'lahutamine':
            lahut +=1  
        elif elem == 'jagamine':
            jag +=1
        else:
            liit +=1
    return[korr, lahut, jag, liit]
print(logsKuuvamine(logs))


