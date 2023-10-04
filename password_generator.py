import random

s_alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
numb=[1,2,3,4,5,6,7,8,9,0]

c_alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
c_list=numb+c_alpha+symbols+s_alpha
r_numb=random.choice(numb)
r_c_aplha=random.choice(c_alpha)
r_s_alpha=random.choice(s_alpha)
r_symbols=random.choice(symbols)
r_mix=r_c_aplha+r_numb+r_s_alpha+r_symbols+str(r_numb)
password=""
for i in range(12):
    password=password+random.choice(r_mix)
print(password)
