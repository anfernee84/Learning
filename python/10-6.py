import shutil


def create_archive(path, file_name, employee_residence):
    file_path = f"{path}/{file_name}"
    with open(file_path, 'wb') as f:
        for i, j in employee_residence.items():
            s = i + ' ' + j + '\n'
            f.write(s.encode('utf-8'))
    archive_name = shutil.make_archive('backup', 'zip', path)
    return(archive_name)

print((create_archive('.', "test.txt", {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'})))


