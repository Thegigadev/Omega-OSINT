###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import asyncio
from .Resources import console
from .Nodes import *
###################################################
class run:
    
    def __init__(self, command):
        options = {
            "help": run.help,
            "twitter": run.twitter,
            "instagram": run.instagram,
            "exit": console.quit,
            "clear": console.clear,
            "cls": console.clear,
            "ascii": console.ascii
        }
        if command in options:
            options[command]()
        else: 
            return

    def social(media):
        def wrapper():
            query = media(input(f"\n  -> Enter {media.__name__} Query: "))
            return query
        return wrapper

    @social
    def twitter(query):
        asyncio.run(Twitter().search(query))

    @social
    def instagram(query): 
        asyncio.run(Instagram().search(query))
###################################################
# seriously well done very swag
# Me > you? cry about it ok go work on facebook osint
# no u skid :rage: