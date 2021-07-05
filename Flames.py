print('WELCOME TO THE GAME\n','THIS GAME IS DESIGNED TO CHECK WHETHER YOUR CRUSH LOVES YOU OR NOT\n','THIS GAME IS DESIGNED BY PRIYANSHU')
def nexa(a,z):
    for i in z:
        a.append(i)
        a.remove(i)
def spill(a):
    b=''
    for i in a:
        b+=i
        b+=' '
    b=b.split()
    return b
def rem(a,b):
    c=a.count(b)
    if c>1:
        a.remove(b)
flames={'f':'friends','l':'love','a':'affectionate','m':'marriage','e':'enemy','s':'sibling'}
a=input('ENTER YOUR NAME: ')
b=input('WHATS YOUR CRUSH NAME: ')
a+=b
list=['f','l','a','m','e','s']
a=spill(a)
for i in a:
    rem(a,i)
b=0
while len(list)!=1:
    for i in list:
        b+=1
        if b%len(a)==0:
            d=list.index(i)
            z=list[0:d]
            list.remove(list[d-1])
            nexa(list,z)
            break
print('she/he is your',flames[list[0]])