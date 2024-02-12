# Python-Cybersecurity-Bruteforce-zipfile
> This project is based on cybersecurity program offered by AIG on Forage. For full information, please visit this [link](https://www.theforage.com/simulations/aig/cybersecurity-ku1i).

## Scenario
An attacker was able to exploit the vulnerability on the affected server and began installing a ransomware virus. Luckily, the Incident Detection & Response team was able to prevent the ransomware virus from completely installing, so it only managed to encrypt one zip file. 
Also, when extracting the the document from the zip file, it prompts the user to enter the password.  

Internally, the Chief Information Security Officer does not want to pay the ransom, because there isn’t any guarantee that the decryption key will be provided or that the attackers won’t strike again in the future. 
Instead, we would like you to bruteforce the decryption key. Based on the attacker’s sloppiness, we don’t expect this to be a complicated encryption key, because they used copy-pasted payloads and immediately tried to use ransomware instead of moving around laterally on the network.

## Implementation
### Import and define the first function 
* 'zf_handle' = Handle Zip file. 
* 'zf_handle.extractall(pwd=password)': This attempts to extract all contents of the ZIP file using the provided password. If the password is correct, the extraction process should succeed.
* Password: This parameter is the password that will be used to attempt to decrypt the encrypted ZIP file. The assumption here is that the ZIP file is password-protected.
```
from zipfile import ZipFile
# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False
```

### Execution (Iterate password entries, extract zip file using passwords, handle correct and incorrect)

* Def main(): The main function described here is bruteforce attack.
* ZipFile enc.zip :: It opens the ZIP file named 'enc.zip' using the ZipFile class. The context manager (with statement) ensures that the file is properly closed after use.
* With open('rockyou.txt', 'rb') as f: It opens a file named 'rockyou.txt' in binary mode. This file is assumed to contain a list of passwords, one per line. It suggests that one of the common password in 'rockyou.txt' might be the solution.
* For p in f:: It iterates over each line in the password file.
* Password = p.strip(): It removes leading and trailing whitespaces from the password obtained from the file. Inside the loop, it calls the attempt_extract function with the current password. If the extraction is successful (meaning the correct password is found), it prints a message and exits the program. If the password is incorrect, it prints a message indicating that the password is incorrect. If the passwords are not found, the message would be shown.
* The if __name__ == "__main__": block ensures that the main() function is executed when the script is run, but not if it's imported as a module.
```
def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                password = p.strip()
                if attempt_extract(zf, password):
                    print('[+] Found correct password: %s' % password)
                    exit(0)
                else:
                    print('[-] Incorrect password: %s' % password)

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
```
### Output
* The code will extract the file out of zip file and the document will be shown in the same directory where you execute bruteforce.py. 
* For your convenience, I attached the output in "Output" folder. 
