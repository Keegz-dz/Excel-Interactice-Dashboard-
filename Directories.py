import os


def create_root_folder_dir(root_folder_name: list) -> None:
    """ This Function takes a list as an argument containing Root Folder names in it and create a directory if it
    does not already exist"""
    try:
        for folder_dir in root_folder_name:
            if not os.path.exists(os.path.join(os.getcwd(), folder_dir)):
                os.mkdir(folder_dir)
    except OSError as e:
        raise Exception(f"Failed to create Folder director for {root_folder_name}: {e}")


def create_sub_folder_dir(root_folder_name: str, sub_folder_name: str) -> str:
    """ This Function takes two arguments : Root folder name and Sub folder name and creates a directory if it does not
    already exist and returns the sub folder directory absolute path"""
    try:
        sub_folder_dir = os.path.join(os.getcwd(), root_folder_name, sub_folder_name)
        if not os.path.exists(sub_folder_dir):
            os.mkdir(sub_folder_dir)
        return sub_folder_dir
    except OSError as e:
        raise Exception(f"Failed to create sub-folder directory for {sub_folder_name} : {e}")


if __name__ == "__main__":
    create_root_folder_dir(['Test 1', 'Test 2'])
    create_sub_folder_dir('Test 1', 'Sub Test 1')
