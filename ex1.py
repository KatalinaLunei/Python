##Найдите сумму цифр трехзначного числа.
input=int(input("ВВедите трехзначное число:"))
n=input//100
m=(input%100)//10
k=input%10
o=n+m+k
print(o)
