#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma, zeta

np.random.seed(20)


# In[2]:


def generate_RV(N=100, distype='Normal'):
    '''
    This function generates random variables of desired shape and distribuition
    INPUTS
        N indicates size
        distype indicates distribution type
    OUTPUT
        array of RVs
        theoritical mean
    '''
    if distype == 'Normal':
        return np.random.normal(size=(N, )), 0
    elif distype == 'Uniform':
        return np.random.uniform(size=(N, )), 0.5
    elif distype == 'Weibull':
        a=10
        return np.random.weibull(a, size=(N, )), gamma(1+1/a)
    elif distype == 'Zipf':
        a = 3
        return np.random.zipf(a, size=(N, )), zeta(a-1)/zeta(a)
    elif distype == "Poisson":
        lamda = 10
        return np.random.poisson(lam=lamda, size=((N, ))), lamda
    elif distype == "Rayleigh":
        sigma = 10
        return np.random.rayleigh(scale=sigma, size=((N, ))), sigma*np.sqrt(np.pi/2)


# In[11]:


def simulate(N=100):
    '''
    This function simulates sum of random variables and convergence to theoritical mean
    INPUTS
        N indicates size
    OUTPUT
        Renders and saves plot
    '''
    dist = ['Normal', 'Uniform', 'Weibull', 'Zipf', 'Poisson', 'Rayleigh']
    plt.figure(figsize=(36, 24))
    plt.suptitle('Illustration of Weak LLN with different probability density functions', fontsize=30, color="red")
    for i, d in enumerate(dist):
        
        arr, mu = generate_RV(N=N, distype=d)
        cum_arr = np.array([np.sum(arr[:idx]/(idx+1)) for idx in range(len(arr))])
        
        plt.subplot(2, 3, (1+i))
        plt.plot(arr, 'g.--', label=r'$X$', alpha=0.2)
        plt.plot(cum_arr, label=r'$\tilde{X_n}$')
        plt.axhline(mu, label=r'$E[X]$', color='red')
        plt.legend()
        plt.title(d, fontsize=20, color="blue")
        plt.ylabel('Amplitude', fontsize=15)
        plt.xlabel('N', fontsize=15)
    
    plt.savefig('simulation.jpeg')
    plt.show()

simulate(N=1000)

