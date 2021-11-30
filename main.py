n1 = 0
temp = 0
game2 = 0
n2 = 0
ans = 0
# basic.forever(function () {
# 
# if (input.isGesture(Gesture.Shake)) {
# 
# }
# 
# })

def on_button_pressed_a():
    if n1 < temp:
        basic.show_number(temp)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global n1, n2, ans, temp, game2
    if game2 == 0:
        n1 = 1
        n2 = 10
        ans = randint(n1, n2)
        temp = 5
        # basic.show_number(n2)
        game2 = 1
        # basic.show_number(n1)
        basic.show_string("" + str(n1) + "-" + ("" + str(n2)))
    else:
        basic.show_string("" + str(n1) + "-" + ("" + str(n2)))
    basic.show_string("?")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global n2, n1, game2
    if ans < temp:
        n2 = temp
        # basic.show_number(n1)
        basic.show_string("" + str(n1) + "-" + ("" + str(n2)))
    elif ans > temp:
        # basic.show_number(n2)
        n1 = temp
        # basic.show_number(n1)
        basic.show_string("" + str(n1) + "-" + ("" + str(n2)))
    else:
        # basic.show_number(n2)
        basic.show_icon(IconNames.HAPPY)
        game2 = 0
    if game2 != 0:
        basic.show_string("?")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if n2 > temp:
        basic.show_number(temp)
input.on_button_pressed(Button.B, on_button_pressed_b)
