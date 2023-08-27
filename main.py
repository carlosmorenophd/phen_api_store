from workspace.toWork import WorkSpace
from database.schema import create_entities


def run_project():
    work_space = WorkSpace('/home/ubuntu/repo/phenotypic-data-warehouse/directory')
    work_space.clean_workspace()
    work_space.start_file('dataverse_files.zip')
    create_entities()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_project()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
