Music Theory Figuring Program
10/20/2020
by Noah Beebe

##################################################################################################################################################################################
Run main.py

main() is run
user_menu()

Input prompt:
    - 1 -> All semitones printed
        - functions.py: print_all_modes_for_each_semitone()
        - Builds scales based on step logic, closed function that borrows from data.py

    - 2 -> Prompted for semitone:mode
        - Logic for input separation
	- Input string converted to int for list indexing
        - functions.py: mode_str_to_int_converter(mode_string: str) -> int
        - functions.py: fetch_single_scale(scale_letter: str, mode: int) -> list
		- functions.py: number_from_scale_input(scale_letter)  # should be renamed get_note_index
		- functions.py: construct_single_scale(scale_index, mode)
			- Similar to print_all_modes_for_each_semitone() logic, perhaps both could be slightly simplified?

    - 3 -> functions.py: guess_chord()
	- Gets inputs, appends # or b as appropriate, ending when "Z" is inputted
	- functions.py: get_sharp_from_flat(inputs) -> list, any flats are converted to sharps for processing sake, need to support both in future
	- functions.py: gather_relevant_scale_mode_data(inputs[:-1], musical_dictionary)  # perhaps the dictionary pass here is unnecessary?
		- Uses scoring system to guess scale, returns scales that match notes for note in len(inputs)

    - 4 -> functions.py: pick_chords_from_inputs_modes(inputs, possible_modes) -> None
	- Compare inputs to possible modes  # could probably make this a standalone and attempt to pick out any chord from any mode
	- Appends input index if match, adds to seemingly unused (at least pragmatically, or to any realistic means) inputs dictionary
	- Outputs inversions, if any, via functions.py: print_inversion_data(inversion, inputs, semitone, mode, chord_types_list[chord_index]) -> None  # print

    - 5 -> Exit

##################################################################################################################################################################################
