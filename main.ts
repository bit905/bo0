input.onButtonPressed(Button.A, function on_button_pressed_a() {
    RingbitCar.running_time(RingbitCar.Direction_run.backward, 3)
    basic.showIcon(IconNames.Happy)
    basic.showString(" search in makecode bo0")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function my_function() {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        # # . # #
        . # # # .
        `)
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Blues), music.PlaybackMode.InBackground)
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Blues), music.PlaybackMode.InBackground)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString(" Hi a new version of bit os is coming ")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function my_function2() {
    basic.showLeds(`
        . # # # .
        . . . . .
        . # . # .
        . # # # .
        . # # # .
        `)
    radio.setGroup(1)
    radio.sendNumber(9086)
})
basic.showIcon(IconNames.Heart)
basic.showLeds(`
    . . # . .
    . # # # .
    # . # . #
    . . # . .
    . . # . .
    `)
basic.showLeds(`
    . . # . .
    . # . . .
    # # # # #
    . # . . .
    . . # . .
    `)
basic.showLeds(`
    . . # . .
    . . . # .
    # # # # #
    . . . # .
    . . # . .
    `)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . . . . .
    # . . . .
    # . . . .
    # . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    # . . . .
    # . . . .
    # . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    # # . . .
    # # . . .
    # # . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    # # # . .
    # # # . .
    # # # . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    # # # # .
    # # # # .
    # # # # .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    # # # # #
    # # # # #
    # # # # #
    . . . . .
    `)
basic.showIcon(IconNames.Heart)
basic.showIcon(IconNames.Square)
basic.showIcon(IconNames.SmallSquare)
basic.showIcon(IconNames.Square)
basic.showLeds(`
    . # # # .
    # # . # #
    # . # . #
    # # . # #
    . # # # .
    `)
basic.showNumber(1567)
basic.showString("bit os 0.0")
joystickbit.initJoystickBit()
joystickbit.Vibration_Motor(100)
basic.showIcon(IconNames.House)
