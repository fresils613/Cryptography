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

        new_file_name = os.path.basename(self.filename)
        file_in = open(self.filename, "rb")

        encrypted_file_text = 'decrypted_' + new_file_name
        encrypted_file_object = open(encrypted_file_text, 'wb')


        private_key = RSA.import_key(open("private.pem").read())
        enc_AES_key,nonce, tag,ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(),16,16,-1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        AES_key = cipher_rsa.decrypt(enc_AES_key)
        # Decrypt the data with the AES session key
        cipher_aes = AES.new(AES_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        encrypted_file_object.write(data)
        encrypted_file_object.close()

        d = Compress()
        d.decompress(encrypted_file_text)

    def Folder_decryption(self):
        cprint('Enter the encryptrd folder path: ',end=' ', color='red', attrs=['bold','blink'])
        self.Directory = input()

        # os.makedirs(self.dir_path, exist_ok=True)
        assert Path(self.Directory).is_dir()
        for new_path in sorted(Path(self.Directory).iterdir(), key=lambda p: str(p).lower()):
            with open(new_path, 'rb') as file_in:
                self.new_file_name = os.path.basename(new_path)   
                encrypted_file_text = 'decrypted_' + self.new_file_name
                encrypted_file_object = open(encrypted_file_text, 'wb')
                
                self.private_key = RSA.import_key(open("private.pem").read())
                self.enc_AES_key,self.nonce, self.tag,self.ciphertext = \
                [file_in.read(x) for x in (self.private_key.size_in_bytes(),16,16,-1) ]

                # Decrypt the session key with the private RSA key
                cipher_rsa = PKCS1_OAEP.new(self.private_key)
                AES_key = cipher_rsa.decrypt(self.enc_AES_key)
                # Decrypt the data with the AES session key
                cipher_aes = AES.new(AES_key, AES.MODE_EAX, self.nonce)
                data = cipher_aes.decrypt_and_verify(self.ciphertext, self.tag)
                encrypted_file_object.write(data)
                encrypted_file_object.close()   

                d = Compress()
                d.decompress(encrypted_file_text)     
