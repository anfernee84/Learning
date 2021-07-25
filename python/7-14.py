def to_indexed(start_file, end_file):
    with open (start_file, "r") as fh:
        s = fh.readlines()
        count = 0
        text = ""
        for i in s:
            i = str(count) + ": " + i
            text += i
            count += 1
    with open (end_file, "w") as fu:
        fu.write(text)
    





print(to_indexed("test.txt", "text2.txt"))
