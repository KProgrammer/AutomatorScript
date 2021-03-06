# AutomatorScript
**Ez Language for noobs who cant do python but are too lazy to do simple stuff**

## Commands

- `move <x> <y>`

  To move the mouse cursor to point (x, y)

- `move <image>`

    If you provide the path of the image, it moves the pointer to the image if found

- `move <x> <y> <duration>`

    Moves the cursor to the (x, y) coordinate in `duration` units(default is 25)

- `move |picture|`

    Moves the cursor to the picture assigned to waitP method

- `click`
  
  (Left) Clicks the mouse
  
- `getinfogui`

  Opens up the GUI to make it easier to get the coordinates
  
- `doubleclick`

  Double Clicks the mouse
  
- `middleclick`

  Middle Click
  
- `rightclick`

  Right Clicks at the mouse location
  
- `wait <t>`

  Waits for `t` seconds
  
- `drag <x> <y> <button>`

  Drags from the current mouse to position (x, y) using `button` button(left, right, or middle)
  
- `scroll <units>`

  Scrolls down `units` units(Can be negative to scroll upwards)
  
- `type <text>`  

  Types `text` wherever the keyboard is focused(You may have to click the location before typing)
  
- `hotkey <key1> <key2> ...... ` 

  Presses multiple keys at once to initiate shortcuts like Ctrl-S the keys could be ctrl, alt or any number or alphabet
  
- `waitP <picture>`

    Waits for the picture to appear on the screen and sets `|picture|` so you can use it in move
- `screenshot <file>`
 
   Takes a screenshot of the screen and saves it to `file`

- `math <expression>`

    Prints out the output of the mathematical expression
- ```
    loop <number/expression>
    ....
    ....
    ....
    endloop
    ```
    Loops a block of code a particular number of times
  
## How to run an autoscript

You will need to download python, and have pyautogui installed(which can be easily done by `pip install pyautogui` in the cmd)
You will also need to change the PATH so you can run `autoscript` command in the cmd

Then create a new file named `first.autoscript`

Fill it with this command 
`move 100 100`

You should then be able to run `autoscript  first.autoscript` in the cmd

After you run this, I recommend you to run `getinfogui` in an autoscript file, and you should be able to see the proper positions to make automation easier
  
## Use Templating to dynamically fill elements in an autoscript

Sometimes you have a value which changes constantly and you want to dynamically fill the content based on some logic. Templating helps you do that. 

We are gonna need 3 files for this

- Python file with the logic, we are gonna call it main.py
- Autoscript Template file, which for this example is gonna be temp.atemplate
- Autoscript File which is gonna hold the output for the template, which is ,for this example, auto.autoscript

First, write the template, in which the dynamic elements are between curly braces({name}).
```
move 100 100
click
type {name}
```

After that, in main.py, import src/templater.py as templater or whatever name you prefer. Then you can write 
```python
name = "KProgrammer"
templater.fill_template('temp.atemplate', 'auto.autoscript', name=name)
```

Then when you run the python file you will see that auto.autoscript looks something like this
```
move 100 100
click
type KProgrammer
```

Then 

  
  
