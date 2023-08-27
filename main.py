from workspace.toWork import WorkSpace

def run_project():
    work_space = WorkSpace('/home/ubuntu/repo/phenotypic-data-warehouse/directory')
    work_space.clean_workspace()
    work_space.prepare_folder_files('dataverse_files.zip')
    work_space.storage_on_database()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_project()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
