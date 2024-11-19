import hashlib

password = "this-isastrongpassword!09"
# Create a SHA-256 hash object
hash_object = hashlib.sha256()
# Convert the password to bytes and hash it
hash_object.update(password.encode())
# Get the hex digest of the hash
hash_password = hash_object.hexdigest()
print(hash_password)