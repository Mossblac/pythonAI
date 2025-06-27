import os


def get_file_content(working_directory, file_path):
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
        #try:
            if os.path.isfile(f):
                max_characters = 10000
                with open(f, "r") as file:
                    file_content_string = file.read()
                    if len(file_content_string) > 10000:
                        print(f'...File "{file_path}" truncated at 10000 characters')
                        for word in file_content_string:
                        #file_content_string = file.read(max_characters)
                        return file_content_string
                    else:
                        return file_content_string
            else:
                return f'Error: File not found or is not a regular file: "{f}"'        
        #except Exception:
            #return "Error: os.path.isfile failed or file failed to read"
        
    else:
        return (f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')