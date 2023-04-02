# Angecryption

## Whats ?
Angecryption is an encryption or an decryption result from a file to create an other file with the same / or not type. This cryptography approach was created by two researchers **Ange Albertini** and **Axelle Apvrille**.

<img src="./assets/angecryption.png">
-------
## Utility

This tool allows to change the format (pdf, png, jpg ..) with an **decryption** by block with AES Mode CBC.

-----
## Installation

```bash
git clone https://github.com/1sis/Angecryption

cd Angecryption

pip3 install -r requirement.txt
```
------
## Example

```bash
python3 angecryption.py -f input.png -k [KEY] -i [IV] -o flag
```