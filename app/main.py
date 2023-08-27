from workspace.toWork import WorkSpace
from database.schema import create_entities

    
workSpace = WorkSpace('/home/ubuntu/repo/database-cimmyt/directory')
workSpace.clean_workspace()
workSpace.start_file('dataverse_files.zip')
create_entities()

# # from fastapi import FastAPI
# from workspace.toWork import WorkSpace
# from database.schema import create_entities

# # app = FastAPI()


# # @app.get("/")
# # async def root():
# #     return {"version": "23.08.0001"}

# # @app.get('/start')
# # async def processFile(info_name: str, file_name: str):
#     workSpace = WorkSpace('/home/ubuntu/repo/database-cimmyt/directory')
#     print('Start to work')
#     workSpace.clean_workspace()
#     workSpace.start_file('dataverse_files.zip')
#     create_entities()
#     return {"status": "working"}
