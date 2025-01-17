import asyncio
import websockets
import os
async def test_client():
    uri = "ws://192.168.100.10:8765"
    async with websockets.connect(uri) as websocket:
        message = await websocket.recv()
        print(f"Server says: {message}")
        await websocket.send("Hello")
        response = await websocket.recv()
        if message == "yep":
            os.system("shutdown now -h")

if __name__ == "__main__":
    asyncio.run(test_client())
