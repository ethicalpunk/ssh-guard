import socket
from sh import tail
import ipaddress
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
import os
import time

BLOCK_IPS = False # Make this variable True if you would like to automatically block failed SSH logins with IPTABLES
VAR_LOG = "/var/log/auth.log" # This is where you define where SSH writes login and logout logs
NAME_OF_SERVER = "Server-1" # This is where you can specify the name of the server that will be displayed in the discord channel
DISCORD_WEBHOOK_URL = "" # This is where you define the webhook channel URL"

def gettime():
    deftime = datetime.datetime.now()
    currtime = (deftime.strftime("%Y-%m-%d %H:%M:%S"))
    return currtime

def webhook(content, colour, url):
    webhook = DiscordWebhook(url=url)

    embed = DiscordEmbed(title=f':warning: SSH ALERT `({NAME_OF_SERVER})`', description=content, color=colour)
    webhook.add_embed(embed)
    response = webhook.execute()

failed = []

print("Listening for input on file: {}".format(VAR_LOG))

for line in tail("-F", "-n 0", VAR_LOG, _iter=True):
    data = line
    ip = None
    found = False
    blocked = False

    if "Failed password for" in data:
        data = data.split()
        for itter in data:
            try:
                ip = str(ipaddress.ip_address(itter))
                break
            except ValueError:
                pass

        if failed:
            for ipaddr in failed:
                ipaddr = ipaddr.split()
                if ipaddr[0] == ip:
                    if int(ipaddr[1]) >= 4:
                        if BLOCK_IPS == True:
                            print("Blocking")
                            failed.remove(f"{ip} 4")
                            os.system("iptables -A INPUT -s {} -j DROP".format(ip))
                            blocked = True
                            failedcount = 4
                            break

                        elif BLOCK_IPS == False:
                            found = True
                            failed.remove(f"{ipaddr[0]} {ipaddr[1]}")
                            failed.append(f"{ipaddr[0]} {str(int(ipaddr[1]) + 1)}")
                            for ipaddr in failed:
                                ipaddr = ipaddr.split()
                                if ipaddr[0] == ip:
                                    failedcount = ipaddr[1]
                                    break


                    elif int(ipaddr[1]) < 4:
                        found = True
                        failed.remove(f"{ipaddr[0]} {ipaddr[1]}")
                        failed.append(f"{ipaddr[0]} {str(int(ipaddr[1]) + 1)}")
                        for ipaddr in failed:
                            ipaddr = ipaddr.split()
                            if ipaddr[0] == ip:
                                failedcount = ipaddr[1]
                                break
                        break

            if blocked == True:
                try:
                    webhook(f"`{gettime()}` **{failedcount} failed SSH connections from:** {ip} **Autoblock=True**", "0xe1ff00", DISCORD_WEBHOOK_URL)
                except:
                    pass

                continue

            if found == False:
                failed.append(f"{ip} 1")
                failedcount = 1

        elif not failed:
            failed.append(f"{ip} 1")
            failedcount = 1

        print(f"{failedcount} failed SSH connections from: {ip}")

        try:
            webhook(f"`{gettime()}` **{failedcount} failed SSH connections from:** {ip}", "0xe1ff00", DISCORD_WEBHOOK_URL)
        except:
            pass

    elif "Accepted password for" in data:
        data = data.split()
        del data[0:5]
        ip = data[-4].strip()
        data = ' '.join(data)
        for ipaddr in failed:
            ipaddr = ipaddr.split()
            if ipaddr[0] == ip:
                failed.remove(f"{ipaddr[0]} {ipaddr[1]}")
                break

        print(f"Successful SSH connection from: {ip}")

        try:
            webhook(f"`{gettime()}` **Successful SSH connection from:** {ip}", "0x00ffb7", DISCORD_WEBHOOK_URL)
        except:
            pass

    failedcount = 1
