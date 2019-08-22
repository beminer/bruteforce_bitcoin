import itertools
import subprocess
import time
import datetime

now = datetime.datetime.now()

PATH_FOR_PASSWD = "/home/beminer/1.txt"
PASSWD_SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
PASSWD_LENGTH = 10

def main():
    a = itertools.product(PASSWD_SYMBOLS, repeat=PASSWD_LENGTH)
    print(now.strftime("%d-%m-%Y %H:%M"))
    for i in a:
        p = subprocess.Popen('bitgreen-cli walletpassphrase {0} 60'.format(''.join(i)), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        if err.decode("utf-8") == '':
            now_last = datetime.datetime.now()
            delta = now_last - now

            hand = open(PATH_FOR_PASSWD, 'w')
            hand.write(''.join(i) + '\n' + str(delta.seconds) + '\n' + str(now_last.strftime("%d-%m-%Y %H:%M")))
            hand.close()

            break

if __name__ == "__main__":
    main()
