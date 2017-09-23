import random

def codify_gender(gnd):
    if gnd == 'F':
        gen_code = random.randrange(65,77)
    elif gnd == 'M':
        gen_code = random.randrange(78,90)
    return chr(gen_code)

def codify_dob(dob):
    return dob.strftime('%y%m%d')

def codify_citizen(citzn):
    if citzn :
        return 'C'
    return 'E'

def generate_sequence():
    return str(random.randrange(1000,9999))

def checksum(num):
    while(num > 10):
        num = sum(map(int, str(num)))
    return num
