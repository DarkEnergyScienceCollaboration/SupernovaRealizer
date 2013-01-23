'''
Created on Jan 21, 2013

@author: akim
'''
import Sources
import ByHost
import numpy

if __name__ == '__main__':
    
    
    galaxies=[Sources.Galaxy(5,5,0.75,1),Sources.Galaxy(10,10,0.5,0)]
    realizer=ByHost.Realizer(1,1000,2000,2./3600,'data/snflux_1a.dat',numpy.power(10,19/2.5))
    
    real1=realizer.realize(galaxies[0])
    real2=realizer.realize(galaxies[1])
    
    i1=iter(real1)
    i2=iter(real2)
    
    sn=i1.next()
    print sn.ra, sn.dec, sn.doe
    sn=i2.next()
    print sn.ra, sn.dec, sn.doe
    
    sn=i1.next()
    print sn.ra, sn.dec, sn.doe
    sn=i2.next()
    print sn.ra, sn.dec, sn.doe

    for galaxy in galaxies:
        real=realizer.realize(galaxy)
        for sn in real:
            print sn.ra, sn.dec, sn.doe