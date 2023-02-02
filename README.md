# nitk-embedathon-websockets

# Report

Websockets are a thin transport layer established between the client and the server.
The client who wants to get information connects to the server. The server uses asyncio to handle multiple clients and to return necessary output to them. Faker module is used to generate random names and respond to the request of the client.
Once the client recieves a 5 names from the server, it sends a response back to the server staing the time taken to recieve the 5 names.
If an interupt is given to close the client, Client reconnects with the server again instead of exiting the program.

# Instructions to run the program

First run the S-RecievesSendsConcurrently.py file which acts as the server.
C-SendsRecievesConcurrently.py file acts as a client, run the same in multiple terminals.

# Steps taken to finish the task

1. Understood the working of websockets and experimented with some simple programs.
2. Downloaded and Installed the necessary libraries required to finish the task.
3. Created and tested the code for concurrency using multiple clients.

# Modules used

1. asyncio: Python framework which provides high perfromance network and web-servers. This helps to decrease latency between the server and the client.
2. websockets: Used to build websocket connection in python, and to increase its performance.
3. faker: Used to generate random names to communicate between server and the client.
4. time: Used to calculate the time taken by the client to recieve 5 requests from the server.

# Results!

Image of the names recieved by the client<br />
![client](https://user-images.githubusercontent.com/97978349/216213068-50821659-c294-4d9e-a3c1-e845f15c465c.png)<br />
Image of the response recieved by the server<br />
![server](https://user-images.githubusercontent.com/97978349/216213373-454fcaa7-e7db-483e-b956-a2be42098def.png)

