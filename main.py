from taipy import Gui

var_name = 'Piotr'

Gui(page="Hi <|{var_name}|>").run(dark_mode=False)
