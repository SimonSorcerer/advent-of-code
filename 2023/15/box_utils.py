boxes = {}

def get_lens_index(box, label):
    if (box not in boxes):
        boxes[box] = []
        
    for index, lens in enumerate(boxes[box]):
        lens_label = lens[0]
        if lens_label == label:
            return index
    return -1

def add_to_box(box, label, focal_no):
    lens_index = get_lens_index(box, label)
    if (lens_index >= 0):
        boxes[box][lens_index] = (label, focal_no)
    else:
        boxes[box].append((label, focal_no))

def remove_from_box(box, label):
    lens_index = get_lens_index(box, label)
    if (lens_index >= 0):
        boxes[box].pop(lens_index)

def visualize():
    for box in boxes:
        print('Box ', box, ':', end='')
        for lens in boxes[box]:
            print('[', lens[0], lens[1], ']', end='')
        print('\n')

def get_boxes():
    return boxes