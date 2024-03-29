from taipy import Gui
from math import cos, exp


page = """
#This is *Taipy* GUI

A value: <|{decay}|>.

A slider: <br />
<|{decay}|slider|>

My chart:
<|{data}|chart|>
"""

def compute_data(decay):
    return [cos(i/16) * exp(-i*decay/6000) for i in range(720)]

# listens for changes in a page and updates the state
def on_change(state, var_name, var_value):
    if var_name == 'decay':
        computed = compute_data(var_value)
        state.data = computed


decay = 10
data = compute_data(decay) 

Gui(page=page).run()
