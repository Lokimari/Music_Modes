# Music Theory Figuring

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


# Data
musical_alphabet = ["A",  "A#", "B",  "C", "C#", "D",  "D#", "E",  "F", "F#", "G", "G#",
                    "A",  "A#", "B",  "C", "C#", "D",  "D#", "E",  "F", "F#", "G", "G#"]
#           indices: 0     1     2     3    4     5     6     7     8    9     10   11

W = 2
H = 1

# Modes and their steps, final step will be shown if scale_length is set to 7 below.
mode_dictionary = {
    "Ionian        ":[W, W, H, W, W, W, H],
    "Dorian        ":[W, H, W, W, W, H, W],
    "Phrygian      ":[H, W, W, W, H, W, W],
    "Lydian        ":[W, W, W, H, W, W, H],
    "Mixolydian    ":[W, W, H, W, W, H, W],
    "Aeolian       ":[W, H, W, W, H, W, W],
    "Locrian       ":[H, W, W, H, W, W, W],
    "Harmonic Major":[W, W, H, W, H, W + H, W],
    "Harmonic Minor":[W, H, W, W, H, W + H, H],
    "Melodic Major ":[W, W, H, W, H, W, W],
    "Melodic Minor ":[W, H, W, W, W, W, H],
}

mode_list = list(mode_dictionary)

chord_types_dictionary = {
    "Major": [1, 3, 5],
    "Minor": [1, 2, 5],
    "Diminished": [1, 2, 4],
    "Augmented": [1, 3, 6],
    # Add more later, these are enough for testing...
}

scale_length = 6  # Does not wrap to root note


def print_all_modes_for_each_semitone():
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
                step_value = mode_dictionary[mode_list[mode]][note]
                root_value = number_from_scale_input(root_scale)

                steps.append(step_value)           # Add the step value onto steps
                index = (sum(steps) + root_value)  # Progressively add up step count

                scale.append(musical_alphabet[index])  # Add the proper note onto the scale

            # Output
            print(f"{mode_list[mode]}: {scale}")

            scale = [root_scale]  # Reinitialize

        print("\n")


def fetch_all_music_data_as_dictionary():
    musical_dictionary = dict()

    # Logic
    for new_scale in range(12):
        # For each semitone
        root_scale = musical_alphabet[new_scale]
        scale = [root_scale]

        # Create an entry for the Root's modes
        musical_dictionary[root_scale] = dict()

        # For each mode
        for mode in range(len(mode_dictionary)):
            steps = []

            # Creating the scale based on mode
            for note in range(scale_length):
                step_value = mode_dictionary[mode_list[mode]][note]
                root_value = number_from_scale_input(root_scale)

                steps.append(step_value)           # Add the step value onto steps
                index = (root_value + sum(steps))  # Progressively add up step count, + root_value as a base

                scale.append(musical_alphabet[index])  # Add the proper note onto the scale

            # Add mode onto root's value
            musical_dictionary[root_scale][mode_list[mode]] = [scale]

            scale = [root_scale]  # Reinitialize

    return musical_dictionary


# For just getting a single scale
def construct_single_scale(scale_index, mode):
    steps = []
    scale = [musical_alphabet[scale_index]]

    for note in range(scale_length):
        steps.append(mode_dictionary[mode_list[mode]][note])  # Add the step value onto steps
        index = (sum(steps) + scale_index)  # Progressively add up step count

        scale.append(musical_alphabet[index])

    return scale


def fetch_single_scale(scale_letter, mode):
    scale_index = number_from_scale_input(scale_letter)
    scale = construct_single_scale(scale_index, mode)

    return scale


def determine_chord(inputs, musical_dict):
    #  Jaccard-like scoring system
    possible_modes = ""
    likelihood = 0

    for root in musical_dict:
        possible_modes[root] = dict()

        for mode in range(len(mode_list)):

            for note in inputs:
                for i in musical_dict[root][mode_list[mode]]:
                    for mode_note in i:
                        if note == mode_note:
                            likelihood += 1

            if likelihood == len(inputs):
                cur_mode = mode_list[mode]

                possible_modes[root][cur_mode] = musical_dict[root][cur_mode]

            likelihood = 0

    possible_modes_list = list(possible_modes)

    # Printing every mode the inputs match with
    for root in possible_modes:
        print(root)

        for mode in range(len(possible_modes[root])):
            try:
                print(str(mode_list[mode]) + str(possible_modes[root][mode_list[mode]]))
            except KeyError:
                pass


def guess_chord():
    found = 0
    musical_dictionary = fetch_all_music_data_as_dictionary()
    inputs = set()

    while found == 0:
        note_input = input(">>> ")
        inputs.add(note_input.upper() if note_input.upper() in musical_alphabet else print("Invalid input"))

        if len(inputs) > 1:
            determine_chord(inputs, musical_dictionary)


def main():
    print("Chord Guesser")
    # print_all_modes_for_each_semitone()
    # print(fetch_single_scale("C", 0))
    # musical_dictionary = fetch_all_music_data_as_dictionary()
    guess_chord()


if __name__ == "__main__":
    main()
