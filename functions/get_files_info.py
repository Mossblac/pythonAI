import os

def get_files_info(working_directory, directory=None):
    #if os.path.abspath(directory).startswith(os.path.abspath(working_directory)) == True:
        #return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if os.path.isdir(directory) == False:
        return (f'Error: "{directory}" is not a directory')
    contents = os.listdir(directory)
    if len(contents) == 0:
        return ('Error: directory is empty')
    else:
        content_string = ""
        for file in contents:
            file_name = file
            file_size = os.path.getsize(file)
            if os.path.isfile(file) == True:
                is_dir = False
            else:
                is_dir = True
            file_string = f'- {file_name}: file_size={file_size} bytes, is_dir={is_dir}'
    return content_string + file_string