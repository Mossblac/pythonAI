import os

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
                return 'Error: os.makedirs() failed'
            
        if os.path.exists(f):
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
        return (f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')