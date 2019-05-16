#!/usr/bin/python3.4m

import numpy
import os
import sys

def cal_dis(atom1,atom2):
    """
    Calculate the distance beween two atoms.

    Parameters
    ----------
    atom1: list
        A list of coordinates [x,y,z]
    atom2: list
        A list of coordinates [x,y,z]

    Returns
    -------
    distance: float
        The distance between atoms.

    Examples
    --------
    >>> cal_dis([0,0,0], [0,0,1])
    1.0
    """
    x_dis = atom1[0]-atom2[0]
    y_dis = atom1[1]-atom2[1]
    z_dis = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_dis**2 + y_dis**2 + z_dis**2)
    return distance

def bond_check(bond_dis,minimum=0,maximum=1.5):
    """
    Check if the distance is a bond.

    Parameters
    ----------
    bond_dis: float
        The distance between atoms
    minimum: float
        The minimum distance for a bond
    maximum: float
        The maximum distance for a bond

    Returns
    -------
    True if bond
    False if not a bond
    """
    if not isinstance(bond_dis, float):
        raise TypeError(F'bond_dis must be type float. (bond_dis)')

    if (bond_dis>minimum and bond_dis<maximum):
        return 1
    else:
        return 0

def open_xyz(filename):
    xyz = numpy.genfromtxt(fname=filename,skip_header=2,dtype='unicode')
    atoms = xyz[:,0]
    coord = xyz[:,1:]
    coord = coord.astype(numpy.float)
    return atoms, coord

if __name__ == "__main__":
   if len(sys.argv) < 2:
      raise IndexError('No file name given. Script requires an xyz file')
   xyz_file = sys.argv[1]

   atoms, coord = open_xyz(xyz_file)

   for numA, atomA in enumerate(coord):
       for numB, atomB in enumerate(coord):
           if numB<numA:
              distance_AB = cal_dis(atomA,atomB)
              if bond_check(distance_AB) == 1:
                print(str(atoms[numA])+ ' ' + 'to' + ' ' + str(atoms[numB]) + ' ' + ':' + ' ' + str(distance_AB))
