import subprocess
import sys
import win32clipboard as wclip
from typing import List

def SQLlist(items: List[str]) -> str:
    newstr = "(" + ', '.join("'"+i+"'" for i in items) + ")"
    return newstr

def fail():
    print("Usage: SQLList.py x y z a b c")
    print("Or - simply copy a list before running")

def ctrlC(text: str):
    text = str(text.strip())
    cmd = f'echo {text} | clip' # make sure created text is actually a string
    echop = subprocess.Popen(cmd, shell=True)
    print(f"{newstr}\nAbove string is copied to clipboard")
    return echop.communicate()[0]

def GetClip() -> List[str]:
    # checks clipboard
    wclip.OpenClipboard()
    try:
        data = wclip.GetClipboardData()

        # split priority: newline (\r\n) -> commas (,) -> space (' ')
        if '\r\n' in data: 
            data = data.split('\r\n')
        elif ',' in data:
            data = data.split(',')
        else:
            data = data.split()
    except TypeError:
        # If the clipboard is not a UTF8 string...
        data = None

    wclip.CloseClipboard()
    return data

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        newstr = SQLlist(args)
        ctrlC(newstr)
        
    elif GetClip(): # needs refactor? func is called twice
        print("Grabbing Clipboard....")
        items = GetClip()
        newstr = SQLlist(items)
        ctrlC(newstr)
    else:
        fail()
    
    input("Press Enter to exit...")
    