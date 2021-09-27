function on_button_pressed_a() {
    
}

input.onButtonPressed(Button.A, function on_button_pressed_a1() {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function on_button_pressed_a2() {
    basic.showIcon(IconNames.Sad)
})
input.onButtonPressed(Button.AB, function on_button_pressed_a3() {
    basic.showIcon(IconNames.Surprised)
    basic.showIcon(IconNames.Silly)
})
