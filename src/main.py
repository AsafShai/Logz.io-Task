import httpx
import asyncio
import json
from time import sleep
from .util.config_parser import ConfigParser
from .services.fetcher_service import FetcherService
from .services.logz_io import LogzIoService


async def main():
    await main_loop()


async def main_loop():
    config_parser = ConfigParser('config.json')
    data_sources = config_parser.get_data_sources()
    logz_io_service = LogzIoService(config_parser.get_logz_io())
    polling_interval = config_parser.get_polling_interval()
    async with httpx.AsyncClient() as client:
        while True:
            tasks = []
            for data_source in data_sources:
                task = asyncio.create_task(FetcherService().fetch_data(client, data_source))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            ndjson_data = '\n'.join(json.dumps(item) for item in results)
            status_code = await logz_io_service.send_data(ndjson_data)
            print(f"Status code: {status_code}")
            await asyncio.sleep(polling_interval)


if __name__ == "__main__":
    asyncio.run(main())
