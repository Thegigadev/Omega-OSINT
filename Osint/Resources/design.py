###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import os
from datetime import datetime
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

  def quit():
    os._exit(1)

  def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
  def ascii():
    console.clear()
    art = f"""{coloring.FAIL}
    
░█████╗░███╗░░░███╗███████╗░██████╗░░█████╗░
██╔══██╗████╗░████║██╔════╝██╔════╝░██╔══██╗
██║░░██║██╔████╔██║█████╗░░██║░░██╗░███████║
██║░░██║██║╚██╔╝██║██╔══╝░░██║░░╚██╗██╔══██║
╚█████╔╝██║░╚═╝░██║███████╗╚██████╔╝██║░░██║
░╚════╝░╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝
    By: Roover & Shell @ Omega Development
    """
    print(art)

  def title():
    if os.name == "nt":
      os.system(f"title OmegaOSINT")
    elif os.name == "linux":
      import subprocess
      subprocess.check_output("Omega OSINT")
    else:
      pass
###################################################