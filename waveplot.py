import matplotlib.pyplot as plt
import numpy as np

def plot_all(fn1,fn2,fntot,t):
    plt.figure(figsize=(8,6))
    ax1 = plt.axes([0.15,0.69,0.81,0.27])
    ax2 = plt.axes([0.15,0.42,0.81,0.27])
    ax3 = plt.axes([0.15,0.15,0.81,0.27])
    
    ax1.xaxis.set_major_formatter(plt.NullFormatter())
    ax2.xaxis.set_major_formatter(plt.NullFormatter())
    
    xx = np.linspace(0,2,100)
    yy1 = np.zeros(len(xx))
    yy2 = np.zeros(len(xx))
    yy3 = np.zeros(len(xx))
    
    for a in range(len(xx)):
        yy1[a] = fn1(xx[a],t)
        yy2[a] = fn2(xx[a],t)
        yy3[a] = fntot(xx[a],t)
    
    ax1.plot(xx,yy1)
    ax1.set_ylim((-1,1))
    ax2.plot(xx,yy2)
    ax2.set_ylim((-1,1))
    ax3.plot(xx,yy3)
    ax3.set_ylim((-2,2))
    plt.show()
