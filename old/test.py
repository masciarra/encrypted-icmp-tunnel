from subprocess import Popen, PIPE

process = Popen(['sudo', 'python', 'Icmp-File-Transfer/icmp.py', 'send', 'shows.rtf', '192.168.2.2'])
stdout, stderr = process.communicate()