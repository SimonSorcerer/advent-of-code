import re;
from hash_utils import hash_step
from box_utils import add_to_box, remove_from_box

def parse_step(step):
    match = re.match(r'(\w+)([=-])(\d*)', step)

    return match.group(1), match.group(2), match.group(3)

def parse_sequence(line):
    steps = line.split(',')

    for step in steps:
        label, operation, focal_no = parse_step(step)
        box = hash_step(label)

        if (operation == '='):
            add_to_box(box, label, focal_no)
        else:
            remove_from_box(box, label)

def get_lens_focus(box, slot, focal_no):
    return (box + 1) * slot * focal_no

def get_focusing_power(boxes):
    result = 0

    for box in boxes:
        for slot, lens in enumerate(boxes[box], 1):
            focal_no = lens[1]
            result += get_lens_focus(box, slot, int(focal_no))

    return result