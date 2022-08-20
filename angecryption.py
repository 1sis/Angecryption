#!/usr/bin/env python3
#coding: utf-8

from pycryptodomex import AES
import argparse
import os


def main(options):
    options.iv = bytes.fromhex(options.iv)

    if not os.path.exists(options.file):
        print("[!] File %s does not exists or is not readable." % options.file)
        return None
    else:
        fin = open(options.file, "rb")
        fin_bytes = fin.read()
        fin.close()

        aes = AES.new(options.key, AES.MODE_CBC, options.iv)
        decrypted = aes.decrypt(fin_bytes)

    try:
        out = open(options.output, "wb")
        out.write(decrypted)
        out.close()

    except Exception as e:
        print("[!] error with output file {}".format(e))


banner = """
Just a banner .. v1.1
"""


def parseArgs():
    parser = argparse.ArgumentParser(description='d')
    parser.add_argument("-f", "--file", help="file input")
    parser.add_argument("-k", "--key", help="Angecryption Key")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-i", "--iv", help="initialize vector")
    return parser.parse_args()


if __name__ == "__main__" :    
    print(banner)
    options = parseArgs()
    main(options)
