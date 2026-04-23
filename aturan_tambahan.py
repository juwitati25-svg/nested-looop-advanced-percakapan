total_belanja = int(input("masukan total belanja: "))
ongkir = int(input("masukan ongkir: "))
status_member = input("apakan member premium? true/false: ")
hari = input("masukan hari: ")

status_member = True if status_member == "true" else "false"

cashback = 1

if status_member :
    cashback += 5
elif hari.lower() == "sabtu" :
    cashback += 3
elif cashback > 15:
    cashback = 15

total_pembayaran = total_belanja + ongkir
jumlah_cashback = total_pembayaran * cashback / 100

print("Total Pembayaran: ", total_pembayaran)
print("Persentase cashback: ", cashback,"%")
print("Jumlah cashback: ", jumlah_cashback)

