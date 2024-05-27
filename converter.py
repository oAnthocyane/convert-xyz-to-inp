import os
import sys
import shutil

CHARGE = sys.argv[1]
MULTIPLICITY = sys.argv[2]

def get_coord(file):
    inp = file.readlines()[2:]
    return "".join(inp)

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
    if el.endswith(".xyz"):
        name_molecule = el
        break
else:
    raise AssertionError("No .xyz files found")

for name_molecule in list_dir:
    extension = name_molecule[-3:]
    if extension != "xyz":
        continue

    file_name = name_molecule[:-4]

    with open(name_molecule, "r") as xyz_file:
        ans = get_coord(xyz_file)

    inp_file_name = file_name + ".inp"
    with open(inp_file_name, "w") as inp_file:
        template = writer(file_template, ans)
        inp_file.write(template)

    dir_name = os.path.dirname(os.path.abspath(file_name))
    os.mkdir(file_name)
    first = os.path.join(dir_name, name_molecule)
    second = os.path.join(dir_name, file_name, name_molecule)
    shutil.copy(first, second)
    first = os.path.join(dir_name, inp_file_name)
    second = os.path.join(dir_name, file_name, inp_file_name)
    os.replace(first, second)
