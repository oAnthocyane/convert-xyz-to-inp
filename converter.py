import os


CHARGE = 0
MULTIPLICITY = 1


def get_coord(file):
    inp = file.readlines()[2:]
    return "\n".join(inp)


def writer(inp_file):
    template = f"""! r2scan-3c 
! OptTs TightOpt Freq

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
xyz_files = [file for file in list_dir if ".xyz" in file]


for xyz_file in xyz_files:
    el_xyz_file = open(xyz_file, "r")
    ans = get_coord(el_xyz_file)
    
    name_xyz_file = xyz_file[:-4]
    name_file_inp = name_xyz_file + ".inp"
    inp_file = open(name_file_inp, "w")
    template = writer(ans)
    inp_file.write(template)

    inp_file.close()
    xyz_file.close()

