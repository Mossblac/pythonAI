import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = "."
    try:
        wk = os.path.abspath(working_directory)
        d = os.path.abspath(directory)
    except Exception:
        return 'Error: os.path.abspath failed'
    try:
        wk_norm = os.path.normpath(wk)
        d_norm = os.path.normpath(d)
    except Exception:
        return 'Error: os.path.normpath failed'
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