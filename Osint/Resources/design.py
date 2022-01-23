###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import os
###################################################
class coloring:
  HEADER = '\033[95m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  WHITE = '\033[0m'
  BOLD = '\033[1m'
###################################################
class console:
  def __init__(self):
    self.version = open("Resources/version.txt", "r").readline()
    self.devs = "Shell & Roover"

  def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
  def ascii(self):
    console.clear()
    art = f"""{coloring.FAIL}
    
░█████╗░███╗░░░███╗███████╗░██████╗░░█████╗░
██╔══██╗████╗░████║██╔════╝██╔════╝░██╔══██╗
██║░░██║██╔████╔██║█████╗░░██║░░██╗░███████║
██║░░██║██║╚██╔╝██║██╔══╝░░██║░░╚██╗██╔══██║
╚█████╔╝██║░╚═╝░██║███████╗╚██████╔╝██║░░██║
░╚════╝░╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝
    By: {self.devs} @ Omega Development
    """
    return art

  def title():
    if os.name == "nt":
      os.system("title Omega OSINT")
    else:
      import subprocess
      subprocess.check_output("Omega OSINT") 
###################################################