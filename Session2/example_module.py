'''An example module that contains basic functions and classes.
Written in May/June 2018 by J. Line to be used at Kathmandu Astro
School 2018'''

from sys import exit
from numpy import ndarray
import matplotlib.pyplot as plt

def polynomial(x,a=1,b=1,c=0):
    '''Returns the 2nd order polynomial of x,
    using the coefficients a,b,c as
    a*x**2 + b*x + c'''
    return a*x**2 + b*x + c

class Spectra():
    '''A simple class to extrapolate and plot spectra for a basic astronomical radio source'''
    def __init__(self,SI,frequency,flux):
        '''Takes the spectral index, reference frequency, and refrence flux
        of a generic radio spectra and initiales the Spectra class.
        Caculate s0 as defined by the equation flux = S0*frequency**SI'''
        self.flux = flux
        self.SI = SI
        self.frequency = frequency
        self._s0 = flux / frequency**SI
        
    def extrapolate_flux(self,frequencies):
        '''Extrapolate fluxes to match the given frequencies'''
        return self._s0 * frequencies ** self.SI
    
    def plot_spectra(self,frequencies):
        '''Do a basic plot of the spectra for these frequencies'''
        plt.plot(frequencies,self.extrapolate_flux(frequencies))
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Flux (Jy)')
        plt.show()

class Spectra_fancier():
    '''A more advanced class to extrapolate and plot spectra for a basic astronomical radio source
    Does internal variable type checks to ensure correct behaviours'''
    def _test_type(self,variable,name):
        '''Tests the type of each variable, and exits the programme if not
        either a float, int or numpy ndarray'''
        if type(variable) != float and type(variable) != int and type(variable) != ndarray:
            print(name, 'must be a float, int, or array. Exiting program')
            exit()
    
    def __init__(self,SI=None,frequency=None,flux=None):
        '''Takes the spectral index, reference frequency, and refrence flux
        of a generic radio spectra and initiales the Spectra class.
        Caculate s0 as defined by the equation flux = S0*frequency**SI'''
        self._test_type(SI,'SI')
        self._test_type(frequency,'frequency')
        self._test_type(flux,'flux')
        
        self.flux = flux
        self.SI = SI
        self.frequency = frequency
        self._s0 = flux / frequency**SI
        
    def extrapolate_flux(self,frequencies=None):
        '''Extrapolate fluxes to match the given frequencies'''
        self._test_type(frequencies,'frequencies')
        return self._s0 * frequencies ** self.SI
    
    def plot_spectra(self,frequencies=None):
        '''Do a basic plot of the spectra for these frequencies'''
        self._test_type(frequencies,'frequencies')
        
        plt.plot(frequencies,self.extrapolate_flux(frequencies))
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Flux (Jy)')
        plt.show()