import pygaze
from pygaze import eye

# Initialize the eye tracker
tracker = eye.init()

def get_eye_position():
    # Get the current eye position (x, y)
    return tracker.get_gaze_position()

def type_character(char):
    # Map gaze coordinates to character selection
    x, y = get_eye_position()
    if x < 0.5:
        return 'a'
    elif x > 0.7:
        return 'b'
    elif y < 0.3:
        return 'c'
    elif y > 0.6:
        return 'd'

def type_text(text):
    # Initialize an empty string to store the typed text
    typed_text = ''
    for char in text:
        if char.isalpha():
            typed_text += type_character(char)
        else:
            typed_text += char
    print(typed_text)

# Test the typing system
test_text = "Hello, World!"
type_text(test_text)
