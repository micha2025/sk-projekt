import asyncio
import websockets

async def handle_connection(websocket):
    client_ip = websocket.remote_address[0]
    with open("lista", "a") as f:
        if os.path.getsize("lista") != 0:
            f.write('\n')
        f.write(client_ip)

    print(f"Client connected from IP: {client_ip}")
    
    # TODO
    await websocket.send(f"Your IP address is: {client_ip}")
    
    try:
        async for message in websocket:
            print(f"Received from {client_ip}: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"Client {client_ip} disconnected")


async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 8765):
        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
