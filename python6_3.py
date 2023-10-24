#!/usr/bin/env python
import subprocess
poem=open('poem.txt','r')
poem_read=poem.read()
print(poem_read)

poem.close()

#poem_upper=poem_read.upper()
#print(poem_upper)
#poem_object=open('poem_capital.txt', 'w')
#poem_object.write(poem_upper)
#print('the file is empty until you close() it!!!')
#subprocess.run('ls -l poem_capital.txt', shell=True)
#poem_object.close()


