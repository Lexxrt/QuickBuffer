# cSpell: disable
import sys
import base64
import hashlib

menu = '''
~ QuickBuffer | By Lexxrt

Usage:
    ~ Options:
        bin     (Denary To Binary)
        hex     (Denary To Hex)
        b64e    (Base64 Encode)
        b64d    (Base64 Decode)
        MD5     (MD5 Hashing)
        rot13   (Rot13 Encoding)
        SHA-1   (SHA-1 Hashing)
        SHA-224 (SHA-224 Hashing)
        SHA-256 (SHA-256 Hashing)
        SHA-384 (SHA-384 Hashing)
        SHA-512 (SHA-512 Hashing)
        rev     (Reverse String)
        cc      (Char. Count)
        wc      (Word. Count)

Examples:
    - ./quickbuffer.py [OPTION] [DATA]
    - python quickbuffer.py [OPTION] [DATA]
    - python3 quickbuffer.py [OPTION] [DATA]

'''

def main(option: str, value: str):
    if option == 'bin':
        txt2bin = int(value)
        bin_result = bin(txt2bin)[2:]
        print('[+] Output:', bin_result)
    elif option == 'hex':
        bin2hex = hex(int(value))[2:]
        print('[+] Output:', bin2hex)
    elif option == 'b64e':
        b64e = base64.b64encode(value.encode('ascii')).decode()
        print('[+] Output:', b64e)
    elif option == 'b64d':
        b64d = base64.b64decode(value.encode('ascii')).decode()
        print('[+] Output:', b64d)
    elif option == 'MD5':
        md5 = hashlib.md5(value.encode('ascii')).hexdigest()
        print('[+] Output:', md5)
    elif option == 'rot13':
        rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz', 'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
        print('[+] Output', value.translate(rot13))
    elif option == 'SHA-1':
        sha1 = hashlib.sha1(value.encode('ascii')).hexdigest()
        print('[+] Output:', sha1)
    elif option == 'SHA-224':
        sha224 = hashlib.sha224(value.encode('ascii')).hexdigest()
        print('[+] Output:', sha224)
    elif option == 'SHA-256':
        sha256 = hashlib.sha256(value.encode('ascii')).hexdigest()
        print('[+] Output:', sha256)
    elif option == 'SHA-384':
        sha384 = hashlib.sha384(value.encode('ascii')).hexdigest()
        print('[+] Output:', sha384)
    elif option == 'SHA-512':
        sha512 = hashlib.sha512(value.encode('ascii')).hexdigest()
        print('[+] Output:', sha512)
    elif option == 'rev':
        print('[+] Output:', value[::-1])
    elif option == 'cc':
        print('[+] Output:', len(value))
    elif option == 'wc':
        c = 0
        for i in value.split(' '):
            c += 1
        print('[+] Output:', c)
    else:
        print('[!] Invalid Option...')
        exit()


if __name__ == '__main__':
    try:
        option = sys.argv[1]
        data = sys.argv[2]

        main(option, data)
    except:
        print(menu)
