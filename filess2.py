with open("data.txt", "r+") as file:
    lines = file.readlines()  # Read all lines into a list
    file.seek(0)  # Move cursor to the beginning
    for line in lines:
        if "Java" in line:
            file.write(line.replace("Java", "JavaScript"))
        else:
            file.write(line)
    file.truncate()  # Remove any leftover content
