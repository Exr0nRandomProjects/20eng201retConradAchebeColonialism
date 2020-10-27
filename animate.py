import pyautogui as pag
from subprocess import run
from time import sleep

pos = {
    'repeating_baby': (961, 341),
    'rivets':         (566, 693),
    'boiler':         (977, 700),
    'forest':         (1414, 728)
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

# def zoom_in():
#     applescript_click('View', 'Zoom In')
#
# def zoom_out():
#     applescript_click('View', 'Zoom Out')

def reset_view():
    pag.press('esc')
    applescript_click('View', 'Presentation Mode')
    pag.moveTo(list(map(lambda x: x-5, pag.size())))

# def scroll(x, y):
#     print("uh, scrolling by ", x/100*hscroll_mult, y/100*scroll_mult)
#     pag.hscroll(x/100*hscroll_mult)
#     pag.scroll(y/100*scroll_mult)

def main():
    for visual in pos:
        print('going to ', visual)
        pag.moveTo(pos[visual])
        input('press for next..')

if __name__ == '__main__':
    focus_illustrator()
    reset_view()
    main()
    pag.moveTo(list(map(lambda x: x/2, pag.size())))
    pag.click()
    pag.press('esc')

