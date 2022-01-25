###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import asyncio
import os
from .Resources import console, coloring
from .Resources.Browsers import *
from .Nodes import *
import inspect
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
###################################################
class run:
    
    def __init__(self, command):
        options = {
            "help": run.help,
            "twitter": run.twitter,
            "instagram": run.instagram,
            "checkpwn": run.checkpwn, 
            "exit": console.quit,
            "clear": console.clear,
            "cls": console.clear,
            "ascii": console.ascii,
            "facebook": run.facebook,
            "facebookapi": run.facebookapi,
            "shodan": run.shodan,
            "shodanreport": run.shodanreport
        }
        if command.lower() in options:
            options[command.lower()]()
        else: 
            return
            
    def osint(media):
        def wrapper():
            if "i" in inspect.signature(media).parameters:
                query = str(input(f"{coloring.BLUE}\n  -> Enter {media.__name__} query: "))
                amount = int(input(f"{coloring.BLUE}\n  -> Enter amount of searches: "))
                media(query, amount)
                return query, amount
            else:
                query = str(input(f"{coloring.BLUE}\n  -> Enter {media.__name__} query: "))
                media(query)
                return query
            # Add \n to results
        return wrapper

    @osint
    def twitter(query, i:int = None):
        asyncio.run(Twitter().search(query, i))

    @osint
    def instagram(query, i:int=None): 
        asyncio.run(Instagram().search(query, i))

    @osint
    def checkpwn(query):
        asyncio.run(pwn.check(query))

    @osint
    def facebookapi(query):
        asyncio.run(Facebook().search2(query))

    @osint
    def facebook(query, i:int=None):
        asyncio.run(Facebook().search(query, i))
    
    @osint
    def shodan(query):
        asyncio.run(Shodan().search(query))

    @osint
    def shodanreport(query):
        asyncio.run(Shodan().report(query))


    def help():
        print(f"""
  {coloring.WHITE}-------------------------------------------------- 
  [{coloring.WARNING}!{coloring.WHITE}] Commands: {coloring.BLUE}[command name]{coloring.WHITE}
  {coloring.BLUE}Name:                  {coloring.BLUE}Description:
  {coloring.WARNING}help                {coloring.WHITE}Creates specified number of GCs with tokens.
  {coloring.WARNING}clear               {coloring.WHITE}Clears terminal of all print. Alias cls.
  {coloring.WARNING}ascii               {coloring.WHITE}Prints terminal art.
  {coloring.WARNING}exit                {coloring.WHITE}Terminates script.
  {coloring.WARNING}twitter             {coloring.WHITE}Searches Twitter for keyword.
  {coloring.WARNING}facebook            {coloring.WHITE}Check if email has been found in breaches.
  {coloring.WARNING}instagram           {coloring.WHITE}Searches Facebook for keyword
  {coloring.WARNING}facebookapi         {coloring.WHITE}Searches Facebook for keyword using their API.
  {coloring.WARNING}checkpwn            {coloring.WHITE}Check if email has been found in breaches.
  {coloring.WARNING}shodan              {coloring.WHITE}Searches shodan for keyword
  {coloring.WARNING}shodanreport        {coloring.WHITE}Searches shodan reports for keyword


  ---------------------------------------------------------------
        """)
###################################################
# Dev Notes #
###################################################
# File made by Roover.
