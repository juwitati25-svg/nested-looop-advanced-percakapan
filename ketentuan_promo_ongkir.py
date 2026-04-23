belanja = int(input("masukan belanja: "))

if belanja >= 400000:
    print("mendapatkan gratis ongkir 100%")
elif belanja >= 250000:
    print("mendapatkan potongan ongkir 75%")
elif belanja >= 150000:
    print("mendapatkan potongan ongkir 50%")
else:
    print("tidak ada potonagn ongkir")
          