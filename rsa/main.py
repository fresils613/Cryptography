import os
import sys
from pathlib import Path
import os 
from tqdm import tqdm
from termcolor import colored,cprint
# from hashing import Hashing as HS
from zip import Compress
from encryption import Encryption
from decryption import Decryption
from generate_rsa import Generate_RSA


space_count = 30 * ' '
cprint('{} File Encryption And Decryption Tool. {}'.format(space_count,space_count), 'red')
cprint('{} {}'.format(space_count + 3 * ' ','Programmed by Paul ogunniyi.'),'green')
while True:
    cprint('1. Genrate RSA key',color='magenta')
    cprint('2. Encryption',color='magenta')
    cprint('2. Decryption', color='magenta')
    cprint('3. Exit', color='red')
    cprint('~Python3:',end=' ', color='green')
    choice = int(input())

    if choice == 1:
        rsa = Generate_RSA()
        rsa.generate_rsa()
    if choice == 2:
        logo = '''  ___                       _   _          
 | __|_ _  __ _ _ _  _ _ __| |_(_)___ _ _  
 | _|| ' \/ _| '_| || | '_ \  _| / _ \ ' \ 
 |___|_||_\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        cprint(logo, color='red', attrs=['bold'])
        enc = Encryption()
        cprint('What do you want to encrypt', color='magenta')
        cprint('1.Single File',color='magenta')
        cprint('2. Folder', color='magenta')
        cprint('3. Exit', color='red')
        cprint('~Python3:',end=' ', color='green')
        option = int(input())
        if option == 1:
            enc.file_encryption()
        elif option == 2:
            enc.folder_encryption()
        elif option == 3:
            sys.exit()
        else:
            print('Choice not available')

    elif choice == 3:
        logo = '''  ___                       _   _          
 |   \ ___ __ _ _ _  _ _ __| |_(_)___ _ _  
 | |) / -_) _| '_| || | '_ \  _| / _ \ ' \ 
 |___/\___\__|_|  \_, | .__/\__|_\___/_||_|
                  |__/|_|                  '''
        cprint(logo, color='red', attrs=['bold'])
        dec = Decryption()
        cprint('What do you want to encrypt', color='magenta')        
        cprint('1.Single File',color='magenta')
        cprint('2. Folder', color='magenta')
        cprint('3. Exit', color='red')
        cprint('~Python3:',end=' ', color='green')
        option = int(input())
        if option == 1:
            dec.File_decryption()
        elif option == 2:
            dec.Folder_decryption()
        elif option == 3:
            sys.exit()
        else:
            print('Choice not available')
