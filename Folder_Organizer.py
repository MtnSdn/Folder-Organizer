import json
import os
import Observer


class Folder_Organize():
    def create_folders(self):
        with open("Extensions.json", "r+") as jsonfile:
            data = json.load(jsonfile)
            # set download folder
            if data["download_dir"] == "":
                jsonfile.seek(0)
                jsonfile.truncate()
                # download directory
                dl_dir = input("Enter your download folder path : ")
                data["download_dir"] = dl_dir
                json.dump(data, jsonfile, indent=2)

            # variables
            self.dl_dir = data["download_dir"]
            self.directories = [directory for directory in data["filetypes"]
                                for directory in directory]
            self.filetypes = data["filetypes"]


folders = Folder_Organize()
folders.create_folders()
Observer.run_handler(folders.dl_dir, folders.filetypes)
