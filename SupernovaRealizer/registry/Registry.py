'''
Created on Jan 16, 2013

@author: akim
'''
import SupernovaRealizer.realizers.ByHost
import SupernovaRealizer.realizers.MyRealizer_ByHost
import importlib


def load_file_registry():
    registry_file = './external_registry.dat'
    f = open(registry_file, 'r')
    realizers = dict()
    for line in f:
        (modulename, realizername) = line.rsplit(".", 1)
        module = importlib.import_module(modulename)
        realizer = getattr(module, realizername)
        name = getattr(module, 'name')
        realizers[name] = realizer
    f.close()
    return realizers

class Registry(object):
    '''
    classdocs
    '''
    # realizers known programmatically
    realizers = dict([(SupernovaRealizer.realizers.ByHost.name, SupernovaRealizer.realizers.ByHost.Realizer), (SupernovaRealizer.realizers.MyRealizer_ByHost.name, SupernovaRealizer.realizers.MyRealizer_ByHost.Realizer)])

    # input registry
    realizers.update(load_file_registry())

    @staticmethod
    def get_realizer(config, args):
        realizername = config['Realizer']['name']
        pars = config['Realizer']['parameters']
        return Registry.realizers[realizername](args, pars)
