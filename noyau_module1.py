# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:54:17 2021

Noyau - Module 1

Exceptionnellement sans classe

@author: JCV
"""
#%% Récupération chemin actuel du script
def ouSuisJe():
    """
    cette fonction retourne le chemin complet du script en cours d'exécution'

    Returns
    -------
    chemin : str
        Chemin complet du script en cours d'exécution.
        Exemple : c:/user/jcv/memolab/

    """
    import os
    absFilePath = os.path.abspath(__file__)
    chemin, nomScript = os.path.split(absFilePath)
    chemin = chemin + "/"
    return chemin


def chargeParametresGeneraux(nomFichierParametres):
    """
    Charge les paramètres contenus dans le fichier xlsx appelé dans le
    dictionnaire paraGen retourné au script appelant

    Parameters
    ----------
    nomFichierParametres : str
        Nom du fichier excel xlsx contenant la liste des paramètres selon
        le modèle fourni avec l'appli.

    Returns
    -------
    paraGen : dict
        Un terme par paramètre.
        L'appel d'un paramètre se fait ainsi :
            <valeurParamètre> = paraGen["<nomParamètre>"]

    """
    paraGen = {}
    # Accès au fichier excel
    import openpyxl
    # chemin du script courant
    chemin = ouSuisJe()
    # print(chemin)
    # objet workbook
    wb = openpyxl.load_workbook(chemin + nomFichierParametres)
    # objet worksheet
    ws = wb.active
    for ligne in range(1, 100):
        adrCelluleNom = "B" + str(ligne)
        adrCelluleVal = "C" + str(ligne)
        nomParametre = ws[adrCelluleNom].value
        valeurParametre = ws[adrCelluleVal].value
        if valeurParametre == None:
            break
        # ajout parametre au dictionnaire
        paraGen.update({nomParametre : valeurParametre})
        # essai création variable
        # exec(nomParametre + " = valeurParametre")
    wb.close()
    # print("JeanClaude =", JeanClaude)
    return paraGen
