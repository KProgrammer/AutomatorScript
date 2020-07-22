import functions
import sys


class Command:
    def __init__(self, command, cmd_function, params_len):
        self.command = command
        self.function = cmd_function
        self.params_len = params_len

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

for line in f:
    line = line.strip()
    lineList = line.split(' ')
    command = lineList[0]
    params = lineList[1:]

    commands = [
        Command("move", functions.move, 2),
        Command("click", functions.click, 0),
        Command("doubleclick", functions.doubleclick, 0),
        Command("middleclick", functions.middleclick, 0),
        Command("rightclick", functions.rightclick, 0),
        Command("click", functions.clickPicture, 1),
        Command("doubleclick", functions.doubleClickPicture, 1),
        Command("middleclick", functions.middleClickPicture, 1),
        Command("rightclick", functions.rightClickPicture, 1),
        Command("getinfogui", functions.getinfogui, 0),
        Command("scroll", functions.scroll, 1),
        Command("type", functions.typeF, 1),
        Command("hotkey", functions.hotkey, -1),
        Command("screenshot", functions.screenshot, 1),
        Command("wait", functions.wait, 1)
    ]

    for new_command in commands:
        if command == new_command.command and new_command.params_len == -1:
            new_command.run(params)
            break
        elif command == new_command.command and len(params) == new_command.params_len:
            new_command.run(params)
            break

f.close()
