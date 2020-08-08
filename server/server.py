import sys
from subprocess import Popen, PIPE


while(True):
    process = Popen(['sudo', 'python', 'Icmp-File-Transfer/icmp.py', 'recv', 'data.txt'])
    process.wait()
    process = Popen(['python', 'substitution_encryption.py', 'decrypt', 'data.txt','handshake.txt'])
    process.wait()
    fi = open("handshake.txt", "r")
    fileContents = fi.read()

    counter = 0;
    handshake = False

    for line in fileContents.splitlines():
        if (counter < 2):
            if (counter == 0 and line == "handshake"):
                # print("success")
                handshake = True
            else:
                if (handshake):
                    print(line)         


        else:
            break
        counter += 1



# for word in fileContents.split():
#     print(word)


# for line in fileContents:
#     print("iteration")
#     print(line)
#     # for word in line.split():
#     #     print(word)
# print("test")

