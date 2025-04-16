"""
GROMACS commands for installation and run:
Note: These commands should be run on Linux terminal
# Installation:
1.	$ sudo apt update
2.	$ sudo apt install cmake
3.	$ sudo apt install build-essential
4.	$ wget https://ftp.gromacs.org/gromacs/gromacs-2025.1.tar.gz
5.	$ tar xfz gromacs-2025.1.tar.gz
6.	$ cd gromacs-2025.1
7.	$ mkdir build
8.	$ cd build
9.	$ cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON
10.	$ make
11.	$ make check
12.	$ sudo make install
13.	$ source /usr/local/gromacs/bin/GMXRC
# Running GROMACS:
1.	$ grep -v HOH your_molecule.pdb > your_molecule_clean.pdb
2.	$ gmx pdb2gmx -f your_molecule_clean.pdb -o your_molecule_processed.gro -water spce -ignh
3.	$ gmx editconf -f 1AKI_processed.gro -o 1AKI_newbox.gro -c -d 1.0 -bt cubic
4.	$ gmx solvate -cp 1AKI_newbox.gro -cs spc216.gro -o 1AKI_solv.gro -p topol.top
5.	$ nano ions.mdp
6.	$ gmx grompp -f ions.mdp -c 1AKI_solv.gro -p topol.top -o ions.tpr
7.	$ gmx genion -s ions.tpr -o 1AKI_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
8.	$ nano em.mdp
9.	$ gmx grompp -f em.mdp -c 1AKI_solv_ions.gro -p topol.top -o em.tpr
10.	$ gmx mdrun -v -deffnm em
11.	$ gmx energy -f em.edr -o potential.xvg 
12.	$ nano nvt.mdp
13.	$ gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
14.	$ gmx mdrun -v -deffnm nvt 
15.	$ gmx energy -f nvt.edr -o temperature.xvg
16.	$ nano npt.mdp 
17.	$ gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
18.	$ gmx mdrun -v -deffnm npt
19.	$ gmx energy -f npt.edr -o pressure.xv
20.	$ gmx energy -f npt.edr -o density.xvg
21.	$ nano md.mdp
Note: Calculation - 1 ns = 1000 ps
                                1 fs = 0.001 ps
                                2 x 5,00,000 steps = 1000 ps = 1 ns
          Change it accordingly as per the required time duration
22.	$ gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr
23.	$ gmx mdrun -v -deffnm md_0_1 -nb gpu
24.	$ gmx trjconv -s md_0_1.tpr -f md_0_1.xtc -o md_0_1_noPBC.xtc -pbc mol -center
25.	$ gmx rms -s md_0_1.tpr -f md_0_1_noPBC.xtc -o rmsd.xvg -tu ns
"""