import enigma
from datetime import datetime

input_file=open('output.txt')
output_file=open('input.txt','w')

e=enigma.enigma()

while True:
    l=input_file.readline()
    if not l:
        break
    if l=='**************\n':
        break
    output_file.write(l)

plain_text=input_file.read()
cipher=e.convert(plain_text)

output_file.write(cipher)
date=datetime.now()
dt_string=date.strftime('%d%m%Y %H:%M:%S')

output_file.write('\n'+dt_string+'\n')

input_file.close()
output_file.close()
