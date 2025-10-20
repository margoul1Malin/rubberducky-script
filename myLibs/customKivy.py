from .utils import *
from usb.device.keyboard import KeyCode as kc

def rootLang(language):
    global kcA
    global kcB
    global kcC
    global kcD
    global kcE
    global kcF
    global kcG
    global kcH
    global kcI
    global kcJ
    global kcK
    global kcL
    global kcM
    global kcN
    global kcO
    global kcP
    global kcQ
    global kcR
    global kcS
    global kcT
    global kcU
    global kcV
    global kcW
    global kcX
    global kcY
    global kcZ

    global kcN1
    global kcN2
    global kcN3
    global kcN4
    global kcN5
    global kcN6
    global kcN7
    global kcN8
    global kcN9
    global kcN0

    global kcENTER
    global kcESCAPE
    global kcBACKSPACE
    global kcTAB
    global kcSPACE
    global kcMINUS
    global kcEQUAL
    global kcOPEN_BRACKET
    global kcCLOSE_BRACKET
    global kcBACKSLASH
    global kcHASH
    global kcSEMICOLON
    global kcQUOTE
    global kcGRAVE
    global kcCOMMA
    global kcDOT
    global kcSLASH

    global kcCAPS_LOCK
    global kcF1
    global kcF2
    global kcF3
    global kcF4
    global kcF5
    global kcF6
    global kcF7
    global kcF8
    global kcF9
    global kcF10
    global kcF11
    global kcF12
    global kcPRINTSCREEN
    global kcSCROLL_LOCK
    global kcPAUSE
    global kcINSERT
    global kcHOME
    global kcPAGEUP
    global kcDELETE
    global kcEND
    global kcPAGEDOWN
    global kcRIGHT
    global kcLEFT
    global kcDOWN
    global kcUP

    global kcKP_NUM_LOCK
    global kcKP_DIVIDE
    global kcKP_AT
    global kcKP_MULTIPLY
    global kcKP_MINUS
    global kcKP_PLUS
    global kcKP_ENTER
    global kcKP_1
    global kcKP_2
    global kcKP_3
    global kcKP_4
    global kcKP_5
    global kcKP_6
    global kcKP_7
    global kcKP_8
    global kcKP_9
    global kcKP_0

    global kcLEFT_CTRL
    global kcLEFT_SHIFT
    global kcLEFT_ALT
    global kcLEFT_UI
    global kcRIGHT_CTRL
    global kcRIGHT_SHIFT
    global kcRIGHT_ALT
    global kcRIGHT_UI
    
    if language == "FR":
        kcA = kc.Q
        kcB = kc.B
        kcC = kc.C
        kcD = kc.D
        kcE = kc.E
        kcF = kc.F
        kcG = kc.G
        kcH = kc.H
        kcI = kc.I
        kcJ = kc.J
        kcK = kc.K
        kcL = kc.L
        kcM = kc.SEMICOLON
        kcN = kc.N
        kcO = kc.O
        kcP = kc.P
        kcQ = kc.A
        kcR = kc.R
        kcS = kc.S
        kcT = kc.T
        kcU = kc.U
        kcV = kc.V
        kcW = kc.Z
        kcX = kc.X
        kcY = kc.Y
        kcZ = kc.W

        kcN1 = kc.N1
        kcN2 = kc.N2
        kcN3 = kc.N3
        kcN4 = kc.N4
        kcN5 = kc.N5
        kcN6 = kc.N6
        kcN7 = kc.N7
        kcN8 = kc.N8
        kcN9 = kc.N9
        kcN0 = kc.N0

        kcENTER = kc.ENTER
        kcESCAPE = kc.ESCAPE
        kcBACKSPACE = kc.BACKSPACE
        kcTAB = kc.TAB
        kcSPACE = kc.SPACE
        kcMINUS = kc.MINUS
        kcEQUAL = kc.EQUAL
        kcOPEN_BRACKET = kc.OPEN_BRACKET
        kcCLOSE_BRACKET = kc.CLOSE_BRACKET
        kcBACKSLASH = kc.BACKSLASH
        kcHASH = kc.HASH
        kcSEMICOLON = kc.SEMICOLON
        kcQUOTE = kc.QUOTE
        kcGRAVE = kc.GRAVE
        kcCOMMA = kc.COMMA
        kcDOT = kc.DOT
        kcSLASH = kc.SLASH

        kcCAPS_LOCK = kc.CAPS_LOCK
        kcF1 = kc.F1
        kcF2 = kc.F2
        kcF3 = kc.F3
        kcF4 = kc.F4
        kcF5 = kc.F5
        kcF6 = kc.F6
        kcF7 = kc.F7
        kcF8 = kc.F8
        kcF9 = kc.F9
        kcF10 = kc.F10
        kcF11 = kc.F11
        kcF12 = kc.F12
        kcPRINTSCREEN = kc.PRINTSCREEN
        kcSCROLL_LOCK = kc.SCROLL_LOCK
        kcPAUSE = kc.PAUSE
        kcINSERT = kc.INSERT
        kcHOME = kc.HOME
        kcPAGEUP = kc.PAGEUP
        kcDELETE = kc.DELETE
        kcEND = kc.END
        kcPAGEDOWN = kc.PAGEDOWN
        kcRIGHT = kc.RIGHT
        kcLEFT = kc.LEFT
        kcDOWN = kc.DOWN
        kcUP = kc.UP

        kcKP_NUM_LOCK = kc.KP_NUM_LOCK
        kcKP_DIVIDE = kc.KP_DIVIDE
        kcKP_AT = kc.KP_AT
        kcKP_MULTIPLY = kc.KP_MULTIPLY
        kcKP_MINUS = kc.KP_MINUS
        kcKP_PLUS = kc.KP_PLUS
        kcKP_ENTER = kc.KP_ENTER
        kcKP_1 = kc.KP_1
        kcKP_2 = kc.KP_2
        kcKP_3 = kc.KP_3
        kcKP_4 = kc.KP_4
        kcKP_5 = kc.KP_5
        kcKP_6 = kc.KP_6
        kcKP_7 = kc.KP_7
        kcKP_8 = kc.KP_8
        kcKP_9 = kc.KP_9
        kcKP_0 = kc.KP_0

        kcLEFT_CTRL = kc.LEFT_CTRL
        kcLEFT_SHIFT = kc.LEFT_SHIFT
        kcLEFT_ALT = kc.LEFT_ALT
        kcLEFT_UI = kc.LEFT_UI
        kcRIGHT_CTRL = kc.RIGHT_CTRL
        kcRIGHT_SHIFT = kc.RIGHT_SHIFT
        kcRIGHT_ALT = kc.RIGHT_ALT
        kcRIGHT_UI = kc.RIGHT_UI
    elif language == "US":
        kcA = kc.A
        kcB = kc.B
        kcC = kc.C
        kcD = kc.D
        kcE = kc.E
        kcF = kc.F
        kcG = kc.G
        kcH = kc.H
        kcI = kc.I
        kcJ = kc.J
        kcK = kc.K
        kcL = kc.L
        kcM = kc.M
        kcN = kc.N
        kcO = kc.O
        kcP = kc.P
        kcQ = kc.Q
        kcR = kc.R
        kcS = kc.S
        kcT = kc.T
        kcU = kc.U
        kcV = kc.V
        kcW = kc.W
        kcX = kc.X
        kcY = kc.Y
        kcZ = kc.Z
        kcN1 = kc.N1
        kcN2 = kc.N2
        kcN3 = kc.N3
        kcN4 = kc.N4
        kcN5 = kc.N5
        kcN6 = kc.N6
        kcN7 = kc.N7
        kcN8 = kc.N8
        kcN9 = kc.N9
        kcN0 = kc.N0
        kcENTER = kc.ENTER
        kcESCAPE = kc.ESCAPE
        kcBACKSPACE = kc.BACKSPACE
        kcTAB = kc.TAB
        kcSPACE = kc.SPACE
        kcMINUS = kc.MINUS
        kcEQUAL = kc.EQUAL
        kcOPEN_BRACKET = kc.OPEN_BRACKET
        kcCLOSE_BRACKET = kc.CLOSE_BRACKET
        kcBACKSLASH = kc.BACKSLASH
        kcHASH = kc.HASH
        kcSEMICOLON = kc.SEMICOLON
        kcQUOTE = kc.QUOTE
        kcGRAVE = kc.GRAVE
        kcCOMMA = kc.COMMA
        kcDOT = kc.DOT
        kcSLASH = kc.SLASH
        kcCAPS_LOCK = kc.CAPS_LOCK
        kcF1 = kc.F1
        kcF2 = kc.F2
        kcF3 = kc.F3
        kcF4 = kc.F4
        kcF5 = kc.F5
        kcF6 = kc.F6
        kcF7 = kc.F7
        kcF8 = kc.F8
        kcF9 = kc.F9
        kcF10 = kc.F10
        kcF11 = kc.F11
        kcF12 = kc.F12
        kcPRINTSCREEN = kc.PRINTSCREEN
        kcSCROLL_LOCK = kc.SCROLL_LOCK
        kcPAUSE = kc.PAUSE
        kcINSERT = kc.INSERT
        kcHOME = kc.HOME
        kcPAGEUP = kc.PAGEUP
        kcDELETE = kc.DELETE
        kcEND = kc.END
        kcPAGEDOWN = kc.PAGEDOWN
        kcRIGHT = kc.RIGHT
        kcLEFT = kc.LEFT
        kcDOWN = kc.DOWN
        kcUP = kc.UP
        kcKP_NUM_LOCK = kc.KP_NUM_LOCK
        kcKP_DIVIDE = kc.KP_DIVIDE
        kcKP_AT = kc.KP_AT
        kcKP_MULTIPLY = kc.KP_MULTIPLY
        kcKP_MINUS = kc.KP_MINUS
        kcKP_PLUS = kc.KP_PLUS
        kcKP_ENTER = kc.KP_ENTER
        kcKP_1 = kc.KP_1
        kcKP_2 = kc.KP_2
        kcKP_3 = kc.KP_3
        kcKP_4 = kc.KP_4
        kcKP_5 = kc.KP_5
        kcKP_6 = kc.KP_6
        kcKP_7 = kc.KP_7
        kcKP_8 = kc.KP_8
        kcKP_9 = kc.KP_9
        kcKP_0 = kc.KP_0

        kcLEFT_CTRL = kc.LEFT_CTRL
        kcLEFT_SHIFT = kc.LEFT_SHIFT
        kcLEFT_ALT = kc.LEFT_ALT
        kcLEFT_UI = kc.LEFT_UI
        kcRIGHT_CTRL = kc.RIGHT_CTRL
        kcRIGHT_SHIFT = kc.RIGHT_SHIFT
        kcRIGHT_ALT = kc.RIGHT_ALT
        kcRIGHT_UI = kc.RIGHT_UI



def userInputInlineTwo(vlue, languagezer):
    rootLang(languagezer)

    # Exemple d'entrées utilisateur (remplace par les valeurs dynamiques)
    inputted = ['[(kcLEFT_CTRL, kcLEFT_ALT, kcT)]', '[[DELAY 100]]', 'echo Bonjour les amis']
    
    sequence = []

    for line in inputted:
        if line.startswith("[[DELAY") and line.endswith("]]"):
            # Si un délai est rencontré
            try:
                # Envoyer la séquence actuelle avant le délai
                if sequence:
                    sendKeys(sequence, vlue, 0.01)
                
                # Réinitialiser la séquence après l'envoi
                sequence = []
                
                # Extraire le délai (en millisecondes) et le convertir en secondes
                delay_value = int(line[8:-2].strip()) / 100.0
                time.sleep(delay_value)  # Effectuer la pause
            except ValueError:
                raise ValueError(f"Format invalide pour DELAY")
        
        elif line.startswith("[") and line.endswith("]"):
            # Supprimer les crochets
            key_block = line[1:-1].strip()
            
            if key_block.startswith("(") and key_block.endswith(")"):
                # Gérer une séquence en tuple (ex : (kcLEFT_CTRL, kcLEFT_ALT, kcT))
                tuple_keys = key_block[1:-1].split(",")  # Supprime les parenthèses et sépare les clés
                tuple_sequence = []
                for key in tuple_keys:
                    key = key.strip()
                    try:
                        tuple_sequence.append(globals()[key])
                    except KeyError:
                        raise ValueError(f"Touche inconnue dans le tuple")
                sequence.append(tuple(tuple_sequence))  # Ajouter le tuple au sequence
            else:
                # Gérer une séquence normale (ex : kcA)
                keys = key_block.split("+")  # Extrait les touches séparées par '+'
                for key in keys:
                    key = key.strip()
                    try:
                        sequence.append(globals()[key])
                    except KeyError:
                        raise ValueError(f"Touche inconnue")
                sequence.append(ENTER)
        else:
            # Gérer une chaîne normale
            for i in stringSeq(line):
                sequence.append(i)
            sequence.append(ENTER)  # Ajouter 'ENTER' après chaque ligne normale

    # Envoyer les touches restantes après avoir traité toutes les lignes
    if sequence:
        sendKeys(sequence, vlue, 0.01)
        