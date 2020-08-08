Encrypted ICMP Tunnel in Python:

Client and server scripts to send/receive encrypted text over ICMP

References ICMP code from:

https://github.com/Vidimensional/Icmp-File-Transfer

Works with Python 2 and 3.

Text file to send must include have the first line "handshake" without quotes.  The scripts use this line to determine if incoming data is from a familiar source.  An example is provided in the client directory, named "handshake.txt".

To run the client, run sudo python /client/client.py <txt file to send> <ip to send to>

To run the server, run sudo python /server/server.py

Server prints incoming decrypted data to terminal.