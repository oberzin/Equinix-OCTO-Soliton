"""
Created on Sep 5, 2017

@author: oberzin
"""
import numpy as np

import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

def plot_data(a, b):
    fig = plt.figure()
    fig.patch.set_facecolor('black')
    plt.grid(True)
    frame1=plt.gca()
    plt.ioff()

    plt.plot(a, b, linewidth=2, color='red')

    plt.title('O C T O', fontsize=20, color='red', fontweight='normal',
              family='tahoma')

    plt.xlabel(r'$\frac{1}{\sqrt{2\pi}}\exp\{\minus\frac{x^2}{2}\}\cos\{2\pi{kx}\}$', fontsize=12, color='blue', fontweight='bold')
    plt.text(-1.6,-0.5, r'$\frac{1}{\sqrt{2\pi}}\exp\{\minus\frac{x^2}{2}\}\cos\{2\pi{kx}\}$',fontsize=16, color='red', fontweight='bold')
  
    plt.xticks([])

    frame1.axis('off')

    plt.rcParams['figure.dpi']=500

    plt.draw()

    plt.show()

    #plt.savefig('EqixOctoSoliton-High.png', dpi=1200)
    
def main():

    x = np.linspace(-3, 3, 300)
    y = 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)
    z = y * np.cos(2*np.pi*2*x)
    plot_data(x ,z)

if __name__ == '__main__':
    main()