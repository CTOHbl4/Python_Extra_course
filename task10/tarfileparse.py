import io
import sys
import bz2
import gzip
import lzma
import tarfile


s = sys.stdin.read()
s = s.replace(' ', '')
s = s.replace('\n', '')
b = bytes.fromhex(s)

start = b[0]
match start:
    case 253:  # \xfd
        decomp = lzma.decompress(b)
    case 66:  # \x42
        decomp = bz2.decompress(b)
    case 31:  # \x1f
        decomp = gzip.decompress(b)

f = tarfile.open(fileobj=io.BytesIO(decomp), mode='r')
res_count = 0
res_size = 0

for e in f.getmembers():
    if e.isfile():
        res_count += 1
        res_size += e.size

f.close()
print(res_size, res_count)
