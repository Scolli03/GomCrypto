import csv

from cryptography.fernet import Fernet

# get key from file
file = open(r"C:\Users\shainc\Desktop\key.txt", 'rb')
key = file.read()
file.close()

# open encrypted file
with open(
        r"\\dc01\layout_reports\AAC - Advanced Airfoil Components\19177-01 (2515 Fired Core)\Turn-Key Elements\Encrypted Files\Datum Points.encrypted",
        'rb') as f:
    data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    decoded = decrypted.decode('utf-8')
    reader = csv.DictReader(decoded)

# Write the encrypted file
# with open(r"C:\Users\shainc\Desktop\CostsDecrypted.csv",'wb') as f:
#     f.write(decrypted)
