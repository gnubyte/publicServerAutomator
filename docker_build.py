# @Author: Patrick Hastings
# @Date 4-13-2018
# ----------------



import server

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


newDocker = server.Server(inputKeyPath="publickey.pem", inputKeyPassword='PASS', inputServerIP="0.0.0.0" )
newDocker.set_commands(commandList=dockerInstructions)
newDocker.connect()
newDocker.run_commands()