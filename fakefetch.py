#!/usr/bin/python
#made by JackCDK
#add your own info in. I'm not gonna add hardware/os dection but, you can.
#all ascii art is from: http://chris.com/ascii/
import argparse

#ascii logos

anchor = '''
         _
        (_)         [techgnome]
         |          [OS]: Debian 8.6 jessie
    ()---|---()     [Kernel]: x86_64 Linux 3.16.0-4-amd64
         |          [WM]: OpenBox
         |
  __     |     __
 |\     /^\     /|
   '..-'   '-..'
     `-._ _.-`
         `
'''
axe = '''
     ,  /\  .       [techgnome]
    //`-||-'\\      [OS]: Debian 8.6 jessie
   (| -=||=- |)     [Kernel]: x86_64 Linux 3.16.0-4-amd64
    \\,-||-.//      [WM]: OpenBox
     `  ||  '
        ||
        ||
        ||
        ||
        ||
        ()
'''

linux = '''
       a8888b.
      d888888b.     [techgnome]
      8P"YP"Y88     [OS]: Debian 8.6 jessie
      8|o||o|88     [Kernel]: x86_64 Linux 3.16.0-4-amd64
      8'    .88     [WM]: OpenBox
      8`._.' Y8.
     d/      `8b.
    dP   .    Y8b.
   d8:'  "  `::88b
  d8"         'Y88b
 :8P    '      :888
  8a.   :     _a88P
._/"Yaa_:   .| 88P|
\    YP"    `| 8P  `.
/     \.___.d|    .'
`--..__)8888P`._.'


'''



#arg stuff

parser = argparse.ArgumentParser()
parser.add_argument('-l','--logo', choices=['anchor', 'axe', 'linux',], default='anchor', help='choose the ascii art you want')


args = parser.parse_args()
if args.logo == "anchor":
    print(anchor)

elif args.logo == "axe":
	print(axe)

elif args.logo == "linux":
	print(linux)
