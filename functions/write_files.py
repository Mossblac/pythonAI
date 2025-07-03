import os
from google.genai import types

def write_file(working_directory, file_path, content):
    if file_path == None:
        file_path = "."
    try:
        pathdir = os.path.join(working_directory, file_path)
        wk = os.path.abspath(working_directory)
        f = os.path.abspath(pathdir)
    except Exception:
        return 'Error: os.path.abspath or os.path.join failed'
    
    try:
        wk_norm = os.path.normpath(wk)
        d_norm = os.path.normpath(f)
    except Exception:
        return 'Error: os.path.normpath failed'
    
    if d_norm == wk_norm or d_norm.startswith(wk_norm + os.sep):
            if os.path.exists(f) == False:
                try:
                    os.makedirs(f)
                except Exception:
                    return 'Error: failed to create directory'
            try:
                with open(f, "w") as file:
                    file.write(content)
            except Exception:
                return 'Error: write to file failed'
            try:
                with open(f, "r") as file:
                    new_content = file.read()
                    if new_content == content:
                        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            except Exception:
                return 'Error: failed to verify content written'
    else:
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="create and write to files, then list what was written. constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT, 
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file destination",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="what is being written to the file"
            )
        },
    ),
)
    
    