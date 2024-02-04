:: Create a directory named "new_folder" in the current directory.
mkdir new_folder

:: Check if "new_folder" exists. If it does, create a directory named "if_folder."
if exist new_folder (mkdir if_folder)

:: Check if "if_folder" exists. If it does, create a directory named "hyperionDev"; otherwise, create "new_projects."
if exist if_folder (mkdir hyperionDev) else (mkdir new_projects)

:: List the contents of the current directory.
dir

