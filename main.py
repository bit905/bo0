def on_button_pressed_a():
    RingbitCar.running_time(RingbitCar.Direction_run.BACKWARD, 3)
    basic.show_icon(IconNames.HAPPY)
    basic.show_string(" search in makecode bo0")
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function():
    basic.show_leds("""
        . . . . .
        . # # # .
        # # # # #
        # # . # #
        . # # # .
        """)
    music._play_default_background(music.built_in_playable_melody(Melodies.BLUES),
        music.PlaybackMode.IN_BACKGROUND)
    music._play_default_background(music.built_in_playable_melody(Melodies.BLUES),
        music.PlaybackMode.IN_BACKGROUND)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function)

def on_button_pressed_ab():
    basic.show_string(" Hi a new version of bit os is coming ")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def my_function2():
    basic.show_leds("""
        . # # # .
        . . . . .
        . # . # .
        . # # # .
        . # # # .
        """)
    radio.set_group(1)
    radio.send_number(9086)
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function2)

basic.show_icon(IconNames.HEART)
basic.show_leds("""
    . . # . .
    . # # # .
    # . # . #
    . . # . .
    . . # . .
    """)
basic.show_leds("""
    . . # . .
    . # . . .
    # # # # #
    . # . . .
    . . # . .
    """)
basic.show_leds("""
    . . # . .
    . . . # .
    # # # # #
    . . . # .
    . . # . .
    """)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    """)
basic.show_leds("""
    . . . . .
    # . . . .
    # . . . .
    # . . . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    # . . . .
    # . . . .
    # . . . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    # # . . .
    # # . . .
    # # . . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    # # # . .
    # # # . .
    # # # . .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    # # # # .
    # # # # .
    # # # # .
    . . . . .
    """)
basic.show_leds("""
    . . . . .
    # # # # #
    # # # # #
    # # # # #
    . . . . .
    """)
basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.SQUARE)
basic.show_icon(IconNames.SMALL_SQUARE)
basic.show_icon(IconNames.SQUARE)
basic.show_leds("""
    . # # # .
    # # . # #
    # . # . #
    # # . # #
    . # # # .
    """)
basic.show_number(1567)
basic.show_string("bit os 0.0")
joystickbit.init_joystick_bit()
joystickbit.Vibration_Motor(100)
basic.show_icon(IconNames.HOUSE)