import argparse
from pykeepass import PyKeePass
from getpass import getpass

def load_passwords(file_path, password):
    kp = PyKeePass(file_path, password=password)
    passwords = {f"{entry.title}:{entry.username}": entry.password for entry in kp.entries if entry.password}
    return passwords

def compare_passwords(file1, password1, file2, password2):
    passwords1 = load_passwords(file1, password1)
    passwords2 = load_passwords(file2, password2)

    only_in_file1 = passwords1.keys() - passwords2.keys()
    only_in_file2 = passwords2.keys() - passwords1.keys()
    in_both = passwords1.keys() & passwords2.keys()

    different_passwords = {
        key: (passwords1[key], passwords2[key])
        for key in in_both
        if passwords1[key] != passwords2[key]
    }

    print(f"Anzahl gleicher Passwörter: {len(in_both) - len(different_passwords)}")
    print(f"\nPasswörter nur in {file1}:")
    for key in only_in_file1:
        print(f"- {key}")

    print(f"\nPasswörter nur in {file2}:")
    for key in only_in_file2:
        print(f"- {key}")

    print("\nUnterschiedliche Passwörter:")
    for key, (pwd1, pwd2) in different_passwords.items():
        print(f"- {key}: {file1} = {pwd1}, {file2} = {pwd2}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vergleiche Passwörter aus zwei KeePass-Datenbanken.")
    parser.add_argument("file1", help="Pfad zur ersten KDBX-Datei")
    parser.add_argument("file2", help="Pfad zur zweiten KDBX-Datei")

    args = parser.parse_args()

    print(f"Bitte Passwort für {args.file1} eingeben:")
    password1 = getpass()

    print(f"Bitte Passwort für {args.file2} eingeben:")
    password2 = getpass()

    compare_passwords(args.file1, password1, args.file2, password2)
