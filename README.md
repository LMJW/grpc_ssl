---
Date: 05-01-2018
---

## local branch

Description: This branch realizes the server client communication in localhost network using ssl server verification. There are three tests you can do for this example.

### test: working example
- in ```server.py``` file, load the certification in folder ```out/localhost.key``` and ```out/localhost.crt```. 
- in ```client.py``` file, load the certification in folder ```out/root.crt```. 
Note: the localhost.crt is signed by the root.crt. So in this case, ssl communication should be able to established.

### test: fail example
- in ```server.py``` file, load the certification in folder ```out2/localhost.key``` and ```out2/localhost.crt```. 
- in ```client.py``` file, load the certification in folder ```out/root.crt```. 
Note: the localhost.crt from folder ```out2``` is generated independently from ```root``` authentication. Since client is using ```root.crt``` certification, this example should fail to establish communication between server and client.

### test: fail example
- in ```server.py``` file, load the certification in folder ```out/localhost.crt``` and key from folder ```out2/localhost.key```. 
- in ```client.py``` file, load the certification in folder ```out/root.crt```. 
Note: the localhost.crt from folder ```out``` is signed by the ```root``` authentication. However, using ```localhost.key``` from the folder ```out2``` does not match with the key, therefore, server cannot create a ssl channel. Thus the communication will fail.

