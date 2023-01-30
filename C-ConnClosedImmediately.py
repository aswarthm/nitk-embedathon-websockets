import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8000") as websocket:
        websocket.send("Client")

        greeting = await websocket.recv()
        print(greeting)

asyncio.run(hello())
