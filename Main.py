import os
import time
import asyncio
import asyncpg

from Apikeys import DB

from datetime import datetime, timezone
from asyncpg.pool import create_pool

async def Main():
    try:
        app_pool = await asyncpg.create_pool(
            database= DB.Name,
            host= DB.Host_IP,
            port= DB.Host_Port,
            user= DB.User_Name,
            password= DB.User_Pass
            )
    except:
        exit(f'Failed to connect to DB, please try again.\nERROR: 418 "Im a teapot"')

asyncio.run(Main())