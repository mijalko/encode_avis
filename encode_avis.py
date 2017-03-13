import os
import subprocess

# paths are hardcoded because I import all my media in same root folder, so I don't need to enter source folder as argument when I run the screept 

encrypted_files = []
for root, dirs, files in os.walk("/Users/mijalko/slike"):
    for file in files:
        if file.lower().endswith(".avi"):
             #print(os.path.join(root, file))
            full_path = os.path.join(root, file)
            file_name_no_ext, extension = os.path.splitext(full_path)
            new_file_name = file_name_no_ext + ".mp4"

            print full_path
            print new_file_name

            encrypted_files.append(full_path)

            process = subprocess.Popen("/Applications/HandBrakeCLI -i {} -o {} --preset-import-file /Users/mijalko/handbrakedefault.json".format(full_path, new_file_name), shell=True, stdout=subprocess.PIPE)
            process.wait()

            #os.remove(full_path)

print "Encrypted files:"
for f in encrypted_files:
    print f
