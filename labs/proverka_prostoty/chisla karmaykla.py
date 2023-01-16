# def primFerma(a,n):
#     if a**(n-1)%n==1:
#         print('правдоподобно простое')
#     else:
#         print('составное')

n=560
a=2
result = a**(n-1)%n
if a**(n-1)%n==1:
    print('залупа')
print(result)

