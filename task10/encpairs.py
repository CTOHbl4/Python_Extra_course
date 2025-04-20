from itertools import product
import sys


encs = ('KOI8-R', 'CP1251', 'MACCYRILLIC', 'CP866', 'ISO-8859-5', 'CP855')

zimbabve = {name: 'Зимбабве'.encode(name) for name in encs}

s = sys.stdin.buffer.read()

for dec, enc, res_dec in product(encs, encs, encs):
    try:
        check = s.decode(dec).encode(enc)
        if zimbabve[res_dec] in check:
            print(check.decode(res_dec))
            break
    except (UnicodeDecodeError, UnicodeEncodeError):
        continue
