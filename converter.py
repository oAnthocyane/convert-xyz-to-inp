import os
import sys


CHARGE = sys.argv[1]
MULTIPLICITY = sys.argv[2]


def get_coord(file):
    inp = file.readlines()[2:]
    return "\n".join(inp)


def writer(calc_file, inp_file):
    start_values = "".join(calc_file)
    template = f"""{start_values}
* xyz {CHARGE} {MULTIPLICITY}
{inp_file}
*
"""
    return template

file_template_name = sys.argv[3]
file_template = open(file_template_name, "r").readlines()

list_dir = os.listdir()

for el in list_dir:
    if ".xyz" in el:
        name_molecule = el
        break
else:
    assert "Not have files"
  
for name_molecule in list_dir:
    extension = name_molecule[-3:]
    if extension != "xyz": continue
    
    file_name = name_molecule[:-4]
        
    xyz_file = open(name_molecule, "r")
    ans = get_coord(xyz_file)
    
    inp_file_name = file_name + ".inp"
    inp_file = open(inp_file_name, "w")
    template = writer(file_template, ans)
    inp_file.write(template)

    inp_file.close()
    xyz_file.close()
    
    dir_name = os.path.dirname(os.path.abspath(name))
    os.mkdir(file_name)
    first = dir_name + "\\" + name_molecule
    second = dir_name + "\\" + file_name + "\\" + name_molecule
    os.replace(first, second)
    first = dir_name + "\\" + inp_file_name
    second = dir_name + "\\" + file_name + "\\" + inp_file_name
    os.replace(first, second)

