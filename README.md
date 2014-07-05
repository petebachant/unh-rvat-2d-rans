UNH-RVAT 2D OpenFOAM case
=========================

OpenFOAM (2.3.x) case files for a 2D RANS simulation of the UNH-RVAT cross-flow
turbine in a towing tank. The simulation uses the `pimpleDyMFoam` solver and the
`kOmegaSST` turbulence model. 

Note that this simulation has not been verified or validated.

Python scripts
--------------
There are some Python scripts included to perform various tasks. Note that these
require [foamPy](https://github.com/petebachant/foamPy.git).

  * `perf.py` -- calculates performance of turbine, plots torque.
  * `gendynmeshdict.py` -- generates a dynamicMeshDict to rotate the turbine. 
    Note that by defaults the turbine rotates at an angular velocity that is 
    slightly unsteady to match experiments.
  * `prog.py` -- creates a progress bar using PyQt.
  
Tagged commits
--------------

### `mesh0`
  * 139k cells
  * Average `yPlus` at 6 s: 2.44 at blades, 0.944 at shaft
  * Mean `C_P` from 360 deg to 6 s: 0.51
  * `maxCo`: 20
  * On `kOmegaSSTLowRe` branch, mean `C_P` is 0.51. `yPlus` values are close
    as well.

Video
-----
A video of the vorticity contours produced by this simulation (commit
5aee960afcda71cc3398a6f417780fd3d5e978ba, OpenFOAM version 2.2.2) can be
found here: http://youtu.be/AQ4EztjPEFk

Acknowledgements
----------------
Thanks to Boloar from the cfd-online forums for providing a nice example case on
which to base this one. Also thanks to vkrastev for additional advice.

