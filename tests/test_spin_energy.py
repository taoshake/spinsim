import numpy as np
from spinsim.spin2 import energy
def test_energy():
    print(energy(1,np.array([1,1,1]), np.array([-1,-1,-1])))
test_energy()
