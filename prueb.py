from datetime import  datetime
import os

from werkzeug.security import check_password_hash, generate_password_hash

#now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print(now)

with open('cred.txt', 'r') as f:
    primera_linea = f.readline()

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
#print(primera_linea)

contra = "1234"

generada = generate_password_hash(contra)

print(generada)

