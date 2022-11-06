from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import os
import sys
from  hashlib import sha256
from pathlib import Path
import os 
from tqdm import tqdm
from termcolor import colored,cprint
from zip import Compress

class Decryption:
    def File_decryption(self):
        cprint('Please input the file you wish to decrypt: ',end=' ', color='red', attrs=['bold','blink'])
        self.filename = input()

        # cprint('Do You want to select the key from file or type? file or type', end='', color='blue',attrs=['bold','blink'])
        # self.option = input('')

        # if self.option.lower() == 'file':
        cprint('input the key file to decrypt: ',end=' ', color='red', attrs=['bold','blink'])
        self.key_file = input()
        cprint('Is the file encrypted with a public key?? True or False:',end=' ', color='red', attrs=['bold','blink'])
        self.public_key = input()
        new_file_name = os.path.basename(self.filename)
        file_in = open(self.filename, "rb")
        file_key = open(self.key_file, "rb") 

        encrypted_file_text = 'decrypted_' + new_file_name
        encrypted_file_object = open(encrypted_file_text, 'wb')

        if self.public_key == 'True':
            private_key = RSA.import_key(open("private.pem").read())
            enc_AES_key = file_key.read()
            nonce, tag,ciphertext = \
            [ file_in.read(x) for x in (16,16,-1) ]

            # Decrypt the session key with the private RSA key
            cipher_rsa = PKCS1_OAEP.new(private_key)
            AES_key = cipher_rsa.decrypt(enc_AES_key)
            # Decrypt the data with the AES session key
            cipher_aes = AES.new(AES_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        elif self.public_key == 'False':
            enc_AES_key = file_key.read()
            nonce, tag, ciphertext = \
            [ file_in.read(x) for x in (16, 16, -1) ]
            # Decrypt the data with the AES session key
            cipher_aes = AES.new(enc_AES_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        else: 
            print('Input must be True or False')
            cprint('Do you want to do it again (y/n):',end = ' ', color='red',attrs=['bold','blink'])

        encrypted_file_object.write(data)
        encrypted_file_object.close()

        d = Compress()
        d.decompress(encrypted_file_text)

    # def Folder_decryption(self):




d = Decryption()
d.File_decryption()