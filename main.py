def on_button_pressed_a():
    pass
def on_button_pressed_a1():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a1)
def on_button_pressed_a2():
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_a2)
def on_button_pressed_a3():
    basic.show_icon(IconNames.SURPRISED)
    basic.show_icon(IconNames.SILLY)
input.on_button_pressed(Button.AB, on_button_pressed_a3)