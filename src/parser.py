import functions
import sys

f = open(sys.argv[1])

for line in f:
    line = line.strip()
    lineList = line.split(' ')
    command = lineList[0]
    params = lineList[1:]

    if command == 'click':
        if len(params) == 1:
            functions.clickPicture(params)
        else:
            functions.click()
        #print("Click Karo")
    elif command == 'move':
        if len(params) != 2:
            print("chole, move takes 2 params")
            break
        #print(f"Move Karo {params}")
        functions.move(params)
    elif command == 'getinfogui':
        functions.getinfogui()
    elif command == 'doubleclick':
        functions.doubleclick()
    elif command == 'middleclick':
        functions.middleclick()
    elif command == 'rightclick':
        functions.rightclick()
    elif command == 'mousedown':
        functions.mousedown()
    elif command == 'mouseup':
        functions.mouseup()
    elif command == 'wait':
        if len(params) != 1:
            print("wait takes 1 param")
            break
        functions.wait(params)
    elif command == 'drag':
        if len(params) != 3:
            print("drag takes 3 params")
            break
        functions.drag(params)
    elif command == 'scroll':
        if len(params) != 1:
            print("scroll takes 1 param")
            break
        functions.scroll(params)
    elif command == 'type':
        if len(params) != 1:
            print("type takes 1 param")
            break
        functions.typeF(params)
    elif command == 'hotkey':
        functions.hotkey(params)
    elif command == 'screenshot':
        functions.screenshot(params)
    else:
        print("Command Not Found")
        break


f.close()
