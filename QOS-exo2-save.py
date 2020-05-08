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
def point(absc,ordo): #Ajoute les points à une liste
    xx.append(absc)
    yy.append(ordo)


def trace_courbe(x,y,a): #Trace graphique
    plt.plot(x,y)
    plt.title(a)
    plt.xlabel("")
    plt.ylabel("")
    plt.show()
    return 
	
def calcul_proba_blocage(roh,n): #Calcul la probabilité de que tout les canaux soit utilisé
    if roh==1:
            return print("pas de chance : try again")
    else:
        p_num= 1-roh
        p_denum= 1-pow(roh,n+1)
        proba_perte= (p_num/p_denum)*(pow(roh,n))
        #print("Pour ",n," capa , on tx perte : ", float_to_str(proba_perte))
        points(n,proba_perte)
        return proba_perte

def calcul_temps_rep(lambdab,roh,n): #Calcul du temps de reponse moyen
    L=0
    p_denum= lambdab*(1-calcul_proba_blocage(roh,n))
    for i in range(n,1,-1):
        L+=  i*(calcul_proba_blocage(roh,n)/(roh**i))#nombre moyen de client dans le systeme
    print("nombre de client moyen = ",L)
    temps_rep= L/p_denum
    print("Pour ",n," capa , on a temps de rep: ", float_to_str(temps_rep))
    point(n,temps_rep)
    return temps_rep


#question 1-A
#M/M/1/N
taille_paquet= 1500*8 #consersion en octet en bits
debit= 1*(10**9) #lien de sortie
tps_trans_paquet= taille_paquet/debit #
mu = 1/ tps_trans_paquet


for debit_arrive in range(700,901,100):
    x =[] #axe des abscisses
    y =[] #axe des ordonnées
    xx =[] #axe des abscisses
    yy =[] #axe des ordonnées
    debit_arrive= debit_arrive*pow(10,6) #taux d'arrivé ou débit des paquet entrant
    lambdab = debit_arrive/taille_paquet
    print("lambda ", lambdab)
    roh=lambdab/mu	#cours
    print("roh ", roh)
    for N in range(5,41,5):
        calcul_proba_blocage(roh,N)
        calcul_temps_rep(lambdab,roh,N)
    trace_courbe(x,y,"Probabilité de pertes en fonction du nombre de capa")
    trace_courbe(xx,yy,"temps de réponse en fonction du nombre de capa")
    print("")

