import sys
from subprocess import Popen, PIPE

process = Popen(['python', 'substitution_encryption.py', 'encrypt', 'handshake.txt','data.txt'])
process.wait()
process = Popen(['sudo', 'python', 'Icmp-File-Transfer/icmp.py', 'send', 'data.txt', '10.0.1.151'])

# process = Popen(['python', 'hw1.py', 'substitution', 'decrypt', 'data.txt','result.txt'])



stdout, stderr = process.communicate()