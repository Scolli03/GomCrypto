from cryptography.fernet import Fernet

# get key from file
file = open(r"C:\Users\shainc\Desktop\key.txt", 'rb')
key = file.read()
file.close()

# open file to encrypt
with open(
        r"\\dc01\layout_reports\AAC - Advanced Airfoil Components\19177-01 (2515 Fired Core)\Turn-Key Elements\Datum Points\Datum Points.csv",
        'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Write the encrypted file
with open(
        r"\\dc01\layout_reports\AAC - Advanced Airfoil Components\19177-01 (2515 Fired Core)\Turn-Key Elements\Encrypted Files\Datum Points.encrypted",
        'wb') as f:
    f.write(encrypted)
