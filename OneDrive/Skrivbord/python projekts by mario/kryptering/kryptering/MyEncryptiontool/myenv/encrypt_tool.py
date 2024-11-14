import argparse
from cryptography.fernet import Fernet

# Funktion för att skapa en krypteringsnyckel och spara den i en fil
def generate_key():
    key = Fernet.generate_key()  # Generera en krypteringsnyckel med Fernet
    with open("secret.key", "wb") as key_file:  # Öppna en fil för att spara nyckeln
        key_file.write(key)  # Skriv nyckeln till filen
    print("Key has been generated and saved to secret.key")  # Skriv ut ett bekräftelsemeddelande

# Funktion för att kryptera en fil med den sparade nyckeln
def encrypt_file(filename):
    with open("secret.key", "rb") as key_file:  # Läs nyckeln från filen
        key = key_file.read()
    fernet = Fernet(key)  # Skapa ett Fernet-objekt med nyckeln
    with open(filename, "rb") as file:  # Öppna filen som ska krypteras
        original = file.read()
    encrypted = fernet.encrypt(original)  # Kryptera filens innehåll
    with open(filename + ".enc", "wb") as enc_file:  # Öppna/skapa en fil för att spara den krypterade datan
        enc_file.write(encrypted)  # Skriv den krypterade datan till filen
    print(f"File {filename} has been encrypted.")  # Skriv ut ett meddelande om att filen har krypterats

# Funktion för att dekryptera en fil med den sparade nyckeln
def decrypt_file(filename):
    with open("secret.key", "rb") as key_file:  # Läs nyckeln från filen
        key = key_file.read()
    fernet = Fernet(key)  # Skapa ett Fernet-objekt med nyckeln
    with open(filename, "rb") as enc_file:  # Öppna den krypterade filen
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)  # Dekryptera filens innehåll
    with open(filename.replace(".enc", ""), "wb") as dec_file:  # Öppna/skapa en fil för att spara det dekrypterade innehållet
        dec_file.write(decrypted)  # Skriv det dekrypterade innehållet till filen
    print(f"File {filename} has been decrypted.")  # Skriv ut ett meddelande om att filen har dekrypterats

# Konfigurera argparse för att hantera kommandoradsargument
parser = argparse.ArgumentParser(description="Enkelt verktyg för filkryptering/avkryptering")
parser.add_argument("action", choices=["generate", "encrypt", "decrypt"], help="aktionen som ska utföras: generate, encrypt eller decrypt")
parser.add_argument("--file", help="filen att kryptera eller avkryptera")

args = parser.parse_args()

# Utför den angivna åtgärden baserat på kommandoradsargumenten
if args.action == "generate":
    generate_key()
elif args.action in ["encrypt", "decrypt"] and args.file:
    if args.action == "encrypt":
        encrypt_file(args.file)
    elif args.action == "decrypt":
        decrypt_file(args.file)
else:
    print("Fel: Fil saknas för kryptering/avkryptering.")



import os

def encrypt_file(filename):
    if not os.path.exists(filename):
        print(f"Filen {filename} finns inte. Kontrollera sökvägen och försök igen.")
        return
# Fortsätt med krypteringen om filen inte finns

#så kör jag koden 
#python encrypt_tool.py generate
#python encrypt_tool.py encrypt --file stop.txt  #(stop.txt är min file name)
#python encrypt_tool.py decrypt --file stop.txt.enc
