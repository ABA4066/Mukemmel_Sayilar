print("Mükemmel Sayılar Kendisi Hariç Tam Bölenleri Kendisine Eşit Olan Saylardır\n")
n=int(input("Mükemmel Sayı Olup Olmadığını Kontol Etmek İstediğiniz Sayıyı Girin:\n"))
top=0


for i in range(1,n):
    if n%i==0:
        top += i
if top == n:
    print("{} bir mükemmel sayıdır.".format(n))
else:
    print("{} bir mükemmel sayı değidir.\n".format(n))

