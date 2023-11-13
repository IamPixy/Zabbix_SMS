With this Python script, You can send an SMS Alert From Zabbix by using Magfa SMS panel. 

ZABBIX SETUP

Clone the latest version of the script
Edit the following parameters in the script:
    - username = "Magfa UserName"
    - password = "Magfa service Password"
    - domain = "Magfa Domain"
    - magfaNumber = "Magfa Number"
    - text = 'Put the Message that you want to send in here'
    - receivers = ['Number 1', 'Number 2']



    
Put the script in the directory, you specified in the zabbix_server.conf, key AlertScriptsPath: Location for custom alert scripts AlertScriptsPath=/usr/lib/zabbix/alertscripts and ensure that it's executable (chmod 755 Zabbix_SmS.py).
Test the script, by running the following command: 
    - python3 ./Zabbix_SmS.py

After a few seconds, you should receive an SMS. In Zabbix go to Administration, Media Types, add a new media called sendsms, choose that it's a script, and enter the filename Zabbix_SmS.py as the script name and add these 2 parameters: {ALERT.SENDTO}, {ALERT.MESSAGE}

Finally, in Zabbix, Administration, Users, click on a user and add a new media called Zabbix_SmS.

Thats it.
