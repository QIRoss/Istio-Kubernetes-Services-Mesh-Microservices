from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
async def read_root():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    finally:
        s.close()

    return {"message": f"Hello from IP {ip_address}!"}
