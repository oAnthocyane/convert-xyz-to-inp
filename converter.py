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
    
    name_file = xyz_file[:-4]
    
    dir_name = os.path.dirname(os.path.abspath(__name__))
    
    name_file_inp = name_file + ".inp"
    inp_file = open(name_file_inp, "w")
    template = writer(ans)
    inp_file.write(template)

    inp_file.close()
    el_xyz_file.close()
    
    os.mkdir(name_file)
    first = dir_name + "\\" + xyz_file
    second = dir_name + "\\" + name_file + "\\" + xyz_file
    os.replace(first, second)
    first = dir_name + "\\" + name_file_inp
    second = dir_name + "\\" + name_file + "\\" + name_file_inp
    os.replace(first, second)

