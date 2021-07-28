'''
This code will hopefully turn a GAMESS coordinate file, with the structure:

C 12 2.718281 3.1415926 6.626070

To something as:

C 12 2.718281 3.1415926 6.626070
S   6
1         0.3047524880E+04       0.1834737132E-02
2         0.4573695180E+03       0.1403732281E-01
3         0.1039486850E+03       0.6884262226E-01
4         0.2921015530E+02       0.2321844432E+00
5         0.9286662960E+01       0.4679413484E+00
6         0.3163926960E+01       0.3623119853E+00
L   3
1         0.7868272350E+01      -0.1193324198E+00       0.6899906659E-01
2         0.1881288540E+01      -0.1608541517E+00       0.3164239610E+00
3         0.5442492580E+00       0.1143456438E+01       0.7443082909E+00
L   1
1         0.1687144782E+00       0.1000000000E+01       0.1000000000E+01
D   1
1         0.8000000000E+00       1.0000000
'''

#this first dictionary allows to change from element symbol, to name
#names were written according to how BSE displays them, however, it is not
#imposible for confusions to arise (e.g. aluminium and aluminum) if a basis
#is not taken from BSE
def sym2name(symbol):
    dictio = {
    "H": "HYDROGEN",
    "He": "HELIUM",
    "Li": "LITHIUM",
    "Be": "BERYLLIUM",
    "B": "BORON",
    "C": "CARBON",
    "N": "NITROGEN",
    "O": "OXYGEN",
    "F": "FLUORINE",
    "Ne": "NEON",
    "Na": "SODIUM",
    "Mg": "MAGNESIUM",
    "Al": "ALUMINIUM",
    "Si": "SILICON",
    "P": "PHOSPHORUS",
    "S": "SULFUR",
    "Cl": "CHLORINE",
    "Ar": "ARGON",
    "K": "POTASSIUM",
    "Ca": "CALCIUM",
    "Sc": "SCANDIUM",
    "Ti": "TITANIUM",
    "V": "VANADIUM",
    "Cr": "CHROMIUM",
    "Mn": "MANGANESE",
    "Fe": "IRON",
    "Co": "COBALT",
    "Ni": "NICKEL",
    "Cu": "Copper",
    "Zn": "ZINC",
    "Ga": "GALLIUM",
    "Ge": "GERMANIUM",
    "As": "ARSENIC",
    "Se": "SELENIUM",
    "Br": "BROMINE",
    "Kr": "KRYPTON",
    "Rb": "RUBIDIUM",
    "Sr": "STRONTIUM",
    "Y": "YTTRIUM",
    "Zr": "ZIRCONIUM",
    "Nb": "NIOBIUM",
    "Mo": "MOLYBDENUM",
    "Tc": "TECHNETIUM",
    "Ru": "RUTHENIUM",
    "Rh": "RHODIUM",
    "Pd": "PALLADIUM",
    "Ag": "SILVER",
    "Cd": "CADMIUM",
    "In": "INDIUM",
    "Sn": "TIN",
    "Sb": "ANTIMONY",
    "Te": "TELLURIUM",
    "I": "IODINE",
    "Xe": "XENON",
    "Cs": "CAESIUM",
    "Ba": "BARIUM",
    "La": "LANTHANUM",
    "Ce": "CERIUM",
    "Pr": "PRASEODYMIUM",
    "Nd": "NEODYMIUM",
    "Pm": "PROMETHIUM",
    "Sm": "SAMARIUM",
    "Eu": "EUROPIUM",
    "Gd": "GADOLINIUM",
    "Tb": "TERBIUM",
    "Dy": "DYSPROSIUM",
    "Ho": "HOLMIUM",
    "Er": "ERBIUM",
    "Tm": "THULIUM",
    "Yb": "YTTERBIUM",
    "Lu": "LUTETIUM",
    "Hf": "HAFNIUM",
    "Ta": "TANTALUM",
    "W": "TUNGSTEN",
    "Re": "RHENIUM",
    "Os": "OSMIUM",
    "Ir": "IRIDIUM",
    "Pt": "PLATINUM",
    "Au": "GOLD",
    "Hg": "MERCURY",
    "Ti": "THALLIUM",
    "Pb": "LEAD",
    "Bi": "BISMUTH",
    "Po": "POLONIUM",
    "At": "ASTATINE",
    "Rn": "RADON",
    "Fr": "FRANCIUM",
    "Ra": "RADIUM",
    "Ac": "ACTINIUM",
    "Th": "THORIUM",
    "Pa": "PROTACTINIUM",
    "U": "URANIUM",
    "Np": "NEPTUNIUM",
    "Pu": "PLUTONIUM",
    "Am": "AMERICIUM",
    "Cm": "CURIUM",
    "Bk": "BERKELIUM",
    "Cf": "CALIFORNIUM",
    "Es": "EINSTEINIUM",
    "Fm": "FERMIUM",
    "Md": "MENDELEVIUM",
    "No": "NOBELIUM",
    "Lr": "LAWRENCIUM",
    "Rf": "RUTHERFORDIUM",
    "Db": "DUBNIUM",
    "Sg": "SEABORGIUM",
    "Bh": "BOHRIUM",
    "Hs": "HASSIUM",
    "Mt": "MEITNERIUM",
    "Ds": "DARMSTADTIUM",
    "Rg": "ROENTGENIUM",
    "Cn": "COPERNICIUM",
    "Nh": "NIHONIUM",
    "Fl": "FLEROVIUM",
    "Mc": "MOSCOVIUM",
    "Lv": "LIVERMORIUM",
    "Ts": "TENNESSINE",
    "Og": "OGANESSON"
    }

    return dictio[symbol]
import sys 


file = sys.argv[1]
atomsnbasis = sys.argv[2]


# In order to make sure the files will be opened, we import the full
# working directory of both
import os
pwd = os.path.dirname(__file__)

if os.path.exists("Output.txt"):
    os.remove("Output.txt")
inputcoord = os.path.join(pwd, file)
inputmix = os.path.join(pwd, atomsnbasis)

# The following section extracts the atom types and the basis set to use
# for each of them
with open(inputmix, 'r') as mix:
    #splitting by \n allows to read the file line by line
    mixdata = mix.read().split('\n')
    atomtypes = []
    basissets = []
    for line_number,line in enumerate(mixdata):
        #the following is a life saver, and will exit the loop if the line is empty
        if len(line.split()) == 0: break
        #save the first element of the line to the atom list
        atom = line.split()[0]
        #save the second element of the line to the basis set list
        basis = line.split()[1]
        atomtypes.append(atom)
        basissets.append(basis)
        # each atom type is related to its basis set by the index number in each list

    nametypes = []
    # Change the chemical symbol to name of the element, since that's how
    # they appear in basis sets
    for k in range(len(atomtypes)):
        atomname = sym2name(atomtypes[k])
        nametypes.append(atomname)
#print(atomtypes)
#print(nametypes)
#print(basissets)

functionstouse = []
# Now we read the basis files, and write some temporary files with the info of each
# elemnt. The first for loops as many times as atom types are in the inputmix file
for i in range(len(atomtypes)):
    # Now open the basis set files
    with open(basissets[i], 'r') as thebasefile:
        # given the structure of the files from BSE in GAMESS US format
        # the basis file is separated by blank lines. Each "paragraph"
        # has the information of one elemnt
        baseinfo = thebasefile.read().split('\n\n')
        if not baseinfo:
            # if there is nothing after the empty line, exit the loop
            pass
        # Now, make decisions base on the content of the paragraph
        # the loop goes as many times, as paragraphs there are in the basis set file
        for atomdatainbase in baseinfo:
            # this flag will tell us if there is a match with the atom we are
            # looking for. Initially, we asume there is no match.
            flag = 0
            # now, split the paragraph in lines
            eachline = atomdatainbase.split('\n')
            # the follwing loop goes through the elements of the line being read
            for thisistheline in eachline:
                # if the element of the line is the same as the atom we are looking
                # for, we set our flag to 1, we have a match
                if thisistheline == nametypes[i]:
                    flag = 1
            # if the indicating flag is 1, we begin working with our temporary files
            if flag == 1:
                # we read again the lines of the paragraph we are currently working
                # with, the one that turned the flag to 1
                for yetanotherline in eachline:
                    # since we don't need the atom name to be written again, we pass
                    # that line
                    if yetanotherline == nametypes[i]:
                        pass
                    # fo all other lines in the paragraph, we open a temporary file
                    # with the name of the element, write the line and jump to another line
                    else:
                        tempo = open(nametypes[i], "a")
                        tempo.write(yetanotherline)
                        tempo.write("\n")
                        tempo.close
# We open the input with the coordinates
with open(inputcoord, 'r') as coord:
    # separate by lines, since each line represent an atom in the structure
    coorddata = coord.read().split('\n')
    # this for loops as many times as lines there are in the input file
    for inputline in coorddata:
        # life saver, if the line is empty, exit the loop
        if len(inputline.split()) == 0: break
        # now open the final output, and write that line
        output = open("Output.txt", "a")
        output.write(inputline)
        # the atom type to be described in that line is saved to theatomintheline
        theatomintheline = inputline.split()[0]
        # this for loops as many times as atom types have been included in the input mix
        for j in range(len(atomtypes)):
            # we have the list, called atomtypes, in which atoms from the input have
            # been stored with their symbol, so we compare with that
            if theatomintheline == atomtypes[j]:
                output.write('\n')
                # if the symbols are the same, we open the temporary file as "extractor"
                with open(nametypes[j], 'r') as extractor:
                    # we split the extractor file in lines
                    coef = extractor.read().split('\n')
                    # this for loops as many times as lines are in the temporary file
                    # proceed to write the info from the temporary file
                    for writer in coef:
                        output.write(writer)
                        output.write('\n')

        output.close
# this next section covers the case in which we use effective core potentials
# it just writes the flags needed in a GAMESS input and the chemical symbols with
# word NONE. The ECP will then have to be added manually to the output file
with open(inputcoord, 'r') as theinput:
    thedata = theinput.read().split('\n')
    out = open("Output.txt", "a")
    out.write(" $END")
    out.write('\n')
    out.write(" $ECP")
    out.write('\n')
    for inputline in coorddata:
        if len(inputline.split()) == 0: break
        theatomintheline = inputline.split()[0]
        out.write(" ")
        out.write(theatomintheline)
        out.write(" NONE")
        out.write('\n')
    out.write(" $END")
# almost done, now just remove the temporary files
for k in range(len(atomtypes)):
    filetoremove = os.path.join(pwd, nametypes[k])
    os.remove(filetoremove)

