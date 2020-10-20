import data as dt
import copy

# Variables
musical_alphabet = dt.musical_alphabet
mode_dictionary = dt.mode_dictionary
scale_length = dt.scale_length
mode_list = dt.mode_list
mode_list_no_spaces = dt.mode_list_no_spaces
chord_types_dictionary = dt.chord_types_dictionary

# Functions


def number_from_scale_input(scale_input) -> int:
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


def conv_flat_to_sharp(input) -> str:
    if input == "Ab":
        return "G#"
    elif input == "Bb":
        return "A#"
    elif input == "Cb":
        return "B"
    elif input == "Db":
        return "C#"
    elif input == "Eb":
        return "D#"
    elif input == "Fb":
        return "E"
    elif input == "Gb":
        return "F#"
    else:
        print("Invalid input for conv_flat_to_sharp function in functions file")
        return input


def get_sharp_from_flat(inputs) -> list:
    for inp in range(len(inputs)):
        if len(inputs[inp]) > 1:
            if inputs[inp][1] == "b":
                converted_inp = conv_flat_to_sharp(inputs[inp])
                inputs[inp] = converted_inp

    return inputs


def print_all_modes_for_each_semitone() -> None:
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


def fetch_all_music_data_as_dictionary() -> dict:
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


def gather_relevant_scale_mode_data(inputs: list, musical_dict: dict) -> [list, list]:
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

def guess_chord() -> [list, list]:
    found = 0
    musical_dictionary = fetch_all_music_data_as_dictionary()
    inputs = []
    uNote = str()

    print("Input notes, type \"z\" when finished.")
    while found == 0:
        note_input = str(input(">>> "))

        if len(note_input) == 1:
            uNote = note_input.upper()

        elif len(note_input) == 2:
            uNote = note_input[0].upper()

            if note_input[1] == "#":
                uNote += "#"
            elif note_input[1].lower() == "b":
                uNote += "b"

        # uNote = note_input.upper() if len(note_input) == 1
        # flat_uNote = (str(uNote[0]) + str(uNote[1].lower())) if len(uNote) == 2 and uNote[1] == "B" else None

        inputs.append(uNote if uNote in musical_alphabet or uNote == "Z" or uNote in dt.flats else print("Invalid input"))

        inputs = get_sharp_from_flat(inputs)

        if inputs[-1] == "Z":
            return gather_relevant_scale_mode_data(inputs[:-1], musical_dictionary)


def pick_chords_from_inputs_modes(inputs, possible_modes) -> None:
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


def print_inversion_data(inversion, inputs, semitone, mode, chord_type) -> None:
    print(f"{inversion} is the first inversion of {inputs}")
    print(f"{inversion} found in {semitone} {mode} as a(n) {chord_type} chord.")


def find_possible_scales_from_scale_input(inputs, possible_modes) -> None:
    print(f"Inputs: {inputs}")
    print("Possible Modes")

    for semitone in possible_modes:
        print(semitone) if len(possible_modes[semitone]) > 0 else None  # Incompatible semitones are not printed
        for mode in possible_modes[semitone]:
            for mode_scale in possible_modes[semitone][mode]:
                print(f"{mode}: {mode_scale}")


