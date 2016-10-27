#!/usr/bin/python
#made by JackCDK
#add your own info in. I'm not gonna add hardware/os dection but, you can.
#all ascii art is from: http://chris.com/ascii/
import argparse, getpass, platform, os
from colorama import *

#color guide
# "\033[37m"   white
# "\033[33m"   black
# "\033[31m"   red
# "\033[32m"   green
# "\033[33m"   yellow
# "\033[34m"   blue
# "\033[35m"   magenta
# "\033[36m"   cyan

#ascii logos

anchor = '''
        \033[37m _
        \033[37m(_)         \033[32m[{}]
         \033[37m|          \033[32m[OS]:\033[39m Debian 8.6 jessie
    \033[37m()---|---()     \033[32m[Kernel]:\033[39m {}
         \033[37m|          \033[32m[WM]:\033[39m OpenBox
         \033[37m|
 \033[37m __     |     __
 \033[37m|\     /^\     /|
   \033[37m'..-'   '-..'
     \033[37m`-._ _.-`
         \033[37m`\033[39m
'''.format(getpass.getuser(),platform.release())

tux = '''
       \033[37ma8888b.
      \033[37md888888b.     \033[32m[{}]
      \033[37m8P"YP"Y88     \033[32m[OS]: \033[39mDebian 8.6 jessie
      \033[37m8|o||o|88     \033[32m[Kernel]: \033[39m {}
      \033[37m8'    .88     \033[32m[WM]:\033[39m OpenBox
      \033[37m8`._.' Y8.
     \033[37md/      `8b.
    \033[37mdP   .    Y8b.
   \033[37md8:'  "  `::88b
  \033[37md8"         'Y88b
 \033[37m:8P    '      :888
'''.format(getpass.getuser(),platform.release())



#arg stuff

parser = argparse.ArgumentParser()
parser.add_argument('-l','--logo', choices=['anchor', 'tux',], default='anchor', help='choose ascii logo')


args = parser.parse_args()
if args.logo == "anchor":
    print(anchor)

elif args.logo == "tux":
	print(tux)
