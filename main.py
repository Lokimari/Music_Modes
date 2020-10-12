# Music Theory Figuring

import copy

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
flats = ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"]

W = 2
H = 1

# Modes and their steps, final step will be shown if scale_length is set to 7 below.
mode_dictionary = {
    "Ionian        ": [W, W, H, W, W, W, H],
    "Dorian        ": [W, H, W, W, W, H, W],
    "Phrygian      ": [H, W, W, W, H, W, W],
    "Lydian        ": [W, W, W, H, W, W, H],
    "Mixolydian    ": [W, W, H, W, W, H, W],
    "Aeolian       ": [W, H, W, W, H, W, W],
    "Locrian       ": [H, W, W, H, W, W, W],
    "Harmonic Major": [W, W, H, W, H, W + H, W],
    "Harmonic Minor": [W, H, W, W, H, W + H, H],
    "Melodic Major ": [W, W, H, W, H, W, W],
    "Melodic Minor ": [W, H, W, W, W, W, H],
}

mode_list_no_spaces = [
    "Ionian",
    "Dorian",
    "Phrygian",
    "Lydian",
    "Mixolydian",
    "Aeolian",
    "Locrian",
    "Harmonic Major",
    "Harmonic Minor",
    "Melodic Major",
    "Melodic Minor"
]

mode_list = list(mode_dictionary)

chord_types_dictionary = {
    "Major": [1, 3, 5],
    "Minor": [1, 2, 5],
    # "Diminished": [1, 2, 4],
    # "Augmented": [1, 3, 6],
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

            # Creating the scale basesd on mode
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
def construct_single_scale(scale_index: int, mode: int) -> list:
    steps = []
    scale = [musical_alphabet[scale_index]]

    for note in range(scale_length):
        steps.append(mode_dictionary[mode_list[mode]][note])  # Add the step value onto steps
        index = (sum(steps) + scale_index)  # Progressively add up step count

        scale.append(musical_alphabet[index])

    return scale


def mode_str_to_int_converter(mode_string: str) -> int:
    i = 0
    for mode in mode_list_no_spaces:
        if mode_string == mode:
            return i
        i += 1


def fetch_single_scale(scale_letter: str, mode: int) -> list:
    scale_index = number_from_scale_input(scale_letter)
    scale = construct_single_scale(scale_index, mode)

    return scale

def determine_chord(relevant_scale_mode_data):
    pass

def gather_relevant_scale_mode_data(inputs, musical_dict):
    # Jaccard-like scoring system
    possible_modes = dict()
    likelihood = 0

    for root in musical_dict:
        possible_modes[root] = dict()

        for mode in range(len(mode_list)):

            for note in inputs:
                for mode_notes in musical_dict[root][mode_list[mode]]:
                    for mode_note in mode_notes:
                        if note == mode_note:
                            likelihood += 1

            if likelihood == len(inputs):
                cur_mode = mode_list[mode]

                possible_modes[root][cur_mode] = musical_dict[root][cur_mode]

            likelihood = 0

    return inputs, possible_modes

    # # Printing every mode the inputs match with
    # for root in possible_modes:
    #     print(root)
    #
    #     for mode in range(len(possible_modes[root])):
    #         try:
    #             print(str(mode_list[mode]) + str(possible_modes[root][mode_list[mode]]))
    #         except KeyError:
    #             pass


def guess_chord():
    found = 0
    musical_dictionary = fetch_all_music_data_as_dictionary()
    inputs = []

    print("Input notes, type \"z\" when finished.")

    while found == 0:
        note_input = input(">>> ")
        uNote = note_input.upper()

        inputs.append(uNote if uNote in musical_alphabet or note_input.lower() == "z" or note_input in flats else print("Invalid input"))

        if inputs[-1].lower() == "z":
            return gather_relevant_scale_mode_data(inputs[:-1], musical_dictionary)

def pick_chords_from_inputs_modes(inputs, possible_modes):
    print("Possible Chords")
    print(f"Inputs: {inputs}")

    input_indices = []
    input_dict = {}

    chord_types_list = list(chord_types_dictionary)

    for semitone in possible_modes:
        for mode in possible_modes[semitone]:
            for mode_scale in possible_modes[semitone][mode]:
                for mode_note in mode_scale:
                    for note in inputs:
                        if note == mode_note:
                            input_indices.append(mode_scale.index(mode_note))
                            input_dict[note] = mode_scale.index(mode_note)

            input_dict_list = list(input_dict)

            for mode_type in chord_types_dictionary:

                plus_ones = [n + 1 for n in input_indices]
                # print(f"input_dict: {input_dict}")

                # Inversion detection logic

                if plus_ones == chord_types_dictionary[mode_type]:
                    chord_index = chord_types_list.index(mode_type)
                    inversion = [note for note in input_dict]
                    inv_copy = copy.copy(inversion)

                    if input_dict[inputs[-1]] < input_dict[inputs[0]]:
                        print("1st inversion")  # CEG -> EGC

                        for note in range(len(inversion)):
                            inversion[note] = inv_copy[note - len(inversion) + 1]

                        print_inversion_data(inversion, inputs, semitone, mode, chord_types_list[chord_index])

                    elif input_dict[inputs[1]] < input_dict[inputs[0]]:
                        print("2nd inversion")  # CEG -> GCE

                        for note in range(len(inversion)):
                            inversion[note] = inv_copy[note - 1]

                        print_inversion_data(inversion, inputs, semitone, mode, chord_types_list[chord_index])

                    else:
                        print(f"{inputs} found in {semitone} {mode} as a(n) {chord_types_list[chord_index]} chord.")

            input_indices = []

def print_inversion_data(inversion, inputs, semitone, mode, chord_type):
    print(f"{inversion} is the first inversion of {inputs}")
    print(f"{inversion} found in {semitone} {mode} as a(n) {chord_type} chord.")

def find_possible_scales_from_scale_input(inputs, possible_modes):
    print(f"Inputs: {inputs}")
    print("Possible Modes")

    for semitone in possible_modes:
        print(semitone) if len(possible_modes[semitone]) > 0 else None  # Incompatible semitones are not printed
        for mode in possible_modes[semitone]:
            for mode_scale in possible_modes[semitone][mode]:
                print(f"{mode}: {mode_scale}")


def user_menu():
    print("\n##################################################")
    print("####  Menu:                                   ####")
    print("####        1: Print all modes                ####")
    print("####        2: Fetch a single scale/mode      ####")
    print("####        3: Fetch scale(s) via input       ####")
    print("####        4: Fetch chord presence via input ####")
    print("####                                          ####")
    print("##################################################")


def main():

    while True:
        user_menu()

        menu_choice = input("\n>>> ")

        if int(menu_choice) == 1:
            print_all_modes_for_each_semitone()

        elif int(menu_choice) == 2:
            data = input("Enter a semitone and which mode you would like printed. eg. C Ionian\n>>> ")

            # Separate note from mode type
            semitone = data[0] if data[1].lower() != "b" or data[1].lower() != "#" else data[:2]
            mode = data[2:] if len(semitone) == 1 else data[3:]

            # Output
            print(f"note: {semitone}")
            print(f"mode: {mode}")

            mode_int = mode_str_to_int_converter(mode)
            print(fetch_single_scale(semitone, mode_int))

        elif int(menu_choice) == 3 or int(menu_choice) == 4:
            inputs, possible_modes = guess_chord()

            if int(menu_choice) == 3:
                find_possible_scales_from_scale_input(inputs, possible_modes)

            elif int(menu_choice) == 4:
                print("Section not fully implemented, it can only tell some Major Chords for now.")
                pick_chords_from_inputs_modes(inputs, possible_modes)  # TODO: Needs refinement

        else:
            print("Invalid input")
            pass

    # musical_dictionary = fetch_all_music_data_as_dictionary()  # All musical scale/mode data


if __name__ == "__main__":
    main()
