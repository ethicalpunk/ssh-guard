# SSH-GUARD #

___A program that monitors the SSH log file for malicious attempts to login and send them to a Discord webhook.___
___Once a successful SSH connection has been made, you will also be notified on the Discord webhook.___

Documentation
=============

    Configuration Options: (FOUND_IN: sshguard.py)
    
    - BLOCK_IPS |-| This variable must be set as a boolean phenomenetic Value.
    - VAR_LOG |-| This variable defines where the SSH log is located. By default this will be /var/log/auth.log.
    - NAME_OF_SERVER |-| This variable is optional and defines the name of the server to be shown in the Discord embed.
    - DISCORD_WEBHOOK_URL |-| This variable is where you define the discord webhook URL.

![alt text](https://github.com/ethicalpunk/ssh-guard/blob/main/docmentation/images/config_documentation.png?raw=true)

Demonstration
=============

    Once a login has failed, this message shown below will be send to the Discord webhook.

![alt text](https://github.com/ethicalpunk/ssh-guard/blob/main/docmentation/images/discord_msg_demo.png?raw=true)

    Once a successful login has been made, this message will be send to the Discord webhook.
    
![alt text](https://github.com/ethicalpunk/ssh-guard/blob/main/docmentation/images/discord_msg_demo_2.png?raw=true)
