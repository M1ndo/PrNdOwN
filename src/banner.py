# Created By ybenel
from colors import get_colors
from random import shuffle
import threading
import os,sys
from time import sleep as sl
sys.path.insert(1,'ascii')
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
def banner():
    print(get_colors.white()+get_colors.randomize()+"""
           .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'     - Welcome To PrNdOwN!
      `-._   ````    _.-'
          ``-------''
    """+ get_colors.white())
list_choice = ['Nice Choice',"Wow What a taste","Cool Choice","You're Talented", "Ooh I See", "Perfect", "Truly Amazing",'Seems Naughty', 'My Master', 'I Hand You They Key Of Freedom', 'Soo Long My Friend','I Wanna','Dark Side Of My Room',"Start The Engine",'I Can Handle It', 'Meow Meow',"Fuck I'm Not Famous Enough"]
shuffle(list_choice)
for i in list_choice:
    sentence = i
def banner2():
    print(get_colors.white()+get_colors.randomize()+f"""    
      /\_/\ \

 /\  / o o \ \
            
//\\\ \~(*)~/
`  \/   ^ /
   | \|| ||  {sentence}!
   \ '|| ||  
    \)()-())
""" + get_colors.white())
path = os.getcwd()
def banner3():
    files = ['cat1.txt','cat2.txt','cat3.txt','cat4.txt','cat5.txt','cat6.txt']
    frames = []
    for file in files:
        with open(f'{path}\\src\\ascii\\{file}','r') as f:
            frames.append(f.readlines())
    for i in range(0,2):
        for frame in frames:
            print(get_colors.randomize() + "".join(frame) + "     " + get_colors.randomize1() + "I'm Spinning")
            sl(0.01)
            clear()
    
def buggy():
    ascii = []
    with open(f'{path}\\src\\ascii\\buggy.txt','r') as s:
       ascii.appen(s.readlines())
    for asci in ascii:
        print(get_colors.white() + get_colors.randomize()+"".join(asci) + get_colors.white() + "        "+get_colors.randomize()+"Wow How Lucky You're This Only Happens 1 out of 100 (1%)")


def banner4():
    files = ['cat1.txt','cat2.txt','cat3.txt','cat4.txt','cat5.txt','cat6.txt']
    shuffle(files)
    file = files[0]
    ascii = []
    with open(f'{path}\\src\\ascii\\{file}','r') as s:
        ascii.append(s.readlines())
    for asci in ascii:
        print(get_colors.white() + get_colors.randomize2() + "".join(asci) + get_colors.white() + "        " + get_colors.randomize3() + sentence)