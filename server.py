import asyncio
import websockets


def delete_line_with_string(file_path, target_string):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    filtered_lines = [line for line in lines if target_string not in line]
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

async def handle_connection(websocket):
    client_ip = websocket.remote_address[0]
    print(f"connected from IP: {client_ip}")
    with open("lista", 'r') as file:
        lines = file.readlines()
        if not any(client_ip in line for line in lines):
            with open("lista", "a") as f:
                if os.path.getsize("lista") != 0:
                    f.write('\n')
                f.write(client_ip)
    with open("wylacz", "r") as file:
        lines = file.readlines()
        if not any(client_ip in line for line in lines):
            await websocket.send(f"yep")
            delete_line_with_string("wylacz", client_ip)
        else:
            await websocket.send(f"nope")
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