import hashlib
from passlib.hash import bcrypt

unique_decrypted_password = "Industry@2025"
new_password_md5 = hashlib.md5(unique_decrypted_password.encode()).hexdigest()
new_password_md5 = bcrypt.using(rounds=10, ident="2y").hash(new_password_md5)
print(new_password_md5)
