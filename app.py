import os


def get_file_extensions(parent_directory):
    file_extensions = set()

    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            file_extensions.add(file_extension.lower())

    return file_extensions


def write_extensions_to_txt(file_extensions, output_file):
    with open(output_file, "w") as file:
        for extension in sorted(file_extensions):
            file.write(extension + "\n")


parent_directory = "path name"
extensions = get_file_extensions(parent_directory)
output_file = "extensions.txt"
write_extensions_to_txt(extensions, output_file)

print(f"File extensions are written to {output_file}.")
