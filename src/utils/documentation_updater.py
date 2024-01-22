```python
import os
import re

def update_documentation_name_references(directory, old_name, new_name):
    """
    Recursively updates all references from old_name to new_name in markdown files within the given directory.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated_content = content.replace(old_name, new_name)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

def update_asset_references(directory, old_name, new_name):
    """
    Updates file names and references to assets that include the old project name.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if old_name in file:
                new_file_name = file.replace(old_name, new_name)
                os.rename(os.path.join(root, file), os.path.join(root, new_file_name))

            if file.endswith(('.png', '.svg')):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    content = f.read()

                updated_content = re.sub(old_name.encode(), new_name.encode(), content)

                with open(file_path, 'wb') as f:
                    f.write(updated_content)

if __name__ == "__main__":
    documentation_directories = ['docs']
    asset_directories = ['src/frontend/public/assets']
    old_project_name = 'Smol-Developer'
    new_project_name = 'DevFusion'

    for directory in documentation_directories:
        update_documentation_name_references(directory, old_project_name, new_project_name)

    for directory in asset_directories:
        update_asset_references(directory, old_project_name, new_project_name)
```