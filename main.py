import os
from math import ceil

from pypdf import PdfReader, PdfWriter

print("**********************> Simple PDF splitter(if you know what you're doing it's simple) :) "
      "<**********************\n")
file_name_input = input("Hello poor soul! Make sure you have your files scanned. Now give me the file name or the "
                        "path to it: ")
print("Brr..robot magic")

try:
    reader = PdfReader(file_name_input)
except FileNotFoundError:
    print("Peasant! No such file exists. Make sure you either provide the full path or put the file in the current "
          "directory. Include the extension. Now start me again.. ")
    exit(0)

pages_count = len(reader.pages)
print("Brr.. file is found. At least you know the file name, that's an achievement.")
split_option = int(input(f"The input is exactly {pages_count} pages, so tell me how many pages "
                         "should be each new file: "))
optionChosen = input("Now tell me poor soul, do you want to use numbers for the file names"
                     "(the other option is custom) ? (Y/N)")

file_names = []
folder_names = []
folders_chosen = False
same_name_for_files = ""
actual_range = ceil((pages_count / split_option))
if optionChosen.lower() == "y":
    for x in range(0, actual_range):
        file_names.append(str(x) + ".pdf")
else:
    folder_or_file = input("As you misery requested the custom method, now I'll have to ask if you want them "
                           "sorted into folders or not(Y/N)")
    if folder_or_file.lower() == "y":
        folders_chosen = True
        match_file_name_or_not = input("\nYou really are a pretty lazy person. Fine. "
                                       "Should the file names match those of the folder ?\n"
                                       "Otherwise you will type a name for all the files without the extension"
                                         " (Y/the file name of choice): ")
        if match_file_name_or_not.lower() != "y":
            same_name_for_files = match_file_name_or_not

    if not same_name_for_files and not folders_chosen:
        print("Now you'll provide me the file names in order without the .pdf extension. Go peasant!")
        for x in range(0, actual_range):
            page_name = input(f"File {x} name: ")
            file_names.append(page_name + ".pdf")
    elif same_name_for_files and folders_chosen:
        print("Now you'll provide me the folder names in order. Go peasant!")
        for x in range(0, actual_range):
            file_names.append(same_name_for_files + ".pdf")
            folder_name = input(f"Folder {x} name: ")
            folder_names.append(folder_name)
    elif folders_chosen and not same_name_for_files:
        print("Now you'll provide me the folder and file names in order without the .pdf extension. Go peasant!")
        for x in range(0, actual_range):
            file_names.append(same_name_for_files + ".pdf")
            folder_name = input(f"Folder {x} name: ")
            file_name = input(f"File {x} name: ")
            folder_names.append(folder_name)
            file_names.append(file_name + ".pdf")


print("Okay, now I'm gonna do the dirty work, because you're too incompetent and lazy to do it yourself.")


pages_arr = [*reader.pages]
for file_name in file_names:
    file_writer = PdfWriter()
    folder_name = ""

    for number in range(0, split_option):
        try:
            curr_page = pages_arr.pop(0)
            file_writer.add_page(curr_page)
        except IndexError:
            break

    if folders_chosen:
        try:
            folder_name = folder_names.pop(0)
        except IndexError:
            break
        os.mkdir(folder_name)
        folder_name += "/"

    with open(folder_name + file_name, "wb") as fp:
        file_writer.write(fp)
        print(f"File {file_name} written.")

print("Job done! Tools like me are the reason why your salary keeps going down ;)")
