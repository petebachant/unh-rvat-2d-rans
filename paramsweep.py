#!/usr/bin/env python
"""
This script runs multiple simulations to check sensitivity to parameters.

"""
from subprocess import call
import foampy
import os
import processing
import pandas as pd

def set_blockmesh_resolution(nx):
    newres = nx
    resline = "({res} {res} 1)".format(res=newres)
    blocks = """blocks
(
    hex (0 1 2 3 4 5 6 7)
    {}
    simpleGrading (1 1 1)
);
""".format(resline)
    zres = 110.0/float(newres)*0.025
    vertices = """vertices
(
    ( 2.16 -1.83 -{z}) // 0
    ( 2.16  1.83 -{z}) // 1
    (-1.52  1.83 -{z}) // 2
    (-1.52 -1.83 -{z}) // 3
    ( 2.16 -1.83  {z}) // 4
    ( 2.16  1.83  {z}) // 5
    (-1.52  1.83  {z}) // 6
    (-1.52 -1.83  {z}) // 7 
);
""".format(z=zres)
    foampy.dictionaries.replace_value("constant/polyMesh/blockMeshDict", 
                                      "blocks", blocks)
    foampy.dictionaries.replace_value("constant/polyMesh/blockMeshDict", 
                                      "vertices", vertices)
                                      
def set_timestep(dt):
    dt = str(dt)
    foampy.dictionaries.replace_value("system/controlDict", "deltaT", dt)

def spatial_grid_dep():
    call("rm -f processed/spatial_grid_dep.csv", shell=True)
    nx_list = [35, 45, 55, 70, 85]
    for nx in nx_list:
        call("./Allclean")
        set_blockmesh_resolution(nx)
        call("./Allrun")
        processing.log_perf("spatial_grid_dep.csv", verbose=False)
        
def timestep_dep():
    call("rm -f processed/timestep_dep.csv", shell=True)
    dt_list = [8e-3, 4e-3, 2e-3, 1e-3, 7e-4, 5e-4]
    for dt in dt_list:
        call("./Allclean")
        set_timestep(dt)
        call("./Allrun")
        processing.log_perf("timestep_dep.csv", verbose=False)
                            
if __name__ == "__main__":
    timestep_dep()
