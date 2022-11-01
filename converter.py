import os


CHARGE = 0
MULTIPLICITY = 1


def get_coord(file):
    inp = file.readlines()[2:]
    return "\n".join(inp)


def writer(inp_file):
    template = f"""! r2scan-3c 
! Opt TightOpt Freq

%pal nprocs 24 end

%geom 
 Calc_Hess TRUE
 end

* xyz {CHARGE} {MULTIPLICITY}
{inp_file}
*
"""
    return template


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
    template = writer(ans)
    inp_file.write(template)

    inp_file.close()
    xyz_file.close()
