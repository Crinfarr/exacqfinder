import numpy as np
import json

port25 = np.array([])
port80 = np.array([])

linect = 0
for line in open("./complete.list"):
    linect += 1
    print(f'\rcounting lines...{linect}', end="")
print("\rDone.  Total lines: "+str(linect))

for line in enumerate(open("./complete.list")):
    if (line[1].startswith("#")): continue
    port, ip = line[1].split(" ")[-3:-1]
    if port == '25':
        port25 = np.append(port25, ip)
    else:
        port80 = np.append(port80, ip)
    print(f'sorting lines...{round(line[0]/linect*100,2)}%  ', end="\r")
f = open('./out.json', 'x')
print('comparing arrays...')
isect = np.intersect1d(port25, port80)
print("dumping to list")
isect = isect.tolist()
f.write(json.dumps(np.intersect1d(port25, port80)))
f.close()
print("saved.")