import websockets
import asyncio


clients = []


async def handle_message(websocket, path):
    global clients
    global fastest_time
    message = await websocket.recv()
    if message == "buzz":
        respones_time = asyncio.get_event_loop().time()
        clients.append([websocket, respones_time])
        if len(clients) == 1:
            await websocket.send("First place!")
        else:
            t = round(respones_time - fastest_time, 2)
            await websocket.send("cdsada")

async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        print('Websocket server has started')
        await asyncio.Future()



def main():
    asyncio.run(start_server())



if __name__ == '__main__':
    main()