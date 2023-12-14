import numpy

def rotate_matrix(matrix, clockwise=False):
    return numpy.rot90(matrix) if clockwise else numpy.rot90(matrix, k=1, axes=(1, 0))

def detect_sequence(sequence):
    start_index = 0
    loop_length = 0

    for start_index in range(len(sequence)):
        for index in range(start_index + 1, len(sequence)):
            if sequence[start_index] == sequence[index]:
                # print('found repeat at index', index, ':', sequence[index])
                loop_length = index - start_index
                current_index = start_index
                while (current_index < index):
                    if (sequence[current_index] != sequence[current_index + loop_length]):
                        loop_length = 0
                        break
                    current_index += 1
                
            if (loop_length > 1):
                break;
        if (loop_length > 1):
                break;
  
    return start_index, loop_length