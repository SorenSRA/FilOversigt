from os.path import join, getmtime, isfile
from os import listdir
import datetime


import fildates.constants as c


def print_folder_list(project):
    for folder in project.distspec.values():
        file_path = join(project.pathroot, project.pathspec, folder)
        file_list = (listdir(file_path))
        print(file_path)
        for file in file_list:
            if isfile(join(file_path, file)):
                modified_time = getmtime(join(file_path, file))
                print("\t" + file + " : " + datetime.datetime.fromtimestamp(modified_time).strftime('%d-%m-%Y %H:%M:%S'))

    return



def create_file_list(pr):
    match pr:
        case "Nat":
            project = c.NatureMan()
        case "Open":
            project = c.Openwood()
        case "For":
            project = c.ForFit()
        case _:
            project = None

    if project:
        print_folder_list(project)
    else:
        print("Forkert angivelse af projekt: Gyldige arg.: Nat - Open - For")
