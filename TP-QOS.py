import math, numpy,pylab,decimal
import matplotlib.pyplot as plt
 
# create a new context for this task
ctx = decimal.Context()
ctx.prec =8

def float_to_str(f): #ecriture numérique
    d1 =ctx.create_decimal(repr(f))
    return format(d1, 'f')

def points(absc,ordo):
    x.append(absc)
    y.append(ordo)

def trace_courbe(x,y): #trace graphique
    plt.plot(x,y)
    plt.title("Probabilité de pertes en fonction du nombre de canaux")
    plt.show()
    return 

def calcul_proba_blocage(A,C):
   p_somme =0
   p_c =A**C/math.factorial(C)
   for i in range(C):
       p_somme+=((A**i)/(math.factorial(i)))
   res =round((p_c/p_somme),8)
   print("Pour "+str(C)+" canal, on a P Blocage = "+float_to_str(res))
   points(C,res)
   return res
          
lambda_A =5 #appel 
lambda_B =2 #appel handover
mu =1/5

A =lambda_A/mu
B =(lambda_A+lambda_B)/mu

x =[]
y =[]

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

