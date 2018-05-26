from sys import argv
import pyping
import re


hostname = argv[1]
delays = []
i = 0

a = pyping.ping(hostname, count=12000)

with open('rtt_files/{}.txt'.format(hostname), 'w') as out_file:
    for reqs in a.output:
        rtt = re.findall(r'time=(.*) ms', reqs)
        if rtt:
            out_file.write(str(int(round(float(rtt[0])))) + "\n")
