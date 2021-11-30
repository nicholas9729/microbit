let n1 = 0
let temp = 0
let game2 = 0
let n2 = 0
let ans = 0
// basic.forever(function () {
// 
// if (input.isGesture(Gesture.Shake)) {
// 
// }
// 
// })
input.onButtonPressed(Button.A, function () {
    if (n1 < temp) {
        temp += -1
        basic.showNumber(temp)
    }
})
input.onGesture(Gesture.Shake, function () {
    if (game2 == 0) {
        n1 = 1
        n2 = 10
        ans = randint(n1, n2)
        temp = 0
        // basic.show_number(n2)
        game2 = 1
        // basic.show_number(n1)
        basic.showString("" + n1 + "-" + ("" + n2))
    } else {
        basic.showString("" + n1 + "-" + ("" + n2))
    }
    basic.showString("?")
})
input.onButtonPressed(Button.AB, function () {
    if (ans < temp) {
        n2 = temp
        // basic.show_number(n1)
        basic.showString("" + n1 + "-" + ("" + n2))
    } else if (ans > temp) {
        // basic.show_number(n2)
        n1 = temp
        // basic.show_number(n1)
        basic.showString("" + n1 + "-" + ("" + n2))
    } else {
        // basic.show_number(n2)
        basic.showIcon(IconNames.Happy)
        game2 = 0
    }
    if (game2 != 0) {
        basic.showString("?")
    }
})
input.onButtonPressed(Button.B, function () {
    if (n2 > temp) {
        temp += 1
        basic.showNumber(temp)
    }
})
