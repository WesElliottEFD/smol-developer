import os
import fnmatch

def update_file_content(file_path, old_name, new_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace(old_name, new_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def update_file_name(file_path, old_name, new_name):
    dir_name, file_name = os.path.split(file_path)
    new_file_name = file_name.replace(old_name, new_name)
    new_file_path = os.path.join(dir_name, new_file_name)
    os.rename(file_path, new_file_path)

def update_name_references(directory, old_name='Smol-Developer', new_name='DevFusion'):
    for root, dirs, files in os.walk(directory):
        # Update content in files
        for filename in fnmatch.filter(files, '*.*'):
            file_path = os.path.join(root, filename)
            update_file_content(file_path, old_name, new_name)

        # Update filenames
        for filename in fnmatch.filter(files, '*{}*.*'.format(old_name)):
            file_path = os.path.join(root, filename)
            update_file_name(file_path, old_name, new_name)

        # Update directory names
        for dirname in fnmatch.filter(dirs, '*{}*'.format(old_name)):
            dir_path = os.path.join(root, dirname)
            new_dir_path = dir_path.replace(old_name, new_name)
            os.rename(dir_path, new_dir_path)

# Example usage:
# update_name_references('src/', 'Smol-Developer', 'DevFusion')