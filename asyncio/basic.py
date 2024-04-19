# In a real-time chat application, we need to handle multiple users who are sending and receiving messages simultaneously.

# Problems: 

# Handling multiple incoming connections simultaneously without slowing down the user experience.
# Receiving and broadcasting messages in real-time to possibly hundreds or thousands of connected clients.
# Managing waiting times efficiently when no data is being transmitted.

import asyncio
import websockets

connected = set()

async def chat_handler(websocket, path):
    # Register websocket connection
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast incoming message to all connected clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    finally:
        # Unregister websocket connection
        connected.remove(websocket)

async def main():
    async with websockets.serve(chat_handler, "localhost", 6789):
        await asyncio.Future()  # run forever

asyncio.run(main())


