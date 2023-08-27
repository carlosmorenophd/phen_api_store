
# from workspace.toWork import WorkSpace
# from database.schema import create_entities

    
# workSpace = WorkSpace('/home/ubuntu/repo/database-cimmyt/directory')
# workSpace.clean_workspace()
# workSpace.start_file('dataverse_files.zip')
# create_entities()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

