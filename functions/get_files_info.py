import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = "."
    try:
        pathdir = os.path.join(working_directory, directory)
        wk = os.path.abspath(working_directory)
        d = os.path.abspath(pathdir)
    except Exception:
        return 'Error: os.path.abspath or os.path.join failed'

    # --- ADD THESE PRINT STATEMENTS ---
    #print(f"DEBUG: Initial working_directory: {working_directory}")
    #print(f"DEBUG: Initial directory: {directory}")
    #print(f"DEBUG: abspath wk: {wk}")
    #print(f"DEBUG: abspath d: {d}")
    # --- END ADDITION ---

    try:
        wk_norm = os.path.normpath(wk)
        d_norm = os.path.normpath(d)
    except Exception:
        return 'Error: os.path.normpath failed'

    # --- ADD THESE PRINT STATEMENTS ---
    #print(f"DEBUG: normpath wk_norm: {wk_norm}")
    #print(f"DEBUG: normpath d_norm: {d_norm}")
    #print(f"DEBUG: Comparison: d_norm == wk_norm ({d_norm == wk_norm})")
    #print(f"DEBUG: Comparison: d_norm.startswith(wk_norm + os.sep) ({d_norm.startswith(wk_norm + os.sep)})")
    #print(f"DEBUG: Final condition result: {d_norm == wk_norm or d_norm.startswith(wk_norm + os.sep)}")
    # --- END ADDITION ---

    if d_norm == wk_norm or d_norm.startswith(wk_norm + os.sep):
        if os.path.isdir(d) == False:
            return (f'Error: "{directory}" is not a directory')
        try:
            contents = os.listdir(d)
        except Exception:
            return ('Error: listdir() failed' )
        if len(contents) == 0:
            return ""
        else:
            file_list = []
            for file in contents:
                file_name = file
                try:
                    file_size = os.path.getsize(os.path.join(d,file))
                except Exception:
                    return "Error: os.path.getsize() returned error"
                if os.path.isdir(os.path.join(d,file)):
                    is_dir = True
                else:
                    is_dir = False
                file_string = f'- {file_name}: file_size={file_size} bytes, is_dir={is_dir}'
                file_list.append(file_string)
    else:
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    return "\n".join(file_list)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)