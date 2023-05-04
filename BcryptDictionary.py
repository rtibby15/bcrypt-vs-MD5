import time
import bcrypt

start_time = time.time()
passwords = ["Rakesh@123"]

for password in passwords:
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    
end_time = time.time()

print(f"The password is {password}")
print(hash)
print(f"Time taken to guess the password: {end_time - start_time}")