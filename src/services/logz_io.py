import httpx

class LogzIoService:
    def __init__(self, logz_io):
        self.listener_host = logz_io['listener_host']
        self.listener_port = logz_io['listener_port']
        self.listener_token = logz_io['listener_token']
        self.url = f"https://{self.listener_host}:{self.listener_port}/?token={self.listener_token}"

    async def send_data(self, data):
        try:
            response = httpx.post(self.url, content=data, headers={"Content-Type": "application/json"})
            return response.status_code
        except httpx.RequestError as e:
            print(f"Error sending data to Logz.io: {e}")
            return None