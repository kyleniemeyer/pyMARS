#trims reaction mechanism files

import cantera as ct
import os
import sys


solution_objects=[]

def readin(data_file, exclusion_list):
    """Function to import data file and identify format.

    Parameters
    ----------
    data_file:
        Local Chemkin or Cantera data file containing mechanism information
    exclusion_list:
        list of species to trim
    Returns
    -------
        Converted mechanism file
        Trimmed Solution Object
        Trimmed Mechanism file
    """
    global solution_objects
    #import working functions
    from create_trimmed_model import create_trimmed_model
    from convert_chemkin_file import convert
    from write_to_cti import write
    from chemkin_user_prompt import ask

    if data_file.endswith(".xml") or data_file.endswith(".cti"):
        print("This is an Cantera xml or cti file")
        #trims file
        solution_objects=create_trimmed_model(data_file, exclusion_list)

    if data_file.endswith(".inp") or data_file.endswith('.dat') \
                or data_file.endswith('.txt'):
        print("This is a Chemkin file")
        ask()
        #convert file to cti
        converted_file_name = convert(data_file)

        #trims newly converted file
        solution_objects=create_trimmed_model(converted_file_name, \
                                    exclusion_list)
    else:
        print("File type not supported")

    write(data_file, solution_objects)

    return (solution_objects)


if __name__ == '__main__':
    readin(sys.argv[0], sys.argv[1])
