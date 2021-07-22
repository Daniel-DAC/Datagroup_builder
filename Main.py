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

print("This program requires the following structure in the coordinate file:")
print("AtomicSymbol AtomicNumber X.XXXXX Y.YYYYY Z.ZZZZZ")

file = input("Provide the full name of the file with the coordinate system: \n")
atomsnbasis = input("Provide the full name of the file with the atoms and basis sets to use \n")

import os
pwd = os.path.dirname(__file__)

if os.path.exists("Output.txt"):
    os.remove("Output.txt")
inputcoord = os.path.join(pwd, file)
inputmix = os.path.join(pwd, atomsnbasis)

with open(inputmix, 'r') as mix:
    mixdata = mix.read().split('\n')
    atomtypes = []
    basissets = []
    for line_number,line in enumerate(mixdata):
        if len(line.split()) == 0: break
        atom = line.split()[0]
        basis = line.split()[1]
        atomtypes.append(atom)
        basissets.append(basis)

    nametypes = []
    for k in range(len(atomtypes)):
        atomname = sym2name(atomtypes[k])
        nametypes.append(atomname)

#    print(nametypes)
#    print(basissets)
functionstouse = []
for i in range(len(atomtypes)):
    with open(basissets[i], 'r') as thebasefile:
        baseinfo = thebasefile.read().split('\n\n')
        if not baseinfo:
            pass
        for atomdatainbase in baseinfo:
            flag = 0
            eachline = atomdatainbase.split('\n')
            for thisistheline in eachline:
                if thisistheline == nametypes[i]:
                    flag = 1
            if flag == 1:
                for yetanotherline in eachline:
                    if yetanotherline == nametypes[i]:
                        pass
                    else:
                        tempo = open(nametypes[i], "a")
                        tempo.write(yetanotherline)
                        tempo.write("\n")
                        tempo.close

with open(inputcoord, 'r') as coord:
    coorddata = coord.read().split('\n')

    for inputline in coorddata:
        if len(inputline.split()) == 0: break
        output = open("Output.txt", "a")
        output.write(inputline)
        theatomintheline = inputline.split()[0]
        for j in range(len(atomtypes)):
            if theatomintheline == atomtypes[j]:
                output.write('\n')
                with open(nametypes[j], 'r') as extractor:
                    coef = extractor.read().split('\n')
                    for writer in coef:
                        output.write(writer)
                        output.write('\n')

        output.close

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

for k in range(len(atomtypes)):
    filetoremove = os.path.join(pwd, nametypes[k])
    os.remove(filetoremove)
