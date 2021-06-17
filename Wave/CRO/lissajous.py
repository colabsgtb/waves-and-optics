#from numpy import sin,pi,linspace as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def res_var():
    data = pd.read_csv('var_res.csv')
    A_x = data['Ax(in V )']
    A_y = data['Ay(in V )']
    delta = data['delta( in rad)']
    t = np.linspace(-np.pi,np.pi,300)

    for i in range(0,5):
        x = A_x[i]*np.sin(100* t)
        y = A_y[i]*np.sin(100* t + delta[i])
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlabel("x($V$)")
        ax.set_ylabel("y($V$)")
        plt.tight_layout()
        ax.grid(True)
        plt.plot(x,y)
        plt.show()
        
def freq_var():
    data = pd.read_csv('var_freq.csv')
    A_x = data['Ax(in V )']
    A_y = data['Ay(in V )']
    delta = data['delta( in rad)']
    t = np.linspace(-np.pi,np.pi,300)

    for i in range(0,3):
        x = A_x[i]*np.sin(100* t)
        y = A_y[i]*np.sin(100* t + delta[i])
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlabel("x($V$)")
        ax.set_ylabel("y($V$)")
        plt.tight_layout()
        ax.grid(True)
        plt.plot(x,y)
        plt.show()
        
def delta_vs_freq():
    data = pd.read_csv('var_freq.csv')
    delta = data['delta( in rad)']
    freq = data['v(Hz)']
    
    plt.xscale('log')
    plt.tight_layout()
    plt.grid(True)
    plt.xlabel("$v$ $(Hz)$")
    plt.ylabel("$\Theta$ (rad)")
    plt.plot(freq,delta)
    plt.show()
    
def freq_not():
    data = pd.read_csv('var_res.csv')
    Ax = data['Ax(in V )']
    Ay = data['Ay(in V )']
    p=[12,17]
    q=[17,-0.72]
    r=[17,17]
    fig, ax = plt.subplots()
    ax.plot(Ax,Ay)
    #ax.plot(q,r,color='#444444',linestyle='dashed')
    #ax.plot(r,p,color='#444444',linestyle='dashed')
    ax.set_xlabel("$A_x(V)$")
    ax.set_ylabel("$A_y(V)$")
    plt.xticks(np.arange(12, 21, 1.0))
    plt.yticks(np.arange(0, 18, 2.5))
    ax.annotate("(17,17)", (17,17),xytext=(17,17))
    #ax.set_ylim([0, 0])
    plt.grid(True)
    plt.show()
    

        
if __name__ == "__main__":
    res_var()
    freq_var()
    delta_vs_freq()
    freq_not()

