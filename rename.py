import os

import pathlib


def print_hi(name):
    print(f' - {name}' "   değişti")  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print("starting")

    # path = input("Path to change all files names (do not end it with the slash): ")
    path = "/home/ms/dnm/mail22/m samat"
    path = path + "/"
    rename = "VERGİ LEVHASI"
    space = " - "
    pname_last = ""

    ls = os.listdir(path)
    count = 0

    paths = (os.path.join(root, filename)
             for root, _, filenames in os.walk("/home/ms/dnm/mail22/")
             for filename in filenames)

    for path2 in paths:
        # the '#' in the example below will be replaced by the '-' in the filenames in the directory
        #print(28, path2)
        pathx = pathlib.Path(path2).parent
        name = pathlib.Path(path2).stem
        pname = pathlib.Path(pathx).stem
        if pname != pname_last:
            pname_last = pname
            count = 0
        ext = pathlib.Path(path2).suffix
        #print(31, str(count), "File Extension: ", ext, name, pathx)
        if ext == ".pdf":
            countw = " (" + str(count + 1) + ")"
            if count == 0:
                countw = ""
            before = str(pathx)+"/" + name + ext
            later = str(pathx)+"/" + rename + " - " + pname + countw + ext

            os.rename(before, later)
            print_hi(before + space + later)
        count += 1

