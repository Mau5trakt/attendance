from datetime import  datetime

#now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print(now)

with open('cred.txt', 'r') as f:
    primera_linea = f.readline()

print(primera_linea)