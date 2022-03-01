# Datagroup_builder
This is a code that allows one to create a $DATA group for GAMESS with a mixture of basis sets

The basic use is: We save the basis sets we are interested in from BSE to our computer in GAMESS US format
We lose the $DATA and $END flags, the code reads from the first atom (possibly HYDROGEN, but it's your choice)
and until the last exponen/coefficient.
After that, we will need a file that has the atoms and coordinates that we will use to build out $DATA group.
The basis structure of this file should be:

C   6.0   X.XXXX   Y.YYYY   Z.ZZZZZ 

H   1.0   X.XXXX   Y.YYYY   Z.ZZZZZ 

Notice that this file should only have this information, no $DATA, $END or anything different. Coordinates in this 
format can easily be obtained from most programs used in computational chemistry, as well as GAMESS official visualizer, 
wxMacMolPlt.

We then need a file where we indicate the types of atoms present in our system (H, C, O, etc.) and the file that contains
the basis set for each atom. Example:

H 6-31Gd.txt

C STO3G.txt

...

Xe STO3G.txt

Now, there's a bug that messes up the functions of the last atom in that list, but you can easily get around it by simply
adding an atom that's not in you system at the end, and a basis set file that contains it. Xe is used in the example,
but it can be anything as long as it's not present in you coordinate file.

When you execute the program, it will first ask for the file with the coordinates (i.e. the input), and after that it
will ask for the file with the "Atom - Basis set to use" information. You must include the format of the file, or the 
program won't find it (e.g. 'mybasismix.txt', instead of just 'mybasismix')

After that, the program will do its job and provide you with a nice file called 'Output.txt', whose content you can 
simply copy/paste to your input file.

To run the code, you can go to the comand line/terminal in you device, then type 'python3 ./Main.py', and the program 
will begin running. All files required, including an example, can be found in this repository. 

