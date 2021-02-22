
import paramiko
import time

from getpass import getpass

def sh_int_status():

    # ip = input('Enter IP: ')
    # username = input('Enter username: ')
    #password = getpass()

    ip = '9.0.49.226'
    username = 'admin'
    password = 'R00ster!'

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
    DEVICE_ACCESS.send(b'term length 0\n')
    DEVICE_ACCESS.send(b'show ip int b\n')

    # Wait 2 seconds - command from time module
    time.sleep(5)

    # Receive the output of the command
    output = DEVICE_ACCESS.recv(65000)

    # Print the output
    print (output.decode('ascii'))

    # Close the session
    SESSION.close