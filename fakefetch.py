#!/usr/bin/python
#made by JackCDK
#all ascii art is from: http://chris.com/ascii/
import argparse, getpass, platform, os
from colorama import *


#details

windowm = "Openbox" #window manager
distro =  "Debian 8.5 Jessie" #distro
#change these to fit your liking


#ascii pics

randomtest = '''
  \033[41m  \033[49m
  \033[41m  \033[49m  \033[41m  \033[49m          \033[32m[{}]
  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m      \033[32m[OS]:\033[39m {}
  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m  \033[32m[Kernel]:\033[39m {}
  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m  \033[32m[WM]:\033[39m {}
  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m
  \033[41m  \033[49m  \033[41m  \033[49m  \033[41m  \033[49m
  \033[41m  \033[49m  \033[41m  \033[49m
  \033[41m  \033[49m
'''.format(getpass.getuser(),distro,platform.release(),windowm)


noascii = '''

\033[32m[{}]
\033[32m[OS]:\033[39m {}
\033[32m[Kernel]:\033[39m {}
\033[32m[WM]:\033[39m {}

'''.format(getpass.getuser(),distro,platform.release(),windowm)


anchor = '''
        \033[37m _
        \033[37m(_)         \033[32m[{}]
         \033[37m|          \033[32m[OS]:\033[39m {}
    \033[37m()---|---()     \033[32m[Kernel]:\033[39m {}
         \033[37m|          \033[32m[WM]:\033[39m {}
         \033[37m|
 \033[37m __     |     __   \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
 \033[37m|\     /^\     /|
   \033[37m'..-'   '-..'
     \033[37m`-._ _.-`
         \033[37m`\033[39m
'''.format(getpass.getuser(),distro,platform.release(),windowm)

tux = '''
       \033[37ma8888b.
      \033[37md888888b.     \033[32m[{}]
      \033[37m8P YP Y88     \033[32m[OS]:\033[39m {}
      \033[37m8|o||o|88     \033[32m[Kernel]:\033[39m {}
      \033[37m8'    .88     \033[32m[WM]:\033[39m {}
      \033[37m8`._.' Y8.
     \033[37md/      `8b.   \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
    \033[37mdP   .    Y8b.
   \033[37md8:'  "  `::88b
  \033[37md8"         'Y88b
 \033[37m:8P    '      :888
'''.format(getpass.getuser(),distro,platform.release(),windowm)

colortest = '''

 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m
 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m
 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m
 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m
 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m
 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m
 \033[40m black \033[41m red \033[42m green \033[43m yellow \033[44m blue \033[45m purple \033[46m cyan \033[47m grey\033[48m \033[49m

 '''

#arg stuff

parser = argparse.ArgumentParser()
parser.add_argument('-l','--logo', choices=['anchor', 'tux','noascii','ctest'], default='anchor', help='choose ascii logo')
args = parser.parse_args()
if args.logo == "anchor":
    os.system("clear")
    print(anchor)

elif args.logo == "tux":
    os.system("clear")
    print(tux)

elif args.logo == "noascii":
    os.system("clear")
    print(noascii)

elif args.logo == "ctest":
    os.system("clear")
    print(colortest)
