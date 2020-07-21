import numpy as np
import pandas as pd


# All units of length are in Angstroms unless stated otherwise.


def get_coordinates(filename):
    """ Extract information about atoms and their coordinates from .xyz file."""
    with open(filename, "r") as f:
        data = []
        lines = f.readlines()
        for line in lines:
            data.append(line.split())
    N = int(data[0][0])
    data = data[2:]
    atom_types, coords = [], []
    for x in range(N):
        atom_types.append(data[x][0])
        coords.append([float(data[x][1]), float(data[x][2]), float(data[x][3])])
    return atom_types, coords


data = pd.read_csv("covalent_radii.txt")
atoms, radii = data['atom'], data['r'] * 0.01
covalent_radii = dict(zip(atoms, radii))


def get_bonds(atom_types, coords):
    """ Finds which atoms are bonded. """
    print("\nThe bonded atoms are: ")
    bonds = []
    for x in range(len(atom_types)):
        r1 = covalent_radii[atom_types[x]]
        for y in range(x + 1, len(atom_types)):
            r2 = covalent_radii[atom_types[y]]
            r12 = 0
            for z in range(3):
                r12 += (coords[x][z] - coords[y][z]) ** 2
            r12 = np.sqrt(r12)
            if r12 < 1.3 * (r1 + r2):
                print("%s%d" % (atom_types[x], (x + 1)), "- %s%d" % (atom_types[y], (y + 1)))
                bonds.append([atom_types[x] + str(x + 1), coords[x], atom_types[y] + str(y + 1), coords[y]])
    return bonds


def get_bond_lengths(bonds):
    """ Obtain the bond lengths from coordinates of bonded atoms."""
    print("\nThe bond lengths are: ")
    bond_lengths = []
    for x in range(len(bonds)):
        bl = 0
        for z in range(3):
            bl += (bonds[x][1][z] - bonds[x][3][z]) ** 2
        bl = np.sqrt(bl)
        print("l(%s-%s) = %0.3f Å" % (bonds[x][0], bonds[x][2], bl))
        bond_lengths.append([bonds[x][0], bonds[x][2], bl])
    return bond_lengths


def get_angle(x, y, z):
    """ Gives angle of x-y-z bond. """
    for i in range(len(bonds)):
        for j in [0, 2]:
            if bonds[i][j] == x:
                coord1 = bonds[i][j + 1]
            if bonds[i][j] == y:
                coord2 = bonds[i][j + 1]
            if bonds[i][j] == z:
                coord3 = bonds[i][j + 1]

    v1 = np.array(coord2) - np.array(coord1)
    v2 = np.array(coord2) - np.array(coord3)

    v1_mag, v2_mag, v = 0, 0, 0
    for a in range(3):
        v1_mag += v1[a] ** 2
        v2_mag += v2[a] ** 2
        v += v1[a] * v2[a]
    v1_mag = np.sqrt(v1_mag)
    v2_mag = np.sqrt(v2_mag)

    theta = (180 / np.pi) * np.arccos(v / (v1_mag * v2_mag))
    print("\nThe %s-%s-%s angle is : %0.3f˚" % (x, y, z, theta))
    return theta
