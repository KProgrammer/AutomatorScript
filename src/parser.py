import functions
import sys

loop_dic = {
    'commands': [],
    'on': False,
    'times': ""
}


class Command:
    def __init__(self, command, cmd_function, params_len, config={}):
        self.command = command
        self.function = cmd_function
        self.params_len = params_len
        self.config = config

    def run(self, params):
        if len(params) != self.params_len and self.params_len != -1:
            # TODO: Add Error Handling
            print(f"{self.command} requires {self.params_len} parameters")
        else:
            if self.params_len:
                self.function(params)
            else:
                self.function()


f = open(sys.argv[1])


def loop_setter(params):
    global loop_dic
    loop_dic = functions.startLoop(params)


def loopF():
    global loop_dic
    loop_dic["on"] = False
    for i in range(int(functions.doMath([loop_dic["times"]])-1)):
        for new_command in loop_dic["commands"]:
            run(new_command.split(' ')[0], new_command.split(' ')[1:])


def run(command, params):
    global loop_dic
    if loop_dic["on"] and command != 'endloop' and command != 'endloop ':
        loop_dic["commands"].append(command + ' ' + ' '.join(params))

    for new_command in commands:
        if command == new_command.command and new_command.params_len == -1:
            new_command.run(params)
            break
        elif command == new_command.command and len(params) == new_command.params_len:
            new_command.run(params)
            break


commands = [
    Command("move", functions.move, 2),
    Command("move", functions.movePicture, 1),
    Command("move", functions.moveDuration, 3),
    Command("click", functions.click, 0),
    Command("doubleclick", functions.doubleclick, 0),
    Command("middleclick", functions.middleclick, 0),
    Command("rightclick", functions.rightclick, 0),
    Command("getinfogui", functions.getinfogui, 0),
    Command("scroll", functions.scroll, 1),
    Command("type", functions.typeF, 1),
    Command("hotkey", functions.hotkey, -1),
    Command("screenshot", functions.screenshot, 1),
    Command("wait", functions.wait, 1),
    Command("math", functions.doMath, 1),
    Command("loop", loop_setter, 1),
    Command("endloop", loopF, 0),
    Command("print", functions.printF, 1),
    Command("waitP", functions.waitP, 1),
    Command("drag", functions.drag, 3)
]


for line in f:
    line = line.strip()
    lineList = line.split(' ')
    command = lineList[0]
    params = lineList[1:]

    run(command, params)

f.close()
