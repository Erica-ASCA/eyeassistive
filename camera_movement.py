from webcam_classification import generate_predictions
from pynput.keyboard import Key, Controller

def convert_to_keypress(cap):

    mov_class = generate_predictions(cap)
    print(mov_class)

    keyboard = Controller()

    if mov_class == "Right":
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif mov_class == "Left":
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif mov_class == "Down":
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    elif mov_class == "Up":
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif mov_class == "Closed":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        pass

def convert_to_keypress2(prediction):

    keyboard = Controller()

    if prediction == "Right":
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif prediction == "Left":
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif prediction == "Down":
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    elif prediction == "Up":
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    elif prediction == "Closed":
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    elif prediction == "Center":
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        pass