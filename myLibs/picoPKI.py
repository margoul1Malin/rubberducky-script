from .utils import *

def OnlyKeyDump(vlue, username, password):
    sequence = []
    
    for letters in stringSeq(username):
        sequence.append(letters)
    sequence.append(TAB)
    for letters in stringSeq(password):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.1)
    
def myLinuxShit(vlue):
    
    sequence = []
    
    step1 = "set root=(hd0,gpt7)"
    step2 = "linux /boot/vmlinuz-6.12.20-amd64 root=/dev/sda7 ro"
    step3 = "initrd /boot/initrd.img-6.12.20-amd64"
    step4 = "boot"
    
    for letters in stringSeq(step1):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.04)
    time.sleep(1)
    sequence = []
    
    for letters in stringSeq(step2):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.04)
    time.sleep(2)
    sequence = []
    
    for letters in stringSeq(step3):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.04)
    time.sleep(4)
    sequence = []
    
    for letters in stringSeq(step4):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.04)