import os
def rename_files():
    # get file names form a folder
                            #add your own file path
    file_list = os.listdir(r"/Users/nathancurtis/Desktop/Nathan/Coding/Python/prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    # add your own file path
    os.chdir(r"/Users/nathancurtis/Desktop/Nathan/Coding/Python/prank")

    # for each file, rename those files
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        # edit what you want removed from folder names. Currently, the function is set to remove numbers 0 - 9
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
