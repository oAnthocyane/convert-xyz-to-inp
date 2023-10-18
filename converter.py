import os
import sys


CHARGE = sys.argv[0]
MULTIPLICITY = sys.argv[1]


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

file_template_name = sys.argv[2]
file_template = open(file_template_name, "r").readlines()

list_dir = os.listdir()

for el in list_dir:
    if ".xyz" in el:
        name_molecule = el
        break
else:
    assert "Not have files"

name_molecule = name_molecule[:-6]
count_files = len(list_dir) - 1

for i in range(count_files):
    counter = i+1
    counter_s = ("0" + str(counter)) if counter < 10 else str(counter)
    file_name = name_molecule + counter_s

    xyz_file_name = file_name + ".xyz"
    xyz_file = open(xyz_file_name, "r")
    ans = get_coord(xyz_file)
    
    inp_file_name = file_name + ".inp"
    inp_file = open(inp_file_name, "w")
    template = writer(file_template, ans)
    inp_file.write(template)

    inp_file.close()
    xyz_file.close()
