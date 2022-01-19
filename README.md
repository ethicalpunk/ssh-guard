# SSH-GUARD #

___A program that monitors the SSH log file for malicious attempts to login and send them to a Discord webhook.___
___Once a successful SSH connection has been made, you will also be notified on the Discord webhook.___

Documentation
=============

    Configuration Options:
    
    - BLOCK_IPS |-| This variable must be set as a boolean phenomenetic Value.
    - VAR_LOG |-| This variable defines where the SSH log is located. By default this will be /var/log/auth.log.
    - NAME_OF_SERVER |-| This variable is optional and defines the name of the server to be shown in the Discord embed.
    - DISCORD_WEBHOOK_URL |-| 

![alt text](https://github.com/ethicalpunk/ssh-guard/blob/main/docmentation/images/config_documentation.png?raw=true)
