from brownie import accounts,network
import os
import socket
import threading

def check_internet():
  try:
	  host=socket.gethostbyname("www.google.com")
	  s=socket.create_connection((host,80),timeout=2)
	  s.close()
	  return True
  except:
    pass
  return False	
	
	
def set_dir(name):
  os.chdir(f"/home/surya/{name}")


def get_account():
  account=accounts.add()
  return account
	
	
def findAccount(dir_name,py_file):
  try:
    set_dir(dir_name)
    value=0
    while(value==0):
      account=get_account()
      if(account.balance()>0):
        print("Got One Account")
        value=account.balance()
        log=open(py_file,'a')
        log.write(f"\n {{\n\tAddress: {account.address}\n\tPrivate Key:{account.private_key}\n\tBalance:{account.balance()}\n}}")
        log.close()
  except:
    print("passing from find accont")
    pass
			

def main():
  run=True
  while run:
    if(check_internet()):
            t1=threading.Thread(target=findAccount, args=("ForeverTest","private_key_possibilities.log"))
            t2=threading.Thread(target=findAccount, args=("ForeverTest","private_key_possibilities.log"))
            t3=threading.Thread(target=findAccount, args=("ForeverTest","private_key_possibilities.log"))
            t4=threading.Thread(target=findAccount, args=("ForeverTest","private_key_possibilities.log"))
            t5=threading.Thread(target=findAccount, args=("ForeverTest","private_key_possibilities.log"))
            t6=threading.Thread(target=findAccount, args=("ForeverTest","private_key_possibilities.log"))
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
    else:
        print("Check Your Internet")
	


