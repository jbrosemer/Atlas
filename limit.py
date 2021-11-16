from gpiozero import Button
button = Button(12)
while True:
    if not button.is_pressed:
        print("BAM")