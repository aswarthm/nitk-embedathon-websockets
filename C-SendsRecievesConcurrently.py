import asyncio
import websockets
import time

cName = "lol"
time1 = time.time()
print(time1)
data = set()
n = 0


async def send_messages(websocket):
    global n, time1
    while True:
        if(len(data) >= 5):
            await websocket.send(f"Client {cName} received {n} blocks in {time.time() - time1} time")
            data.clear()
            n=0
            time1 = time.time()
        await asyncio.sleep(1)

# async def send_messages(websocket):
#     while True:
#         await websocket.send("Hey Server!")
#         await asyncio.sleep(1)


async def receive_messages(websocket):
    global n
    while True:
        message = await websocket.recv()
        data.add(message)
        n += 1
        print(f"{len(data)}. Received message: {message}")


async def client():
    async with websockets.connect("ws://localhost:8000") as websocket:
        # Create tasks to send and receive messages concurrently
        send_task = asyncio.create_task(send_messages(websocket))
        receive_task = asyncio.create_task(receive_messages(websocket))
        await asyncio.gather(send_task, receive_task)

asyncio.run(client())
