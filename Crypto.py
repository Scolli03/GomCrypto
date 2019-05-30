import base64
import csv
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Crypto:
    def __init__(self, location, password):
        self.location = location
        self.password = password
        self.key = self.GenerateKey()

    def GenerateKey(self):
        password_provided = self.password  # This would be an input
        password = password_provided.encode()  # Convert to bytes

        salt = b'\xf2\x9b\xe0\r\xc6t\x9e\xb9\x15<D\xd1V\xda\n\xa5'  # salt generated using os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))  # can only use kdf once

        return key

    def Encrypter(self):
        # open file to encrypt
        for file in os.listdir(self.location):
            with open(os.path.join(self.location, file), 'rb') as f:
                data = f.read()
            print(data)

            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)

            encryptLoc = os.path.join(self.location, "Gom Package")
            if not os.path.exists(encryptLoc):
                os.makedirs(encryptLoc)

            # Write the encrypted file
            with open(os.path.join(self.location, "Gom Package", "{}.encrypted".format(os.path.splitext(file)[0])),
                      'wb') as f:
                f.write(encrypted)

    def Decrypter(self, file, key):
        with open(file, 'rb') as f:
            data = f.read()
            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            decoded = decrypted.decode('utf-8')
            return csv.DictReader(decoded)


if __name__ == '__main__':
    location = r"\\dc01\layout_reports\AAC - Advanced Airfoil Components\19177-01 (2515 Fired Core)\Turn-Key Elements\EncryptMe"
    package = r"\\dc01\layout_reports\AAC - Advanced Airfoil Components\19177-01 (2515 Fired Core)\Turn-Key Elements\Encryptions\Gom Package"
    crypto = Crypto(location, "Pyth0nr0x")

    crypto.Encrypter()

    # DatumPoints = os.path.join(package,"Datum Points.encrypted")
    # InspectionPoints = os.path.join(package,"Inspection Points.encrypted")
    # datumInfo = crypto.Decrypter(DatumPoints,crypto.key)
    # inspectionInfo = crypto.Decrypter(InspectionPoints,crypto.key)
    #
    # for row in datumInfo:
    #     print(row)
    # for row in inspectionInfo:
    #     print(row)
