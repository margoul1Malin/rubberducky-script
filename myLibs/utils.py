from usb.device.keyboard import KeyboardInterface, KeyCode
import time
import os

def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Ignorer les lignes vides ou les commentaires
            if line.strip() and not line.strip().startswith("#"):
                key, value = line.strip().split("=", 1)
                config[key.strip()] = value.strip()
    return config

#Utils
SPACE = KeyCode.SPACE
BACKSPACE = KeyCode.BACKSPACE
ENTER = KeyCode.ENTER
ESCAPE = KeyCode.ESCAPE
TAB = KeyCode.TAB

LSHIFT = KeyCode.LEFT_SHIFT
RSHIFT = KeyCode.RIGHT_SHIFT

LALT = KeyCode.LEFT_ALT
RALT = KeyCode.RIGHT_ALT

LCTRL = KeyCode.LEFT_CTRL
RCTRL = KeyCode.RIGHT_CTRL

RIGHT = KeyCode.RIGHT
LEFT = KeyCode.LEFT
DOWN = KeyCode.DOWN
UP = KeyCode.UP

#<> for Azerty FR
INFERIOR = 100
SUPERIOR = (KeyCode.LEFT_SHIFT, INFERIOR)

#Miscellanous
LINUX_TERMINAL = (LCTRL, LALT, KeyCode.T)
MAC_TERMINAL = (KeyCode.LEFT_UI, SPACE) 
WINDOWS_POWERSHELL = (KeyCode.LEFT_UI)
#Debug

#Mappage
azertyFR = {
    #Letters
    'a': KeyCode.Q, 'b': KeyCode.B, 'c': KeyCode.C, 'd': KeyCode.D,
    'e': KeyCode.E, 'f': KeyCode.F, 'g': KeyCode.G, 'h': KeyCode.H,
    'i': KeyCode.I, 'j': KeyCode.J, 'k': KeyCode.K, 'l': KeyCode.L,
    'm': KeyCode.SEMICOLON, 'n': KeyCode.N, 'o': KeyCode.O, 'p': KeyCode.P,
    'q': KeyCode.A, 'r': KeyCode.R, 's': KeyCode.S, 't': KeyCode.T,
    'u': KeyCode.U, 'v': KeyCode.V, 'w': KeyCode.Z, 'x': KeyCode.X,
    'y': KeyCode.Y, 'z': KeyCode.W,
    
    #Special Chars
    'à': KeyCode.N0, '&': KeyCode.N1, 'é': KeyCode.N2, '"': KeyCode.N3,
    "'": KeyCode.N4, '(': KeyCode.N5, '-': KeyCode.N6, 'è': KeyCode.N7,
    '_': KeyCode.N8, 'ç': KeyCode.N9, ')': KeyCode.MINUS, '=': KeyCode.EQUAL, '+': (KeyCode.LEFT_SHIFT, KeyCode.EQUAL),
    
    #Numbers
    '1': (KeyCode.LEFT_SHIFT, KeyCode.N1), '2': (KeyCode.LEFT_SHIFT, KeyCode.N2), '3': (KeyCode.LEFT_SHIFT, KeyCode.N3),
    '4': (KeyCode.LEFT_SHIFT, KeyCode.N4), '5': (KeyCode.LEFT_SHIFT, KeyCode.N5), '6': (KeyCode.LEFT_SHIFT, KeyCode.N6),
    '7': (KeyCode.LEFT_SHIFT, KeyCode.N7), '8': (KeyCode.LEFT_SHIFT, KeyCode.N8), '9': (KeyCode.LEFT_SHIFT, KeyCode.N9),
    '0': (KeyCode.LEFT_SHIFT, KeyCode.N0), 
    
    #Utils & Special Chars
    '´': (KeyCode.RIGHT_ALT, KeyCode.N1), '~': (KeyCode.RIGHT_ALT, KeyCode.N2), '#': (KeyCode.RIGHT_ALT, KeyCode.N3),
    '{': (KeyCode.RIGHT_ALT, KeyCode.N4), '[': (KeyCode.RIGHT_ALT, KeyCode.N5), '|': (KeyCode.RIGHT_ALT, KeyCode.N6),
    '`': (KeyCode.RIGHT_ALT, KeyCode.N7), '\\': (KeyCode.RIGHT_ALT, KeyCode.N8), '^': (KeyCode.RIGHT_ALT, KeyCode.N9),
    '@': (KeyCode.RIGHT_ALT, KeyCode.N0), ']': (KeyCode.RIGHT_ALT, KeyCode.MINUS), '}': (KeyCode.RIGHT_ALT, KeyCode.EQUAL),
    '/': (KeyCode.LEFT_SHIFT, KeyCode.DOT), 
    
    ' ': KeyCode.SPACE,
    
    '.': (KeyCode.LEFT_SHIFT, KeyCode.COMMA),
    ',': KeyCode.M,
    ';': KeyCode.COMMA,
    ':': KeyCode.DOT,
    
    '!': KeyCode.SLASH,
    '?': (KeyCode.LEFT_SHIFT, KeyCode.M),
    '$': KeyCode.CLOSE_BRACKET,
    '>': SUPERIOR,
    '<': INFERIOR,
    '*': KeyCode.BACKSLASH,
}

qwertyUS = {
    # Letters
    'a': KeyCode.A, 'b': KeyCode.B, 'c': KeyCode.C, 'd': KeyCode.D,
    'e': KeyCode.E, 'f': KeyCode.F, 'g': KeyCode.G, 'h': KeyCode.H,
    'i': KeyCode.I, 'j': KeyCode.J, 'k': KeyCode.K, 'l': KeyCode.L,
    'm': KeyCode.M, 'n': KeyCode.N, 'o': KeyCode.O, 'p': KeyCode.P,
    'q': KeyCode.Q, 'r': KeyCode.R, 's': KeyCode.S, 't': KeyCode.T,
    'u': KeyCode.U, 'v': KeyCode.V, 'w': KeyCode.W, 'x': KeyCode.X,
    'y': KeyCode.Y, 'z': KeyCode.Z,
    
    # Numbers (direct keys)
    '1': KeyCode.N1, '2': KeyCode.N2, '3': KeyCode.N3, '4': KeyCode.N4,
    '5': KeyCode.N5, '6': KeyCode.N6, '7': KeyCode.N7, '8': KeyCode.N8,
    '9': KeyCode.N9, '0': KeyCode.N0,
    
    # Shifted Numbers (special characters)
    '!': (KeyCode.LEFT_SHIFT, KeyCode.N1), '@': (KeyCode.LEFT_SHIFT, KeyCode.N2),
    '#': (KeyCode.LEFT_SHIFT, KeyCode.N3), '$': (KeyCode.LEFT_SHIFT, KeyCode.N4),
    '%': (KeyCode.LEFT_SHIFT, KeyCode.N5), '^': (KeyCode.LEFT_SHIFT, KeyCode.N6),
    '&': (KeyCode.LEFT_SHIFT, KeyCode.N7), '*': (KeyCode.LEFT_SHIFT, KeyCode.N8),
    '(': (KeyCode.LEFT_SHIFT, KeyCode.N9), ')': (KeyCode.LEFT_SHIFT, KeyCode.N0),
    
    # Special characters (direct keys)
    '-': KeyCode.MINUS, '=': KeyCode.EQUAL, '[': KeyCode.OPEN_BRACKET, ']': KeyCode.CLOSE_BRACKET,
    '\\': KeyCode.BACKSLASH, ';': KeyCode.SEMICOLON, "'": KeyCode.QUOTE,
    '`': KeyCode.GRAVE, ',': KeyCode.COMMA, '.': KeyCode.DOT, '/': KeyCode.SLASH,
    
    # Shifted special characters
    '_': (KeyCode.LEFT_SHIFT, KeyCode.MINUS), '+': (KeyCode.LEFT_SHIFT, KeyCode.EQUAL),
    '{': (KeyCode.LEFT_SHIFT, KeyCode.OPEN_BRACKET), '}': (KeyCode.LEFT_SHIFT, KeyCode.CLOSE_BRACKET),
    '|': (KeyCode.LEFT_SHIFT, KeyCode.BACKSLASH), ':': (KeyCode.LEFT_SHIFT, KeyCode.SEMICOLON),
    '"': (KeyCode.LEFT_SHIFT, KeyCode.QUOTE), '~': (KeyCode.LEFT_SHIFT, KeyCode.GRAVE),
    '<': (KeyCode.LEFT_SHIFT, KeyCode.COMMA), '>': (KeyCode.LEFT_SHIFT, KeyCode.DOT),
    '?': (KeyCode.LEFT_SHIFT, KeyCode.SLASH),
    
    # Miscellaneous
    ' ': KeyCode.SPACE,
}

#Parse Strings(COMMANDS) to sendable keys
def stringSeq(string):
    
    config = read_config("config.txt")
    language = config["lang"]
    
    keycodes = []
    if language == "FR":
        for char in string:
            if char.isupper():
                keycodes.append((KeyCode.LEFT_SHIFT, azertyFR[char.lower()]))
            elif char in azertyFR:
                key = azertyFR[char]
                if isinstance(key, tuple):  # Cas des combinaisons (SHIFT, etc.)
                    keycodes.append(key)
                else:
                    keycodes.append((key,))
            else:
                raise ValueError(f"Caractère Incompatible :")
    elif language == "US":
        for char in string:
            if char.isupper():
                keycodes.append((KeyCode.LEFT_SHIFT, qwertyUS[char.lower()]))
            elif char in qwertyUS:
                key = qwertyUS[char]
                if isinstance(key, tuple):  # Cas des combinaisons (SHIFT, etc.)
                    keycodes.append(key)
                else:
                    keycodes.append((key,))
            else:
                raise ValueError(f"Caractère Incompatible :")
    return keycodes

#Function to Send Keys Properly
def sendKeys(seq, parameter, timesleep):
    
    for key in seq:
        if isinstance(key, tuple):
            if key == LINUX_TERMINAL:
                parameter.send_keys(list(key))
                time.sleep(0.3)
            else:
                parameter.send_keys(list(key))
        elif isinstance(key, str):  # Si la clé est une chaîne (caractère Unicode)
            parameter.send_keys([key])
        else:
            parameter.send_keys([key])
            
        time.sleep(timesleep)
        parameter.send_keys([])
        time.sleep(timesleep)