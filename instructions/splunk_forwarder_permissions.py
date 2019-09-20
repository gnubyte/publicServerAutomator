
# @Author: Patrick Hastings
# @Date 4-14-2018
# For Debian based splunk forwarder hosts
# Makes sure that Splunk Forwarder has instructions to the right files
# ----------------
import server

splunk_forwarder_permissions = [
    "apt-get install acl -y",
    "setfacl -m g:splunk:rx /var/log"
    
]
newDocker = server.Server(inputKeyPath="key.pem", inputKeyPassword='PASS', inputServerIP="0.0.0.0" )
newDocker.set_commands(commandList=splunk_forwarder_permissions)
newDocker.connect()
newDocker.run_commands()