# MakeMigration 
    - python manage.py makemigrations
    - python manage.py migrate

    import asyncio 

async def FirstWorker():
    while True:
        await asyncio.sleep(0.01)
        print("First worker working progress...")


async def SecondWorker():
    while True:
        await asyncio.sleep(0.01)
        print("Second worker working progress...")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(FirstWorker())
    asyncio.ensure_future(SecondWorker())
    loop.run_forever()
except KeyboardInterrupt:
    print("Sorry!....")
finally:
    print("Closing the loop")
    loop.close()

#https://www.youtube.com/watch?v=6yrzKI2p2y8
#https: // www.cssscript.com/tiny-native-javascript-image-cropper-croppr-js/
# mercidus-fs.x~007infidostrixWx/Xcostrixvz.~dostrix-0072020%jeos~