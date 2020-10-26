import pyautogui as pag
from subprocess import run
from time import sleep

center = (pag.size()[0]/2, pag.size()[1]/2)
hscroll_mult = 38.2*2
scroll_mult = 21.85*2
pos = {
    'repeating_baby': (245, 180)
    }

def applescript_click(menu, item):
    run(['osascript', '-e', f'''tell application "System Events"
tell process "Illustrator"
click menu item "{item}" of menu "{menu}" of menu bar 1
end tell
end tell'''])

def focus_illustrator():
    run(['osascript', '-e', f'''tell application "System Events"
tell process "Illustrator"
set topmost to true
end tell
end tell'''])

def zoom_in():
    applescript_click('View', 'Zoom In')

def zoom_out():
    applescript_click('View', 'Zoom Out')

def reset_view():
    pag.press('esc')
    applescript_click('View', 'Presentation Mode')
    pag.moveTo(list(map(lambda x: x-5, pag.size())))

def scroll(x, y):
    print("uh, scrolling by ", x/100*hscroll_mult, y/100*scroll_mult)
    pag.hscroll(x/100*hscroll_mult)
    pag.scroll(y/100*scroll_mult)

def main():
    zoom_in()
    sleep(1)
    zoom_out()

if __name__ == '__main__':
    focus_illustrator()
    reset_view()
    scroll(50, 50)
    for i in range(10):
        zoom_in()
    input()
    pag.click()
    pag.press('esc')

