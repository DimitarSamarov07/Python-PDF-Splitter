from math import ceil

from pypdf import PdfReader, PdfWriter

print("Simple PDF splitter(if you know what you're doing it's simple) :)")
file_name_input = input("Hello poor soul! Make sure you have your files scanned. Now give me the file name or the path to it: ")
print("Brr..robot magic")

try:
    reader = PdfReader(file_name_input)
except FileNotFoundError:
    print("Peasant! No such file exists. Make sure you either provide the full path or the file is in the current directory."+
          "Now start me again.. ")
    exit(0)

pages_count = len(reader.pages)
print("Brr.. file is found. At least you know the file name, that's an achievement.")
split_option = int(input(f"The input is exactly {pages_count} pages, so tell me how many pages should be each new file: "))
optionChosen = input("Now tell me poor soul, do you want to use numbers for the file names(the other option is custom) ? (Y/N)")

file_names = []
actual_range = ceil((pages_count / split_option))
if optionChosen.lower() == "Y":
    for x in range(0, actual_range):
        file_names.append(str(x) + ".pdf")
else:
    print("Now you'll provide me the file names in order without the .pdf extension. Go peasant!")
    for x in range(0, actual_range):
        page_name = input(f"File {x} name: ")
        file_names.append(page_name + ".pdf")

print("Okay, now I'm gonna do the dirty work, because you're too incompetent and lazy to do it yourself.")


pages_arr = [*reader.pages]
for file_name in file_names:
    file_writer = PdfWriter()

    for number in range(0, split_option):
        try:
            curr_page = pages_arr.pop(0)
            file_writer.add_page(curr_page)
        except IndexError:
            break

    with open(file_name, "wb") as fp:
        file_writer.write(fp)
        print(f"File {file_name} written.")
