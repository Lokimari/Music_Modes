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
    inp_lower = scale_input.lower()
    semitone_num_dict = {
        "g#": 11,
        "ab": 11,
        "g": 10,
        "f#": 9,
        "gb": 9,
        "f": 8,
        "e" : 7,
        "fb": 7,
        "d#": 6,
        "eb": 6,
        "d": 5,
        "c#": 4,
        "db": 4,
        "c": 3,
        "b#": 3,
        "b": 2,
        "cb": 2,
        "a#": 1,
        "bb": 1,
        "a": 0,
    }
    return semitone_num_dict[inp_lower]


def conv_flat_to_sharp(flat_inp) -> str:
    sharp_dict = {
        "Ab": "G#",
        "Bb": "A#",
        "Cb": "B" ,
        "Db": "C#",
        "Eb": "D#",
        "Fb": "E" ,
        "Gb": "F#",
    }
    return sharp_dict[flat_inp]


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

    input_indices = []  # Gets values to be used for chord_dict for chord detection weee
    input_dict = {}

    chord_types_list = list(chord_types_dictionary)

    # For each semitone
    for semitone in possible_modes:
        # For each mode(name) of that semitone
        for mode in possible_modes[semitone]:
            # For each set of notes in the mode
            for mode_scale in possible_modes[semitone][mode]:
                # For each individual note in the set
                for mode_note in mode_scale:
                    # Compare to inputs
                    for note in inputs:
                        # If equal, append int index of mode note and add mode to input_dict
                        if note == mode_note:
                            input_indices.append(mode_scale.index(mode_note))
                            input_dict[note] = mode_scale.index(mode_note)

            input_dict_list = list(input_dict)

            plus_ones = [n + 1 for n in input_indices]

            # For each set of values in the chord dict
            for mode_type in chord_types_dictionary:


                # print(f"input_dict: {input_dict}")

                # Inversion detection logic
                # Needs a simple, solid way to actually detect chords dynamically with inversions
                # Perhaps just find the possible chord (root) and then find its place in the scale
                # eg. EGC = CEG = C = 1st semitone in scale C, so it must be a Major Chord, I ii iii IV V vi vii*
                # Could work, but the inversions seem to be improperly displaying in general as of 10/22/2020 7:30pm :P

                # Might want to calculate inversions based on differences in the values of inputs_dict or something similar
                if plus_ones == chord_types_dictionary[mode_type]:
                    print(f"input_dict: {input_dict}")
                    potential_root = str()
                    for value in range(len(input_dict)):
                        if input_dict[input_dict_list[value]] == 0:
                            potential_root = input_dict_list[value]

                    print(f"Potential root note of this chord = {potential_root}")

                    chord_index = chord_types_list.index(mode_type)
                    inversion = [note for note in input_dict]
                    inv_copy = copy.copy(inversion)

                    if (input_dict[inputs[0]] > input_dict[inputs[2]]) and (input_dict[inputs[2]] > input_dict[inputs[1]]):
                        print("1st inversion")  # CEG -> EGC
                                                # 024 -> 240

                        for note in range(len(inversion)):
                            inversion[note] = inv_copy[note - len(inversion) + 1]

                        print_inversion_data(inversion, inputs, semitone, mode, chord_types_list[chord_index])

                    elif (input_dict[inputs[1]] > input_dict[inputs[0]]) and (input_dict[inputs[0]] > input_dict[inputs[2]]):
                        print("2nd inversion")  # CEG -> GCE
                                                # 024 -> 402

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


# Can just use this interval system to determine chord types dynamically
# :D
# C to E prints a 4, which is going to be used as a third
# Distance is gotten by total whole notes, so: C D E = 3
# Intervals are always ascending
# A flat is then a minor x-rd
# the 4 being printed in this test case is indicative of the quality of the interval
# the quality is a major third, since 4 semitones are passed over


def get_intervals_between_notes(notes: list) -> list:
    interval_list = [0]
    ma_index = musical_alphabet.index

    for note in range(len(notes) - 1):
        interval = ma_index(notes[note + 1]) - ma_index(notes[note])
        interval_list.append(interval)

    return interval_list


def interpret_intervals(interval_list):
    if len(interval_list) > 1:

        if len(interval_list) == 2:

            if interval_list[1] == 7:
                print("This is a perfect fifth")

        elif len(interval_list) == 3:

            if interval_list[1] == 4 and interval_list[2] == 3:
                print("This is a major triad")

            elif interval_list[1] == 3 and interval_list[2] == 4:
                print("This is a minor triad")




notes = ["B", "D#", "F#"]
print(interpret_intervals(get_intervals_between_notes(notes)))
print(get_intervals_between_notes(notes))
