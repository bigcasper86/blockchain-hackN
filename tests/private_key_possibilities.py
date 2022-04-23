from brownie import accounts
import os
import socket


def check_internet():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), timeout=2)
        s.close()
        return True
    except:
        pass
    return False


def set_dir(name):
    os.chdir(f"/home/surya/{name}")


def get_account():
    account = accounts.add()
    return account


def findAccount(dir_name, py_file):
    try:
        set_dir(dir_name)
        value = 0
        while value == 0:
            account = get_account()
            if account.balance() > 0:
                value = account.balance()
                log = open(py_file, "a")
                log.write(
                    f"\n {{\n\tAddress: {account.address}\n\tPrivate Key:{account.private_key}\n\tBalance:{account.balance()}\n}}"
                )
                log.close()
                print(f"Account Address: {account.address}")
                print(f"Private Key: {account.private_key}")
            else:
                print("Searching Address...")
    except:
        print("Passing Find Account")
        pass


def main():
    while True:
        if check_internet():
            findAccount("ForeverTest", "private_key_possibilities.log")
        else:
            print("Passing Main")
            pass
