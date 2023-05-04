import time
import hashlib

start_time = time.time()
passwords = ["Rakesh@123"]


for password in passwords:
    hash_object = hashlib.md5(password.encode())
    guess_hash = hash_object.hexdigest()
end_time = time.time()

print(f"The password is {password}")
print(guess_hash)
print(f"Time taken to guess the password: {end_time - start_time}")