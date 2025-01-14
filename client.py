import asyncio
import websockets
import keyboard

async def start_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        done = False
        while not done:
            if keyboard.is_pressed:
                print("ok")