#import des librairies
import math, numpy,pylab,decimal
import matplotlib.pyplot as plt

#Fonctions du programme
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

def calcul_proba_blocage(A,C): #Calcul la probabilité de que tout les canaux soit utilisé
   p_somme =0
   p_c =A**C/math.factorial(C)
   for i in range(C):
       p_somme+=((A**i)/(math.factorial(i)))
   res =round((p_c/p_somme),8)
   print("Pour "+str(C)+" canal, on a P Blocage = "+float_to_str(res))
   points(C,res)
   return res

#Variable 
# create a new context for this task
ctx = decimal.Context()
ctx.prec =8

lambda_A =5 #nouveaux appel
lambda_B =2 #appel handover
mu =1/5

A =lambda_A/mu
B =(lambda_A+lambda_B)/mu

x =[] #axe des abscisses
y =[] #axe des ordonnées

#question 1-A
for i in range(15,50,5):
    calcul_proba_blocage(A,i)

#question 1-B
trace_courbe(x,y)
print("")

#question 1-C
x =[]
y =[]
for i in range(40,60,1):
    calcul_proba_blocage(B,i)
trace_courbe(x,y)
print("")

#question 1-D
x =[]
y =[]
for i in range(20,41,1):   
    if 1 <= 40:
        C =lambda_A+lambda_B
    else:
        C =lambda_B
    calcul_proba_blocage(C,i)
trace_courbe(x,y)
print("")

