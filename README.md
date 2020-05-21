# Public Server Automator
## V1.1


![](https://github.com/gnubyte/publicServerAutomator/raw/master/docs/publicServerAutomator.png?raw=true)

 * [PublicServerAutomator Github](https://github.com/gnubyte/publicServerAutomator)
 * [Changelog](https://raw.githubusercontent.com/gnubyte/publicServerAutomator/master/changelog)
 * **Author**: Patrick Hastings
 * **Author Site:**: https://gnubyte.com
 * [Pypi repository](https://pypi.org/project/publicServerAutomator/)


- [Public Server Automator](#public-server-automator)
  - [V1.1](#v11)
  - [Purpose](#purpose)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running multiple SSH Commands](#running-multiple-ssh-commands)
      - [Running SSH commands with Private Key Authentication](#running-ssh-commands-with-private-key-authentication)
      - [Running SSH commands with Username & Password Authentication](#running-ssh-commands-with-username--password-authentication)
    - [Move file to server via SFTP](#move-file-to-server-via-sftp)
      - [SFTP Private Key Authentication example](#sftp-private-key-authentication-example)
      - [Using Username and Password SFTP Authentication](#using-username-and-password-sftp-authentication)





## Purpose

This is a package intended to offer a much simpler, no hickups, no learning curve package + software alternative to Ansible/chef/puppet

## Installation

Install via pip
```
pip install publicServerAutomator
```


##  Usage

Below is a brief tutorial of how to use this framework.


### Running multiple SSH Commands

#### Running SSH commands with Private Key Authentication

Here is how you authenticate SSH commands with private key authentication using PublicServerAutomator.

```
from publicServerAutomator import Server

dockerInstructions = [
    "apt-get update -y",
    "apt-get install apt-transport-https -y",
    "apt-get install software-properties-common -y",
    "apt-get install curl -y",
    "apt-get install gnupg2 -y",
    "apt-get install git -y",
    "apt-get install acl -y",
    "apt-get install fail2ban -y"
    '''add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"''',
    "apt-get update -y",
    "apt-get install docker-ce -y",
    "docker run hello-world"
]

newDocker = Server(inputKeyPath="publickey.pem", inputKeyPassword='PASS', inputServerIP="0.0.0.0" )
newDocker.set_commands(commandList=dockerInstructions)
newDocker.connect()
output = newDocker.run_commands()
print(output)
```

#### Running SSH commands with Username & Password Authentication

This is an example of running multiple commands on a host, without using a private key to authenticate.

Notice that the Username and password are specified using `inputUserName` and `inputPassword`.

```
from publicServerAutomator import Server

dockerInstructions = [
    "apt-get update -y",
    "apt-get install apt-transport-https -y",
    "apt-get install software-properties-common -y",
    "apt-get install curl -y",
    "apt-get install gnupg2 -y",
    "apt-get install git -y",
    "apt-get install acl -y",
    "apt-get install fail2ban -y"
    '''add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"''',
    "apt-get update -y",
    "apt-get install docker-ce -y",
    "docker run hello-world"
]

newDocker = Server(inputServerIP='8.8.8.8',inputUserName='root', inputPassword='123lookatme', inputKeyPath='')
newDocker.set_commands(commandList=dockerInstructions)
newDocker.connect()
output = newDocker.run_commands()

```



### Move file to server via SFTP

How to transfer files with SFTP w & w/o private key authentication

#### SFTP Private Key Authentication example

Here is how you transfer a file with a private key authentication

```
from publicServerAutomator import Server

someServer = Server(inputKeyPath="publickey.pem", inputKeyPassword='PASS', inputServerIP="0.0.0.0" )
someServer.connect()
someServer.transfer_file(full_path_local_file='/home/someGuy/mybigFile.gzip', full_path_target_path='/opt/someSoftware/mybigFile.gzip')
```


#### Using Username and Password SFTP Authentication

Here is how you transfer a file without a private key

```
from publicServerAutomator import Server

someServer = Server(inputServerIP='8.8.8.8',inputUserName='root', inputPassword='123lookatme', inputKeyPath='')
someServer.connect()
someServer.transfer_file(full_path_local_file='/home/someGuy/mybigFile.gzip', full_path_target_path='/opt/someSoftware/mybigFile.gzip')


```