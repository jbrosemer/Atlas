from gpiozero import Button
button = Button(12)
while True:
    if button.is_pressed:
        print("hello")
    else
        print("hi")