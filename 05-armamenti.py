from env import *


def armamenti(a,b,c,d,e,n,x0,y0,n_iter):
    A = sy.Matrx([[a,b,],[c,d]])
    P, J = m.jordan_form()