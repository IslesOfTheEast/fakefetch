#!/usr/bin/python
#made by JackCDK
#most ascii art is from: http://chris.com/ascii/

import argparse, getpass, platform, os
from colorama import *

#details

windowm = "Openbox" #window manager
distro =  "GNU/Linux" #Distro Name
#change these to fit your liking, I am trying to find a way to automate this, so hang in there.


#ascii soundwave by me

wave = '''
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

#linux distro art (from screenfetch)

deb_logo = '''
         \033[31m_,met$$$$$gg.
      \033[31m,g$$$$$$$$$$$$$$$P.      \033[32m[{}]
    \033[31m,g$$P""          Y$$. .    \033[32m[OS]:\033[39m {}
   \033[31m,$$P'              `$$$.    \033[32m[Kernel]:\033[39m {}
  \033[31m ,$$P       ,ggs.     `$$b:  \033[32m[WM]:\033[39m {}
  \033[31m`d$$'     ,$P"'   .    $$$
   \033[31m$$P      d$'     ,    $$P   \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
   \033[31m$$:      $$.   -    ,d$$
   \033[31m$$\;      Y$b._   _,d$P
   \033[31mY$$.    `.`"Y$$$$P"
   \033[31m`$$b      "-.__
    \033[31m`Y$$
     \033[31m`Y$$.
       \033[31m`$$b.
         \033[31m`Y$$b.
            \033[31m`"Y$b._
                \033[31m`""""\033[39m'''.format(getpass.getuser(),distro,platform.release(),windowm)




arch_logo = '''
                   \033[36m-`
                  \033[36m.o+`         \033[32m[{}]
                 \033[36m`ooo/         \033[32m[OS]:\033[39m {}
                \033[36m`+oooo:        \033[32m[Kernel]:\033[39m {}
               \033[36m`+oooooo:       \033[32m[WM]:\033[39m {}
               \033[36m-+oooooo+:
             \033[36m`/:-:++oooo+:     \033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m \033[48m \033[49m
            \033[36m`/++++/+++++++:
           \033[36m`/++++++++++++++:
          \033[36m`/+++ooooooooooooo/`
         \033[36m./ooosssso++osssssso+`
        \033[36m.oossssso-````/ossssss+`
       \033[36m-osssssso.      :ssssssso.
      \033[36m:osssssss/        osssso+++.
     \033[36m/ossssssss/        +ssssooo/-
   \033[36m`/ossssso+/:-        -:/+osssso+-
  \033[36m`+sso+:-`                 `.-/+oso:
 \033[36m`++:.                           `-/+/
 \033[36m.`                                 `/'\033[39m'''.format(getpass.getuser(),distro,platform.release(),windowm)


#ascii art from chris.com

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

#my own color test

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
parser.add_argument('-l','--logo', choices=['anchor','tux','debian','arch','noascii','soundwave','ct'], default='anchor', help='choose ascii logo')
args = parser.parse_args()
if args.logo == "anchor":
    os.system("clear")
    print(anchor)

elif args.logo == "tux":
    os.system("clear")
    print(tux)

elif args.logo == "arch":
    os.system("clear")
    print(arch_logo)

elif args.logo == "debian":
    os.system("clear")
    print(deb_logo)

elif args.logo == "noascii":
    os.system("clear")
    print(noascii)

elif args.logo == "ct":
    os.system("clear")
    print(colortest)

elif args.logo == "soundwave":
    os.system("clear")
    print(wave)
