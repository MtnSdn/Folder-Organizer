import os
import shutil

def file_organize(dl_dir, filetype,directories):
    # change to the download folder
    os.chdir(dl_dir)
        # create directories
    for directory in directories:
        if not os._exists(directory):
            try:
                os.mkdir(directory)
            except:
                pass

    for files in os.scandir(dl_dir):
        if os.path.isdir(files):
            continue
        file_path = os.path.basename(files)
        file_extension = os.path.splitext(files)[1]
        for key in filetype.keys():
            for value in filetype[key]:  # match values with keys
                if file_extension in value:
                    shutil.move(file_path, "{}/{}".format(key, file_path))
                    break
            