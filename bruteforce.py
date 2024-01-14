'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                # Write logic here
                # Iterate through password entries in rockyou.txt
                # Attempt to extract the zip file using each password
                    password = p.strip()
                # Handle correct password extract versus incorrect password attempt
                    if attempt_extract(zf,password):
                        print('[+] Found correct password: %s'% password )
                        exit(0)
                    else:                    
                        print('[-] Incorrect password: %s'% password)
    # Password not found in list
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()


    