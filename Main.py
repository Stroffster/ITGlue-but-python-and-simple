import asyncio #Import sync libary
import asyncpg #Database connection thingy ma jig
import tkinter as tk #Importing the GUI libary
import hashlib #Impoting encryption libary

from Apikeys import DB #Get the database class with log in information

from asyncpg.pool import create_pool #Import the database connection function

#Main
async def DB_connect():
    db_info = DB() 
    try: #Tries to connect, if it fails it prints out an error
        #Connect to the database
        DB_Pool = await asyncpg.create_pool(
            database= db_info.Name,
            host= db_info.Host_IP,
            port= db_info.Host_Port,
            user= db_info.User_Name,
            password= db_info.User_Pass
            )
        print("DB connection successful") #DEBUG
    except:
        #Exit the program and print the error
        exit(f'Failed to connect to DB, please try again.\nERROR:\n418 "Im a teapot"') #DEBUG

#Run main function using sync
asyncio.run(DB_connect())