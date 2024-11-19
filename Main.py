import asyncio #Import sync libary
import asyncpg #Database connection thingy ma jig
import tkinter as tk #Importing the GUI libary
import hashlib #Impoting encryption libary

from Apikeys import DB #Get the database class with log in information

from asyncpg.pool import create_pool #Import the database connection function

#Main
async def Main():
    try: #Tries to connect, if it fails it prints out an error
        #Connect to the database
        app_pool = await asyncpg.create_pool(
            database= DB.Name,
            host= DB.Host_IP,
            port= DB.Host_Port,
            user= DB.User_Name,
            password= DB.User_Pass
            )
    except:
        #Exit the program and print the error
        exit(f'Failed to connect to DB, please try again.\nERROR:\n418 "Im a teapot"')

#Run main function using sync
asyncio.run(Main())