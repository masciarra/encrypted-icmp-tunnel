import sys
from subprocess import Popen, PIPE

ip = sys.argv[2]
inputpath = sys.argv[1]

process = Popen(['python', '../substitution_encryption.py', 'encrypt', inputpath,'data.txt'])
process.wait()
process = Popen(['sudo', 'python', 'Icmp-File-Transfer/icmp.py', 'send', 'data.txt', ip])

stdout, stderr = process.communicate()