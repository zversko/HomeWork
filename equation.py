import numpy as np
import matplotlib.pyplot as plt

def task4_graph():
    x = np.arange(-100, 100, 0.001)
    plt.figure(figsize=(10, 5))
    plt.plot(x, -12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30, label=r'-12*x**4*np.sin(np.cos(x)) - 18*x**3+5*x**2 + 10*x - 30')

    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.savefig('figure_with_legend.png')
    plt.show()

task4_graph()
