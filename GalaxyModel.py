# %%
import galaxykick as Galaxy
import astropy.units as u
import pickle 
import gala.dynamics as gd
import gala.potential as gp
from gala.units import galactic
directory = "Folder/"
filename = "FileName"
print(filename)

# %%
orbitdict = {}
orbitcount = 0
maxIter = 500
dT = 0.1 #* u.Myr 
noiselevel = 0.1
print('noise level is ',noiselevel)
w0 = gd.PhaseSpacePosition(pos=[5., 0., 0.]*u.kpc,vel=[10, 225, 0.]*u.km/u.s)
# w0 = gd.PhaseSpacePosition(pos=[-8.1, 0, 0.02]*u.kpc,vel=[13, 245, 8.]*u.km/u.s) # phase space of Sun

# %%
while orbitcount < maxIter:
    print(f'orbit count = {orbitcount}')
    newpot = Galaxy.MWwNoise(N=noiselevel,dt=dT,units=galactic)
    neworbit = newpot.integrate_orbit(w0, dt=0.01 * u.Myr, n_steps=10000)
    orbitdict[str(noiselevel)+'_'+str(orbitcount)] = neworbit
    orbitcount += 1

# %%
with open(directory+filename+'.pkl', 'wb') as f:
    pickle.dump(orbitdict, f)
