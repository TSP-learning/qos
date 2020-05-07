#import des librairies
import math, numpy,pylab,decimal
import matplotlib.pyplot as plt

ctx = decimal.Context()
ctx.prec =8
def float_to_str(f): #Force un ecriture sous forme de décimal à virgule
    d1 =ctx.create_decimal(repr(f))
    return format(d1, 'f')

def points(absc,ordo): #Ajoute les points à une liste
    x.append(absc)
    y.append(ordo)

def trace_courbe(x,y): #Trace graphique
    plt.plot(x,y)
    plt.title("Probabilité de pertes en fonction du nombre de canaux")
    plt.show()
    return 
	
def calcul_proba_blocage(roh,n): #Calcul la probabilité de que tout les canaux soit utilisé
    if roh==1:
            return print("pas de chance : try again")
    else:
        p_num= 1-roh
        p_denum = 1-pow(roh,n+1)
        proba_perte = (p_num/p_denum)*(pow(roh,n))
        print("Pour ",n," canals , on tx perte : ", float_to_str(proba_perte))
        points(n,proba_perte)
        return proba_perte

x =[] #axe des abscisses
y =[] #axe des ordonnées

#question 1-A
#M/M/1/N
arrive= 700*pow(10,6) #taux d'arrivé ou débit des paquet entrant
taille_paquet= 1500*8 #consersion en octet en bits
lambdab = arrive/taille_paquet
print("l", lambdab)
debit= 1*(10**9) #lien de sortie
tps_trans_paquet= taille_paquet/debit #
mu = 1/ tps_trans_paquet

roh=lambdab/mu	#cours
print("roh ", roh)

for N in range(5,41,5):
    calcul_proba_blocage(roh,N)

trace_courbe(x,y)
print("")

