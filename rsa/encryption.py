import os
import sys
from pathlib import Path
import os 
from tqdm import tqdm
from termcolor import colored,cprint
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from hashing import Hashing as HS
from zip import Compress

# Class Declaration
class Encryption:    
    def file_encryption(self):
        try:
            cprint('Enter the file name or Path: ',end=' ', color='blue', attrs=['bold','blink'])
            self.filename = input()
        except (IOError, FileNotFoundError): # Enter if there is any error with the filename/directory name
            cprint('File with name {self.filename} is not found.'.format(self.filename), color='red',attrs=['bold','blink']) # It is used to give the error color red.
            sys.exit(0) # Terminate the code
        try:
            cprint('Enter the Directory Path you wish to save your encrypted Files: use / instead of \  ',end=' ', color='blue', attrs=['bold','blink'])
            self.dir_path = input()
        except (IOError, FileNotFoundError): # Enter if there is any error with the filename/directory name
            cprint('There is a problem with the {self.dir_path} path.'.format(self.filename), color='red',attrs=['bold','blink']) # It is used to give the error color red.
            sys.exit(0) # Terminate the code

        #Compressing the file
        c = Compress()
        c.compress(self.filename)
        # Opening the file
        compress_file = 'compress_' + self.filename
        original_message = open(compress_file, 'rb')
        cprint('Compression Done. Time for encryption ', color='green', attrs=['bold','blink'])


        os.makedirs(self.dir_path, exist_ok=True)	
        encrypted_file_text = 'cipher_' + self.filename #Add cipher to the name of the file (Used to save the cipher text)
        encrypted_file_object = open(os.path.join(self.dir_path,encrypted_file_text),'wb') # opening the file just created and save the result in the folder the user input 
        encrypted_security_text = 'Key_' + self.filename # Add Key to the name of the file (Used to save the key, nonce and tag generated)
        encrypted_security_object = open(os.path.join(self.dir_path,encrypted_security_text),'wb') # open the file just created and save in the folder specify by the user 
        content = original_message.read() # Reading the Plaintext File
        content = bytearray(content) # Converting the content of the file to bit

        AES_key = get_random_bytes(32) # Generating the AES key which is in 256bits (16bytes to bit)
        cipher_aes = AES.new(AES_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(content) # Encrypting the file and generating the Cipher text and the hash digest(hash function)

        cprint('Input the public key file or directory: ',end=' ', color='red', attrs=['bold','blink'])
        receiver = input()
        recipient_key = RSA.import_key(open(receiver).read()) # Public Key of the receiver 
        cipher_rsa = PKCS1_OAEP.new(recipient_key) 
        enc_AES_key = cipher_rsa.encrypt(AES_key) # Using the recipient public key to encrypt the Aes Key 

        # encrypted_security_object.write(enc_AES_key) # Storing our cipher text in a file           
        [encrypted_file_object.write(x) for x in (enc_AES_key,cipher_aes.nonce, tag, ciphertext)]

        encrypted_file_object.close() 
        encrypted_security_object.close()
        return 
        
    def folder_encryption(self):
        try:
            cprint('Enter the folder part your wish to encrypts(use / instead of \ ): ',end=' ', color='blue', attrs=['bold','blink'])
            self.Directory = input()
        except (IOError, FileNotFoundError):
            cprint('There is an error with the directory: ',end=' ', color='red', attrs=['bold','blink'])
            sys.exit(0)
        try:
            cprint('Enter the Directory Path you wish to save your encrypted Files(use / instead of \ ):  ',end=' ', color='blue', attrs=['bold','blink'])
            self.dir_path = input()
        except (IOError, FileNotFoundError): # Enter if there is any error with the filename/directory name
            cprint('There is a problem with the {self.dir_path} path.'.format(self.filename), color='red',attrs=['bold','blink']) # It is used to give the error color red.
            sys.exit(0) # Terminate the code
        # self.hash = sha256()

        

        cprint('Please enter the recepient public key file name or path with the correct file extention (use / instead of \ ):  ',end=' ', color='blue', attrs=['bold','blink'])
        self.receiver = input()
        os.makedirs(self.dir_path, exist_ok=True)
        assert Path(self.Directory).is_dir()
        for new_path in sorted(Path(self.Directory).iterdir(), key=lambda p: str(p).lower()):
            with open(new_path, 'rb') as p:
                new_file_name = os.path.basename(new_path)
                #Compressing the file
                c = Compress()
                c.compress(new_path)
                # Opening the file
                cprint('Compression Done. Time for encryption ', color='green', attrs=['bold','blink'])

                
                encrypted_path_text = 'cipher_' + new_file_name  #Add cipher to the name of the file 
                
                
                recipient_key = RSA.import_key(open(self.receiver).read()) # Public Key of the receiver 
                AES_key_generate = get_random_bytes(32) # Generating the AES key which is in 128bits (i6bytes to bit)

                rsa_cipher = PKCS1_OAEP.new(recipient_key) 
                enc_AES_key = rsa_cipher.encrypt(AES_key_generate) # Using the recipient public key to encrypt the Aes Key

                compress_file = 'compress_' + new_file_name
                original_message = open(compress_file, 'rb')
                textFile = original_message.read() # Reading the Plaintext File
                textFile = bytearray(textFile) # Converting the content of the file to bit

                aes_cipher = AES.new(AES_key_generate, AES.MODE_EAX)
                ciphertext, tag = aes_cipher.encrypt_and_digest(textFile) # Encrypting thr file and generating the Cipher text and the hash digest(hash function)
                encrypted_path_object = open(os.path.join(self.dir_path,encrypted_path_text), 'wb') # opening the file just created 
                [ encrypted_path_object.write(x) for x in (enc_AES_key, aes_cipher.nonce, tag, ciphertext) ] # Storing our result in a file
                encrypted_path_object.close() 
        return 
        
