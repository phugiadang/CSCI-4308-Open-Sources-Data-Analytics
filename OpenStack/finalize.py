#last = open("finalNumbers.md", "w+")

#last = open("finalNumbers.md", 'w+')

pos_dict = {1 : "First", 2 : "Second", 3 : "Third", 4 : "Fourth", 5 : "Fifth", 6: "Sixth"}

with open("sortedNumbers.md", "r+") as number_file:
    line_number = 0
    for line in number_file:
        if (line_number != 0 and line_number < len(pos_dict)):
            new_line = line.replace("\#","")
            new_line = "#"+pos_dict[line_number] + " Place: " + line
            last.write(new_line)
        line_number += 1	 
