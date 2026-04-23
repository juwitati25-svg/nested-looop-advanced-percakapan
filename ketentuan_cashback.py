cashback = int(input("masukan cashback:"))

if cashback >= 300000:
    print("mendapatkan cashback 10%")
elif cashback >= 250000:
    print("mendapatkan cashback 7%")
elif cashback >= 100000:
    print("mendapatkan cashback 5%")
else:
    print("tidak mendapatkan cashback")