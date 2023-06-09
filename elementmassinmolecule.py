import re


def main():
    tc = input("This program works under the AGPL license, would you like to proceed [y/N]:  ")
    if tc.lower().strip() == "n":
        quit()
    elif tc.lower().strip() == "y":
        pass
    else:
        print("Input must be y or n")
        quit()
    choice = input("Would you like to use the converter or see the instructions [c/i]:  ")

    if choice.lower().strip() == 'c':
        conversion()

        while True:
            print()
            question = input("Would you like to continue [y/N]:  ")

            if question == "y":
                conversion()
                pass
            elif question == "n":
                break
            else:
                print("Input must be y or n")
    elif choice.lower().strip() == 'i':
        print("This tool calculates the portion of each element in a molecule. For accurate results, input the formula without consideration of structure.")
        print("For an example: Methanoic acid should be referred as C2H4O2, but not CH3COOH")
        print("Please note that it assumes that the atoms referred to are the most common isotope")
        print("Remember to have the codes with the first letter capitalised: Na not na or NA")
    else:
        print("Input must be c or i")
        quit()






def conversion():
    chemical = input("Formula:  ")
    regex  = [[elem[0], elem[1]] for elem in re.findall(r"([A-Z][a-z]?)(\d*)", chemical)]
    converted_data = convert(regex)
    atomic_masses = converted_data[0]
    mass = str(round(converted_data[1], 3))
    print()
    print(chemical+": "+mass)
    # creating an atomic masses list and putting it in the convert function
    for i in range(len(atomic_masses)):
        print(atomic_masses[i]['name'] + ': ' + atomic_masses[i]['mass'])


def convert(regex):
    mass = 0
    periodic_table = {
    "H": ("Hydrogen", 1.008),
    "He": ("Helium", 4.003),
    "Li": ("Lithium", 6.941),
    "Be": ("Beryllium", 9.012),
    "B": ("Boron", 10.81),
    "C": ("Carbon", 12.011),
    "N": ("Nitrogen", 14.007),
    "O": ("Oxygen", 15.999),
    "F": ("Fluorine", 18.998),
    "Ne": ("Neon", 20.18),
    "Na": ("Sodium", 22.99),
    "Mg": ("Magnesium", 24.305),
    "Al": ("Aluminum", 26.982),
    "Si": ("Silicon", 28.086),
    "P": ("Phosphorus", 30.974),
    "S": ("Sulfur", 32.06),
    "Cl": ("Chlorine", 35.45),
    "Ar": ("Argon", 39.948),
    "K": ("Potassium", 39.098),
    "Ca": ("Calcium", 40.078),
    "Sc": ("Scandium", 44.956),
    "Ti": ("Titanium", 47.867),
    "V": ("Vanadium", 50.942),
    "Cr": ("Chromium", 52.0),
    "Mn": ("Manganese", 54.938),
    "Fe": ("Iron", 55.845),
    "Co": ("Cobalt", 58.933),
    "Ni": ("Nickel", 58.693),
    "Cu": ("Copper", 63.546),
    "Zn": ("Zinc", 65.38),
    "Ga": ("Gallium", 69.723),
    "Ge": ("Germanium", 72.63),
    "As": ("Arsenic", 74.922),
    "Se": ("Selenium", 78.96),
    "Br": ("Bromine", 79.904),
    "Kr": ("Krypton", 83.798),
    "Rb": ("Rubidium", 85.468),
    "Sr": ("Strontium", 87.62),
    "Y": ("Yttrium", 88.906),
    "Zr": ("Zirconium", 91.224),
    "Nb": ("Niobium", 92.906),
    "Mo": ("Molybdenum", 95.94),
    "Tc": ("Technetium", 98.0),
    "Ru": ("Ruthenium", 101.07),
    "Rh": ("Rhodium", 102.91),
    "Pd": ("Palladium", 106.42),
    "Ag": ("Silver", 107.87),
    "Cd": ("Cadmium", 112.41),
    "In": ("Indium", 114.82),
    "Sn": ("Tin", 118.71),
    "Sb": ("Antimony", 121.76),
    "Te": ("Tellurium", 127.6),
    "I": ("Iodine", 126.9),
    "Xe": ("Xenon", 131.29),
    "Cs": ("Cesium", 132.91),
    "Ba": ("Barium", 137.33),
    "La": ("Lanthanum", 138.91),
    "Ce": ("Cerium", 140.12),
    "Pr": ("Praseodymium", 140.91),
    "Nd": ("Neodymium", 144.24),
    "Pm": ("Promethium", 145.0),
    "Sm": ("Samarium", 150.36),
    "Eu": ("Europium", 151.96),
    "Gd": ("Gadolinium", 157.25),
    "Tb": ("Terbium", 158.93),
    "Dy": ("Dysprosium", 162.5),
    "Ho": ("Holmium", 164.93),
    "Er": ("Erbium", 167.26),
    "Tm": ("Thulium", 168.93),
    "Yb": ("Ytterbium", 173.05),
    "Lu": ("Lutetium", 175.0),
    "Hf": ("Hafnium", 178.49),
    "Ta": ("Tantalum", 180.95),
    "W": ("Tungsten", 183.84),
    "Re": ("Rhenium", 186.21),
    "Os": ("Osmium", 190.23),
    "Ir": ("Iridium", 192.22),
    "Pt": ("Platinum", 195.08),
    "Au": ("Gold", 196.97),
    "Hg": ("Mercury", 200.59),
    "Tl": ("Thallium", 204.38),
    "Pb": ("Lead", 207.2),
    "Bi": ("Bismuth", 208.98),
    "Th": ("Thorium", 232.04),
    "Pa": ("Protactinium", 231.04),
    "U": ("Uranium", 238.03),
    "Np": ("Neptunium", 237.05),
    "Pu": ("Plutonium", 244.06),
    "Am": ("Americium", 243.06),
    "Cm": ("Curium", 247.07),
    "Bk": ("Berkelium", 247.07),
    "Cf": ("Californium", 251.08),
    "Es": ("Einsteinium", 252.08),
    "Fm": ("Fermium", 257.1),
    "Md": ("Mendelevium", 258.1),
    "No": ("Nobelium", 259.1),
    "Lr": ("Lawrencium", 262.11),
    "Rf": ("Rutherfordium", 261.11),
    "Db": ("Dubnium", 262.11),
    "Sg": ("Seaborgium", 266.12),
    "Bh": ("Bohrium", 264.12),
    "Hs": ("Hassium", 267.13),
    "Mt": ("Meitnerium", 268.14),
    "Ds": ("Darmstadtium", 271.15),
    "Rg": ("Roentgenium", 272.15),
    "Cn": ("Copernicium", 285.183),
    "Nh": ("Nihonium", 284.178),
    "Fl": ("Flerovium", 289.190),
    "Mc": ("Moscovium", 288.194),
    "Lv": ("Livermorium", 293.205),
    "Ts": ("Tennessine", 294.211),
    }
    atomic_masses = []

    for i in range(len(regex)):
        if regex[i][1] == '':
            regex[i][1] = '1'
    # Making sure that every element has its own 'default' value

        mass += periodic_table[regex[i][0]][1]*float(regex[i][1])
    for i in range(len(regex)):
        atomic_masses.append({"name": periodic_table[regex[i][0]][0], "mass": str(round((periodic_table[regex[i][0]][1]*float(regex[i][1])/mass)*100, 3))+"%"})
    # Printing the name of the element and its percentage of the mass of the element




    return (atomic_masses, mass)






if __name__ == "__main__":
    main()
