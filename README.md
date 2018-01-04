---
Branch Description: This branch is the "localdocker" branch. This branch mainly accomplish the communication between two containers(server container and client container) using ssl server verification.
Decription of the example: Client query server with a text message, the server will add this message into an in memory sqlite3 database and return client all the messages in this database.
---
## How to run this example

1. open a terminal. Make sure the git branch is ```localdocker```. If not, change branch to docker using ```git checkout localdocker```. Then, run the command```docker build .```

2. After the docker image is successfully built, find the image name/ID. For example, my ID is ```444fef4646ea```.  Replace ```<ID>``` with your image ID. Then, run:

  ```bash
  docker run --name container1 -it <ID>
  ```
  **NOTE**: There maybe an error if you already has a container called "container1". You can name the container to different name or delete the "container1" and re-execute this command.
3. Keep the first terminal open. Then open a new terminal, run the following command:
  ```bash
  docker run --name container2 -it <ID>
  ```

4. Open the third terminal, run the command:
  ```bash
  docker network create testnet
  docker network connect testnet container1 --alias client
  docker network connect testnet container2 --alias server
  ```

5. Open the second terminal (which runs the server container), type:
  ```bash
  python3 server.py
  ```
6. In the first terminal, type:
  ```bash
  python3 client.py
  ```
  and follow the instructions given by the terminal. You can repeat command 6 to send another message.


 

