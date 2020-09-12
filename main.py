# Music Theory Figuring
import copy

def number_from_scale_input(scale_input):
    if scale_input.lower() == "g#" or scale_input.lower() == "ab":
        return 0
    elif scale_input.lower() == "g":
        return 1
    elif scale_input.lower() == "f#" or scale_input.lower() == "gb":
        return 2
    elif scale_input.lower() == "f":
        return 3
    elif scale_input.lower() == "e" or scale_input.lower() == "fb":
        return 4
    elif scale_input.lower() == "d#" or scale_input.lower() == "eb":
        return 5
    elif scale_input.lower() == "d":
        return 6
    elif scale_input.lower() == "c#" or scale_input.lower() == "db":
        return 7
    elif scale_input.lower() == "c" or scale_input.lower() == "b#":
        return 8
    elif scale_input.lower() == "b" or scale_input.lower() == "cb":
        return 9
    elif scale_input.lower() == "a#" or scale_input.lower() == "bb":
        return 10
    elif scale_input.lower() == "a":
        return 11
    else:
        return 0


# Data

musical_alphabet = ["A",  "A#", "B",  "C", "C#", "D",  "D#", "E",  "F", "F#", "G",  "G#"]
#           indices: 0     1     2     3    4     5     6     7     8    9     10    11
reverse_alphabet = ["G#", "G",  "F#", "F", "E",  "D#", "D",  "C#", "C", "B",  "A#", "A" ]

sharp_flat = ["#", "b"]
maj_min = ["maj", "min"]

modes_list = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]

# Logic - Negatively indexed to avoid repetition

i = input("Enter a scale letter, # and b are supported, the scale and its modes will be printed.\n>>> ")
scale_string = i[0] if len(i) == 1 else i[0:2]
i_copy = i
i = number_from_scale_input(i[0:2]) if len(i) == 2 or len(i) == 4 or len(i) == 5 else number_from_scale_input(i[0])

major_steps = [i, i - 2, i - 4, i - 5, i - 7, i - 9, i - 11, i - 12]
#              0    W      W      H      W      W      W       H
minor_steps = [i, i - 2, i - 3, i - 5, i - 7, i - 8, i - 10, i - 12]
#              0    W      H      W      W      H      W       W

scale_type = major_steps if len(i_copy) in range(1, 3) or len(i_copy) == 5 and i_copy[2:] == "maj" else minor_steps

def restructure_scale_mode(mode_index, scale):
    scale_copy = copy.copy(scale)

    for n in range(len(scale)):
        scale[n] = scale_copy[(n - 7) + mode_index]

    return scale

def change_scale_mode(mode_index, scale):
    if mode_index == 0:
        return scale
    else:
        return restructure_scale_mode(mode_index, scale)


scale_modes_list = []

for mode in range(len(modes_list)):
    scale = [reverse_alphabet[scale_type[i]] for i in range(7)]
    scale_modes_list.append(f"{modes_list[mode]}: {change_scale_mode(mode, scale)}")

print("Scale: " + scale_string)
for m in scale_modes_list:
    print(m)
