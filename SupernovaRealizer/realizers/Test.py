'''
Created on Jan 21, 2013

@author: akim
'''
import Sources
import ByHost

if __name__ == '__main__':
    galaxies=[Sources.Galaxy(5,5,0.75,1),Sources.Galaxy(10,10,0.5,0)]
    realizer=ByHost.Realizer(1,1000,2000,2./3600,'data/snflux_1a.dat')
    
    for galaxy in galaxies:
        real=realizer.realize(galaxy)
        for sn in real:
            print sn.ra, sn.dec, sn.doe, sn.luminosity(1500,5000)