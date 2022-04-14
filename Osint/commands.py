###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import asyncio
import os
from .Resources import console, coloring
from .Resources.Browsers import *
import random
from .Nodes import *
import string
import inspect
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
###################################################
class run:
    global rand_string
    rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    def __init__(self, command):
        options = {
            "help": run.help,
            "twitter": run.twitter,
            "instagram": run.instagram,
            "checkpwnemail": run.checkpwnemail, 
            "exit": console.quit,
            "clear": console.clear,
            "cls": console.clear,
            "ascii": console.ascii,
            "facebook": run.facebook,
            "facebookapi": run.facebookapi,
            "shodan": run.shodan,
            "shodanreport": run.shodanreport,
            "google": run.google,
            "duckduck": run.duckduck,
            "imagesearch": run.imagesearch,
            "checkpwnpass": run.checkpwnpass
        }
        if command.lower() in options:
            options[command.lower()]()
        else: 
            return
            
    def osint(media):
        global save
        save = True
        def wrapper():
            ask = input(f"{coloring.BLUE}\n  -> Save Result? [y/n] ")
            if ask == "y" or ask == "Y":

                save = True
            else:

                save = False
            if "query" and "i" in inspect.signature(media).parameters:
                query = str(input(f"{coloring.BLUE}\n  -> Enter {media.__name__} query: "))
                amount = int(input(f"{coloring.BLUE}\n  -> Enter amount of searches: "))
                media(query, amount)
                return query, amount
            if "query" in inspect.signature(media).parameters:
                query = str(input(f"{coloring.BLUE}\n  -> Enter {media.__name__} query: "))
                media(query)
                return query
            if "path" in inspect.signature(media).parameters:
                path = str(input(f"{coloring.BLUE}\n  -> Drag image you want to reverse search: "))
                media(path)
                return path
            
            # Add \n to results
        return wrapper

    @osint
    def twitter(query, i:int = None):
        
        resp = asyncio.run(Twitter().search(query, i))
        for searches in resp:
            for url in searches:
                print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for searches in resp:
                    for url in searches:
                        f.write(f"-> Link found: {url}\n")

    @osint
    def instagram(query, i:int=None): 
        
        resp = asyncio.run(Instagram().search(query, i))
        for searches in resp:
            for url in searches:
                print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for searches in resp:
                    for url in searches:
                        f.write(f"-> Link found: {url}\n")
        
        

    @osint
    def checkpwnemail(query):
        
        resp = asyncio.run(pwn.check_email(query))
        for name in resp:
            print(f"{coloring.FAIL}  -> Breach found: {name['Name']}")
        if save:
            with open(f'../output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Breach found: {name['Name']}\n")
        

    @osint
    def checkpwnpass(query):

        resp = asyncio.run(pwn.check_pass(query))
        print(f"{coloring.FAIL}  -> Link found: {resp}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                f.write(f"-> Link found: {resp}\n")

    @osint
    def facebookapi(query):

        resp = asyncio.run(Facebook().search2(query))
        for url in resp:
            print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            print(save)
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Link found: {url}\n")

    @osint
    def facebook(query, i:int=None):
        resp = asyncio.run(Facebook().search(query, i))
        for searches in resp:
            for url in searches:
                print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Link found: {url}\n")
    
    @osint
    def shodan(query):

        resp = asyncio.run(Shodan().search(query))
        for url in resp:
            print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Link found: {url}\n")
        

    @osint
    def shodanreport(query):
        
        resp = asyncio.run(Shodan().report(query))
        print(f"{coloring.FAIL}{resp}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                f.write(f"{resp}\n")
        


    @osint
    def google(query, i:int=None):
        
        resp = asyncio.run(Google().search(query, i))
        for url in resp:
            print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Link found: {url}\n")
        
    
    @osint
    def duckduck(query, i=None):
        
        resp = asyncio.run(DuckDuck().search(query, i))
        for url in resp:
            print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Link found: {url}\n")
        
        
    @osint
    def imagesearch(path):
        
        if "'" in path:
            path = path.replace("'", "")
        resp = asyncio.run(Yandex().image_search(path))
        for url in resp:
            print(f"{coloring.FAIL}  -> Link found: {url}")
        if save:
            with open(f'./output_{rand_string}.txt', 'a+', encoding='utf-8') as f:
                for url in resp:
                    f.write(f"-> Link found: {url}\n")
        



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
  {coloring.WARNING}checkpwnemail       {coloring.WHITE}Check if email has been found in breaches.
  {coloring.WARNING}checkpwnpass        {coloring.WHITE}Check if password has been found in breaches.
  {coloring.WARNING}shodan              {coloring.WHITE}Searches shodan for keyword
  {coloring.WARNING}shodanreport        {coloring.WHITE}Searches shodan reports for keyword
  {coloring.WARNING}google              {coloring.WHITE}Searches google with specific search
  {coloring.WARNING}duckduck            {coloring.WHITE}Searches duckduckgo with specific search
  {coloring.WARNING}imagesearch         {coloring.WHITE}Searches yandex with image search
  ---------------------------------------------------------------
        """)
###################################################
# Dev Notes #
###################################################
# File made by Roover.
