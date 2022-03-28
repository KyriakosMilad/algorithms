import os

# if you want to create the new directories in same directory holding the files
# enter the directory that holds the files in both directory input and new_directory input

directory = input("Enter directory contains the files: ")
new_directory = input("Enter directory which you want to create the new directories in: ")

for filename in os.listdir(directory):
	file_name_without_extension = filename.split(".")[:-1][0]

	if directory[-1] != "/":
		directory = directory + "/"
	if new_directory[-1] != "/":
		new_directory = new_directory + "/"

	path = os.path.join(new_directory, file_name_without_extension)
	os.mkdir(path)
	print("Directory " + path + " created")

	os.rename(directory + filename, path + "/" + filename)
	print("File " + filename + " moved from " + directory + filename + " to " + path + filename)