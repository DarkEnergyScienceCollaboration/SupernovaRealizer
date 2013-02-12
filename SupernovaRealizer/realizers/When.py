'''
Created on Feb 11, 2013

@author: akim
'''

class ConstantRateAtRedshift(object):
    '''
    classdocs
    '''
    parameter_names = ['when.sim_start', 'when.sim_end']
    rate = 1. / 100. / 365.25  # 1 per century

    def __init__(self, pars):
        '''
        Constructor
        '''
        self.sim_start = pars['sim_start']
        self.sim_end = pars['sim_end']

    def number(self, random_state, redshift):

        expected = ConstantRateAtRedshift.rate * (self.sim_end - self.sim_start) / (1 + redshift)

        # calculate the number of explosions in the time period
        return random_state.poisson(expected)

    def realize(self, random_state, redshift):

        # calculate the number of explosions in the time period
        return random_state.uniform(low=self.sim_start, high=self.sim_end)

