import os
from web3.auto import w3

foler = ""
file = ""

path = os.path.join(foler, file)
print("path", path)

with open(path) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'account-password')

import binascii
print("This is your Ethereum private key: ")
print(binascii.b2a_hex(private_key))
