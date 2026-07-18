import re

pattern = r'^\+373\d{8}$|^00373\d{8}$'

while True:
    numar_telefon = input("Introduceti numarul de telefon in formatul +373XXXXXXXX sau 00373XXXXXXXX: ")

    if re.match(pattern, numar_telefon):
        print(f"Nr de telefon corect: {numar_telefon}")
        break
    else:
        print("Numarul de telefon trebuie sa fie in formatul solicitat!")
