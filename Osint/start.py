###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
from .Resources import *
from .commands import run
###################################################
class inp:
  def __init__(self):
    while True:
        command = input(f"""\n{coloring.BLUE}  ┌──{coloring.BLUE}「{coloring.FAIL}[Ω]OmegaNET{coloring.BLUE}」-[{coloring.WARNING}!{coloring.BLUE}]{coloring.WHITE}:{coloring.BLUE}
  └─{coloring.HEADER}${coloring.WHITE}: """)
        run(command)
###################################################
# Dev Notes #
###################################################
# File made by Roover.
