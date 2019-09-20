
## ----------------------
# JSON Proof Of Concept
# https://stackoverflow.com/questions/10973614/convert-json-array-to-python-list
import json

array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
print data['fruits']
# the print displays:
# [u'apple', u'banana', u'orange']


### ----------------------------
# raise ValueError with custom Error Message POC
# https://stackoverflow.com/questions/4393268/how-to-raise-a-valueerror

def contains(char_string, char):
    largest_index = -1
    for i, ch in enumerate(char_string):
        if ch == char:
            largest_index = i
    if largest_index > -1:  # any found?
        return largest_index  # return index of last one
    else:
        raise ValueError('could not find {} in {}'.format(char, char_string))

print(contains('mississippi', 's'))  # -> 6
print(contains('bababa', 'k'))  # ->

### ----------------------------
# Deconstructors Python Proof of Concept
#  https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
class Package:
    def __init__(self):
        self.files = []

    def __enter__(self):
        return self

    # ...

    def __exit__(self, exc_type, exc_value, traceback):
        for file in self.files:
            os.unlink(file)
### ----------------------------
# Paramiko Python Proof of Concept Simple Connection
# https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
import paramiko
k = paramiko.RSAKey.from_private_key_file("/Users/whatever/Downloads/mykey.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting"
c.connect( hostname = "www.acme.com", username = "ubuntu", pkey = k )
print "connected"
commands = [ "/home/ubuntu/firstscript.sh", "/home/ubuntu/secondscript.sh" ]
for command in commands:
    print "Executing {}".format( command )
    stdin , stdout, stderr = c.exec_command(command)
    print stdout.read()
    print( "Errors")
    print stderr.read()
c.close()
