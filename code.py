###########################################################
#This script use the selenium library to get a huge data from 
#a site it implements a simple algorithme which try to fetch data :

#if the symbole ">" is present then it make click to go the next page and continue the fetch operation 
#after that it put the data into lists then into csv files 
############################################################
from selenium import webdriver

import time

import csv 


############################################################
#Some methods to help the reader understanding the script 
############################################################

def verifNextPresent() :
    x=driver.find_element_by_xpath("//a[@title='Suivant']")
    if(x):
        return True
    return False


def findBoxElement(i) :
      try:        
            driver.find_elements_by_class_name("box-product-item")[i].find_element_by_class_name("buttons-cart").click()
      except :
            print("probleme dans la fonction qui recherche le box de donnée")
            time.sleep(2)


def afficheBoxCourant(x):
    print(x)


def appendDonnee(element) :

    liste=[]

    listeNom=driver.find_elements_by_class_name(element)
    for i in range(len(listeNom)):
        liste.append(listeNom[i].text)

    return(liste)



def isertDonneeFichier(nomFichier,liste1,liste2,liste3,liste4,liste5,liste6,liste7) :
    file=open(nomFichier,"a")
    with file :
        writer=csv.writer(file)

        for i in range(len(liste1)) :
            writer.writerow([liste1[i],liste2[i],liste3[i],liste4[i],liste5[i],liste6[i],liste7[i]])

def appendListwithException(liste,elemPython,mot):
    try : 
        liste.append(elemPython)
    except :
        liste.append("pas de " + mot)
        

def insertInCsvFile(liste1,liste2,liste3,liste4,liste5,liste6,liste7):
        isertDonneeFichier("testCsv.csv",liste1,liste2,liste3,liste4,liste5,liste6,liste7)


#main program :

#get the url using the webdriver of selenium
path ="E:\ChromeDriver\chromedriver.exe"
url="http://"
driver = webdriver.Chrome(path)
driver.get(url)
##############################################

driver.find_element_by_id("nature_filtre_top").find_element_by_tag_name("option").click()
driver.find_element_by_id("submit_filtre_top").click()
listElement=driver.find_elements_by_class_name("box-product-item")

#the declaration of empty list
listeNoms=[]
listeNumerosTelephones=[]
listeAdresses=[]
listeSitesWeb=[]
listePagesFacebook=[]

#if the symbole ">" is present the we click to go to the next page

while(verifNextPresent()) :
	
    listeType=appendDonnee("nat_lib")
    listeplace=appendDonnee("emplacement_jardin")

#iterate all the element in the page 

    for i in range(len(listElement)) :

        afficheBoxCourant(i)
        
        findBoxElement(i)
        
        time.sleep(0.8)
        try :
            appendListwithException(listeNoms,driver.find_element_by_class_name("cats_manzah").find_element_by_tag_name("h1").text,"nom")
        except:
            listeNoms.append("pas de nom")
        try :
            appendListwithException(listeNumerosTelephones,driver.find_element_by_class_name("cat_contenu").find_elements_by_tag_name("p")[1].text.split(":")[1],"numero")
        except :

            listeNumerosTelephones.append("pas de numero de telephone")

        try :
            
            appendListwithException(listeAdresses,driver.find_element_by_class_name("cat_contenu").find_elements_by_tag_name("p")[0].text.split(":")[1],"adresse")
        except :
            listeAdresses.append("pas d'adresse")

        try  :
            
            appendListwithException(listeSitesWeb,driver.find_element_by_css_selector("a.btn.btn-large.postuler.site_web").get_attribute("href"),"site web")
        except :

            listeSitesWeb.append("pas de site web")

            
        try :
            appendListwithException(listePagesFacebook,driver.find_element_by_css_selector("a.btn.btn-large.postuler2.page_fb").get_attribute("href"),"page facebook")
        except :
            listePagesFacebook.append("pas de page facebook") 

        driver.back()
        time.sleep(0.5)
        
    print(listeNoms)
#insert the list into the scv file 
    insertInCsvFile(listeType,listeplace,listeNoms,listeNumerosTelephones,listeAdresses,listeSitesWeb,listePagesFacebook)
    try: 
#go to next page 
        driver.find_element_by_xpath("//a[@title='Suivant']").click()
    except :
        print("le parcours est terminé")
        
    time.sleep(0.5)
            
