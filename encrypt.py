from hashlib import *
import py_compile
import time
import webbrowser



gr = "\033[1;32m"
po = '\033[1;38m'
{gr}- {po}1*[Encrypt md5]
{gr}- {po}2*[Encrypt sha3_512]
{gr}- {po}3*[Encrypt sha256]
{gr}- {po}4*[Encrypt sha384]
{gr}- {po}5*[Encrypt sha1]
{gr}- {po}6*[Encrypt sha512]
{gr}- {po}7*[Encrypt sha224]
{gr}- {po}8*[Encrypt sha3_384]
{gr}- {po}9*[Encrypt sha1]
{gr}- {po}10*[Encrypt Files]
   ''')

print("Enter number")
mod1=input(">> ")
if mod1 == "1":
    time.sleep(0.0)
    print("Encrypt md5  ")
    print("Enter text to Encrypt it ")
    ll = input(">> ")
    q = md5(ll.encode()).hexdigest()
    print(q)
elif mod1 == "2":
    time.sleep(0.0)
    print("Encrypt sha3_512  ")
    print("Enter text to Encrypt it")
    llsf = input(">> ")
    qsdf = sha3_512(llsf.encode()).hexdigest()
    print(qsdf)
elif mod1 == "3":
    time.sleep(0.0)
    print("Encrypt sha256  ")
    print("Enter text to Encrypt it")
    llsffd = input(">> ")
    qsdfsd = sha256(llsffd.encode()).hexdigest()
    print(qsdfsd)
elif mod1 == "4":
    time.sleep(0.0)
    print("Encrypt sha384  ")
    print("Enter text to Encrypt it")
    llsffdgs = input('>> ')
    qsdfsdgs = sha384(llsffdgs.encode()).hexdigest()
    print(qsdfsdgs)
elif mod1 == "5":
    time.sleep(0.0)
    print("Encrypt sha1  ")
    print("Enter text to Encrypt it")
    llsfg = input(">> ")
    qsdfg = sha1(llsfg.encode()).hexdigest()
    print(qsdfg)
elif mod1 == '6':
    time.sleep(0.0)
    print("Encrypt sha512  ")
    print("Enter text to Encrypt it")
    llsfgf = input(">> ")
    qsdfga = sha512(llsfgf.encode()).hexdigest()
    print(qsdfga)
elif mod1 == '7':
    time.sleep(0.0)
    print("Encrypt sha224  ")
    print("Enter text to Encrypt it")
    llsfgfa = input(">> ")
    qsdfgas = sha224(llsfgfa.encode()).hexdigest()
    print(qsdfgas)
elif mod1 == '8':
    time.sleep(0.0)
    print("Encrypt sha3_384  ")
    print("Enter text to Encrypt it")
    llsfgfaa = input(">> ")
    qsdfgass = sha3_384(llsfgfaa.encode()).hexdigest()
    print(qsdfgass)
elif mod1 == '9':
    time.sleep(0.0)
    print("Encrypt sha224  ")
    print("Enter text to Encrypt it")
    llsfgfal = input(">> ")
    qsdfgags = sha1(llsfgfal.encode()).hexdigest()
    print(qsdfgags)
elif mod1 == '10':
    print('Encrypt files ')
    filza4554545455445454 = input('>> ')
    py_compile.compile(filza4554545455445454)
    print('Encryption successful ')
    py_compile.compile(filza4554545455445454)

