from sys import argv
# import pyping
import re
import os

pings_num = 5
hostname = argv[1]
delays = []
while True:
    response = os.system("ping -c 1 {hostname}".format(hostname=hostname))
    # rtt = re.findall(r'time=(.*) ms', reqs)


# delays = []
# i = 0
#
# a = pyping.ping(hostname, count=12000)
#
# with open('rtt_files/{}.txt'.format(hostname), 'w') as out_file:
#     for reqs in a.output:
#         rtt = re.findall(r'time=(.*) ms', reqs)
#         if rtt:
#             out_file.write(str(int(round(float(rtt[0])))) + "\n")
