# Music Theory Figuring

# Functions
def number_from_scale_input(scale_input):
    if scale_input.lower() == "g#" or scale_input.lower() == "ab":
        return 11
    elif scale_input.lower() == "g":
        return 10
    elif scale_input.lower() == "f#" or scale_input.lower() == "gb":
        return 9
    elif scale_input.lower() == "f":
        return 8
    elif scale_input.lower() == "e" or scale_input.lower() == "fb":
        return 7
    elif scale_input.lower() == "d#" or scale_input.lower() == "eb":
        return 6
    elif scale_input.lower() == "d":
        return 5
    elif scale_input.lower() == "c#" or scale_input.lower() == "db":
        return 4
    elif scale_input.lower() == "c" or scale_input.lower() == "b#":
        return 3
    elif scale_input.lower() == "b" or scale_input.lower() == "cb":
        return 2
    elif scale_input.lower() == "a#" or scale_input.lower() == "bb":
        return 1
    elif scale_input.lower() == "a":
        return 0
    else:
        return 0

def get_mode(mode):
    if mode == 0:
        return "Ionian"

    elif mode == 1:
        return "Dorian"

    elif mode == 2:
        return "Phrygian"

    elif mode == 3:
        return "Lydian"

    elif mode == 4:
        return "Mixolydian"

    elif mode == 5:
        return "Aeolian"

    elif mode == 6:
        return "Locrian"


# Data
musical_alphabet = ["A",  "A#", "B",  "C", "C#", "D",  "D#", "E",  "F", "F#", "G",  "G#", "A",  "A#", "B",  "C", "C#", "D",  "D#", "E",  "F", "F#", "G",  "G#"]
#           indices: 0     1     2     3    4     5     6     7     8    9     10    11 It's doubled for easy maths :)

W = 2
H = 1

# Modes and their steps
mode_dictionary = {
    "Ionian":     [W, W, H, W, W, W, H],
    "Dorian":     [W, H, W, W, W, H, W],
    "Phrygian":   [H, W, W, W, H, W, W],
    "Lydian":     [W, W, W, H, W, W, H],
    "Mixolydian": [W, W, H, W, W, H, W],
    "Aeolian":    [W, H, W, W, H, W, W],
    "Locrian":    [H, W, W, H, W, W, W],
}


scale_length = 6  # Does not wrap to root note

# Logic
for new_scale in range(12):
    # For each semitone
    root_scale = musical_alphabet[new_scale]
    scale = [root_scale]

    print(root_scale)

    # For each mode
    for mode in range(len(mode_dictionary)):
        steps = []

        # Creating the scale based on mode
        for note in range(scale_length):
            steps.append(mode_dictionary[get_mode(mode)][note])         # Add the step value onto steps
            index = (sum(steps) + number_from_scale_input(root_scale))  # Add up steps and the index of the scale as "index"

            scale.append(musical_alphabet[index])  # Add the proper note onto the scale

        # Output
        print(f"{get_mode(mode)}: {scale}")

        scale = [root_scale]  # It all goes to shit without this line

    print("\n")
