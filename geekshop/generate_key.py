import hashlib
import random


email = 'test@test.com'


full_salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()
print('full_salt', full_salt)

salt = full_salt[:6]
#salt = '2'
#salt = full_salt


print('salt', salt)

print(email + salt)

activation_key = hashlib.sha1((email + salt).encode('utf8')).hexdigest()

print('activation_key', activation_key)