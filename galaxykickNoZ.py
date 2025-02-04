import numpy as np
import gala.potential as gp

mwp = gp.MilkyWayPotential2022()

class MWwNoise(gp.PotentialBase):
    N = gp.PotentialParameter("N")
    ndim = 3
    
    def _energy(self, xyz, t):
        # N = self.parameters['N'].value
        xyz = xyz.T
        energy = mwp.energy(xyz)
        return energy/energy.unit

    def _gradient(self, xyz, t):
        N = self.parameters['N'].value
        xyz = xyz.T
        grad = (mwp.gradient(xyz)).T
        noise = N*(np.random.rand(1,3)-0.5)* [1,1,0] * grad.unit
        gradwnoise = grad + noise
        return gradwnoise/gradwnoise.unit