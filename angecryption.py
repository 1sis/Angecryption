#!/usr/bin/env python3
# coding: utf-8
# Python Version    : 3.X
# Authors           : Isis, Nishacid

import argparse
import sys
from Crypto.Cipher import AES
from termcolor import colored

def banner():
    banner = """
      ___                                         _   _             
     / _ \                                       | | (_)            
    / /_\ \_ __   __ _  ___  ___ _ __ _   _ _ __ | |_ _  ___  _ __  
    |  _  | '_ \ / _` |/ _ \/ __| '__| | | | '_ \| __| |/ _ \| '_ \ 
    | | | | | | | (_| |  __/ (__| |  | |_| | |_) | |_| | (_) | | | |
    \_| |_/_| |_|\__, |\___|\___|_|   \__, | .__/ \__|_|\___/|_| |_| 
                  __/ |                __/ | |                      
                 |___/                |___/|_|                      
    By @Isis & @Nishacid
    Version 2.0
    """
    return banner 


# Arguments function
def parseArgs():
    parser = argparse.ArgumentParser(description='This tool allows to change the format (pdf, png, jpg ..) with an decryption by block with AES Mode CBC')
    parser.add_argument("-f", "--file",   help="file input",        required=True)
    parser.add_argument("-k", "--key",    help="Angecryption Key",  required=True)
    parser.add_argument("-o", "--output", help="Output file",       required=True)
    parser.add_argument("-i", "--iv",     help="initialize vector", required=True)
    return parser.parse_args()

def main(options):

    try:
        # Arguments
        decryption_key = options.key
        decryption_iv = bytes.fromhex(options.iv)
        input_file = options.file 
        output_file = options.output
        
        with open(input_file, "rb") as fin:
            fin_bytes = fin.read()
        
        # Decrypt with AES CBC modes
        aes = AES.new(decryption_key.encode("utf-8"), AES.MODE_CBC, decryption_iv)
        decrypted = aes.decrypt(fin_bytes)

        # Write in new file 
        with open(output_file, "wb") as out:
            out.write(decrypted)
        print(colored(f"[+] Successfully write the new file {output_file}", "green"))

    # Check for input file
    except FileNotFoundError:
        print(colored(f"[!] File {input_file} does not exists or is not readable.", "red"))
        sys.exit()

    # Wrong input
    except ValueError:
        print(colored("[!] Please provide an hexadecimal input for the IV", "red"))
        sys.exit()

    # Others errors
    except Exception as e:
        print(colored(f"[!] Error with output file : {e}", "red"))
        sys.exit()
    
if __name__ == "__main__" :
    print(banner())
    options = parseArgs()
    main(options)