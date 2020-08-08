import sys
from subprocess import Popen, PIPE

process = Popen(['python', 'hw1.py', 'substitution', 'encrypt', 'handshake.txt','data.txt'])
process.wait()
process = Popen(['sudo', 'python', 'Icmp-File-Transfer/icmp.py', 'send', 'data.txt', '192.168.2.2'])

# process = Popen(['python', 'hw1.py', 'substitution', 'decrypt', 'data.txt','result.txt'])



stdout, stderr = process.communicate()