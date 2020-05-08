#import des librairies
import math, numpy,pylab,decimal
import matplotlib.pyplot as plt

#Fonctions du programme
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

def calcul_proba_blocage(lambda_appel,mu_appel,nb_canal): #Calcul la probabilité de que tout les canaux soit utilisé
   p_somme =0
   A =lambda_appel/mu_appel
   p_c =A**nb_canal/math.factorial(nb_canal)
   for i in range(nb_canal+1):
       p_somme+=((A**i)/(math.factorial(i)))
   res =round((p_c/p_somme),8)
   print("Pour "+str(nb_canal)+" canal, on a P Blocage = "+float_to_str(res))
   points(nb_canal,res)
   return res

#Variable graphique
x =[] #axe des abscisses
y =[] #axe des ordonnées
cal =[] #axe 


#question 1-A
#M/M/C/C
#lambda = 5
#mu = 1/5
for i in range(15,50,5):
    calcul_proba_blocage(5,1/5,i)

#question 1-B
trace_courbe(x,y)
print("")

#question 1-C
#M/M/C/C
#lambda = 7
#mu = 1/5
x =[]
y =[]
for i in range(30,60,1):
    calcul_proba_blocage(7,1/5,i)
trace_courbe(x,y)
print("")

#question 1-D
#M/M/40/C
#lambda
    # 7
    # 2
#mu = 1/5
y =[]
lambda_filtre=0
for C1 in range(20,41,1):
    lambda_filtre=0
    print("C1 = ",C1)
    for i in range(1,41,1):   
        if i <=C1: #teste si le nombre de canaux occupé est inférieur a une valeur seuil (nb de canaux libre)(C1 ≤ C2),
            lambda_filtre+=7 
        else:
            lambda_filtre+=2 
    lambda_filtre=lambda_filtre/i
    print("lambda filtré = ",lambda_filtre)
    cal.append(C1)
    calcul_proba_blocage(lambda_filtre,1/5,40)
trace_courbe(cal,y)
print("")

