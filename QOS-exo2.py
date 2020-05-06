#import des librairies
import math, numpy,pylab,decimal
import matplotlib.pyplot as plt

lambda = 700 * 10**6
taille_paquet=12000
debit : 1*10**-6
n = 5
tps_trans_paquet= Taille_paquet/Debit
mu = 1/ Tps_trans_paquet
roh=Lambda/mu	

def points(absc,ordo): #Ajoute les points à une liste
    x.append(absc)
    y.append(ordo)

def trace_courbe(x,y): #Trace graphique
    plt.plot(x,y)
    plt.title("Probabilité de pertes en fonction du nombre de canaux")
    plt.show()
    return 
	
def calcul_proba_blocage(roh,n): #Calcul la probabilité de que tout les canaux soit utilisé
	p_num = 1 - roh * roh**n
	p_denum = 1 - roh**n+1
	proba_perte = (p_num/p_denum)
	points(n,proba_perte)

   return proba_perte

x =[] #axe des abscisses
y =[] #axe des ordonnées

#question 1-A
for n in range(5,40,5):
    calcul_proba_blocage(roh,n)

trace_courbe(x,y)
print("")

