import paramiko
import time

from getpass import getpass

# ip = input('Enter IP: ')
# username = input('Enter username: ')
# password = input('Enter password: ')

ip = '9.0.49.226'
username = 'admin'
password = 'R00ster!'

a = int (input('Enter first loopback in range : '))
b = int (input('Enter last loopback in range : ')) + 1

# Create a session using paramiko class
SESSION = paramiko.SSHClient() 

# Ad the device certificate on the client
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Set the connection parameters
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

# Invoke shell to pass the commands
DEVICE_ACCESS = SESSION.invoke_shell()

# Send commands
DEVICE_ACCESS.send(b'config t\n')
for N in range (a,b):
    DEVICE_ACCESS.send('no int lo ' +str(N) + '\n')
#    DEVICE_ACCESS.send('ip address 1.1.1.' +str(N) + ' 255.255.255.255\n')  

# Wait 5 seconds - command from time module
time.sleep(5)
DEVICE_ACCESS.send('exit\n')
DEVICE_ACCESS.send('exit\n')
DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b'show ip int b\n')

# Wait 5 seconds - command from time module
time.sleep(5)

# Receive the output of the command
output = DEVICE_ACCESS.recv(65000)

# Print the output
print (output.decode('ascii'))

# Close the session
SESSION.close
