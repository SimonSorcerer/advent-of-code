def parse_contraption_matrix(file):
    contraption = []

    for index, line in enumerate(file):
            contraption.append([])
            for char in line.strip():
                contraption[index].append(char)
    
    return contraption