import os
with open("c:/users/user/desktop/file1/1.TXT") as just:
    data = just.read()
    lines = data.split("\n")
    for line in lines:
        print(line)