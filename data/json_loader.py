import os

import aiofiles
from ujson import loads


async def get_json(filename: str) -> list:
    path = f"data/{filename}"
    
    if os.path.exists(path):
        async with aiofiles.open(path, mode='r', encoding='utf-8') as json_file:
            return loads(await json_file.read())
    return []
