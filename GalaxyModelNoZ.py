# %%
import galaxykickNoZ as Galaxy

# Third-party
import astropy.units as u
import pickle 
import datetime
y = datetime.datetime.now()
print(y)

# Gala
import gala.dynamics as gd
import gala.potential as gp
from gala.units import galactic
directory = "Feb3/"
filename = "v10_225_p5_n01_dt01_NoZ"

# %%
orbitdict = {}
orbitcount = 0
maxIter = 500

# %%
noiselevel = 0.01
print('noise level is ',noiselevel)
w0 = gd.PhaseSpacePosition(pos=[5., 0., 0.]*u.kpc,vel=[10, 225, 0.]*u.km/u.s)
print('phase space position is ',w0)

# %%
while orbitcount < maxIter:
    print(f'orbit count = {orbitcount}')
    newpot = Galaxy.MWwNoise(N=noiselevel,units=galactic)
    neworbit = newpot.integrate_orbit(w0, dt=0.01 * u.Myr, n_steps=10000)
    orbitdict[str(noiselevel)+'_'+str(orbitcount)] = neworbit
    orbitcount += 1

# %%
with open(directory+filename+'.pkl', 'wb') as f:
    pickle.dump(orbitdict, f)

# %%
x = datetime.datetime.now()
print(x-y)