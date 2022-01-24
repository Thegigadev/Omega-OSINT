###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import asyncio
import os
from .Resources import console, coloring
from .Nodes import *
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
            "facebookapi": run.facebookapi
        }
        if command.lower() in options:
            options[command.lower()]()
        else: 
            return
            
    def osint(media):
        def wrapper():
            query = media(input(f"{coloring.BLUE}\n  -> Enter {media.__name__} query: "))
            # Add \n to results
            return query
        return wrapper

    @osint
    def twitter(query):
        asyncio.run(Twitter().search(query))

    @osint
    def instagram(query): 
        asyncio.run(Instagram().search(query))

    @osint
    def checkpwn(query):
        asyncio.run(pwn.check(query))

    @osint
    def facebookapi(query):
        asyncio.run(Facebook().search2(query))

    @osint
    def facebook(query):
        asyncio.run(Facebook().search(query))

    def help():
        print(f"""
  {coloring.WHITE}-------------------------------------------------- 
  [{coloring.WARNING}!{coloring.WHITE}] Commands: {coloring.BLUE}[command name]{coloring.WHITE}
  {coloring.BLUE}Name:              {coloring.BLUE}Description:
  {coloring.WARNING}help            {coloring.WHITE}Creates specified number of GCs with tokens.
  {coloring.WARNING}clear           {coloring.WHITE}Clears terminal of all print. Alias cls.
  {coloring.WARNING}ascii           {coloring.WHITE}Prints terminal art.
  {coloring.WARNING}exit            {coloring.WHITE}Terminates script.
  {coloring.WARNING}twitter         {coloring.WHITE}Searches Twitter for keyword.
  {coloring.WARNING}facebook        {coloring.WHITE}Check if email has been found in breaches.
  {coloring.WARNING}instagram       {coloring.WHITE}Searches Facebook for keyword
  {coloring.WARNING}facebookapi     {coloring.WHITE}Searches Facebook for keyword using their API.
  {coloring.WARNING}checkpwn        {coloring.WHITE}Check if email has been found in breaches.
  ---------------------------------------------------------------
        """)
###################################################
# Dev Notes #
###################################################
# File made by Roover.
