from taipy import Gui

value = 10

page = """
#This is *Taipy* GUI

A value: <|{value}|>.

A slider: <br />
<|{value}|slider|>
"""

Gui(page=page).run()
