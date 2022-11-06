import zlib, sys
from termcolor import colored,cprint
import os

class Compress:
    def compress(self, filename):
        self.filename_in = filename
        new_file_name = os.path.basename(self.filename_in)
        self.filename_out = 'compress_' + new_file_name
        with open(self.filename_in, mode="rb") as fin, open(self.filename_out, mode="wb") as fout:
            data = fin.read()
            compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
            cprint('Done! Your file is compress_ + your filename', color='green', attrs=['bold','blink'])
            # print(f"Original size: {sys.getsizeof(data)}")
            # # Original size: 1000033
            # print(f"Compressed size: {sys.getsizeof(compressed_data)}")
            # # Compressed size: 1024
            print('doneeeee')
            fout.write(compressed_data)
    def decompress(self, file_compress):
        self.file_compress = file_compress
        main = 'decompress_' + self.file_compress
        with open(self.file_compress, mode="rb") as fin, open(main, mode="wb") as fout:
            data = fin.read()
            decompressed_data = zlib.decompress(data)
            print(f"Compressed size: {sys.getsizeof(data)}")
            # Compressed size: 1024
            print(f"Decompressed size: {sys.getsizeof(decompressed_data)}")

            fout.write(decompressed_data)
            # Decompressed size: 10000
