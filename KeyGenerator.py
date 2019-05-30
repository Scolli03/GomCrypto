import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "abc123"  # This would be an input
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

print(key)
