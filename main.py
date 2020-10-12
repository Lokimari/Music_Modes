# Music Theory Figuring - just a fun project

import functions as mt

def user_menu():
    print("\n##################################################")
    print("####  Menu:                                   ####")
    print("####        1: Print all modes                ####")
    print("####        2: Fetch a single scale/mode      ####")
    print("####        3: Fetch scale(s) via input       ####")
    print("####        4: Fetch chord presence via input ####")
    print("####        5: Exit                           ####")
    print("####                                          ####")
    print("##################################################")


def main():

    while True:
        user_menu()

        menu_choice = input("\n>>> ")

        if int(menu_choice) == 1:
            mt.print_all_modes_for_each_semitone()

        elif int(menu_choice) == 2:
            data = input("Enter a semitone and which mode you would like printed. eg. C Ionian\n>>> ")

            # Separate note from mode type
            semitone = data[0] if data[1].lower() == " " else data[0:2]
            mode = data[2:] if len(semitone) == 1 else data[3:]

            # Output
            print(f"note: {semitone}")
            print(f"mode: {mode}")

            mode_int = mt.mode_str_to_int_converter(mode)
            print(mt.fetch_single_scale(semitone, mode_int))

        elif int(menu_choice) == 3 or int(menu_choice) == 4:
            inputs, possible_modes = mt.guess_chord()

            if int(menu_choice) == 3:
                mt.find_possible_scales_from_scale_input(inputs, possible_modes)

            elif int(menu_choice) == 4:
                print("Section not fully implemented, it can only tell some Major Chords for now.")
                mt.pick_chords_from_inputs_modes(inputs, possible_modes)  # TODO: Needs refinement

        elif int(menu_choice) == 5:
            print("Exiting")
            exit()

        else:
            print("Invalid input")
            pass

    # musical_dictionary = fetch_all_music_data_as_dictionary()  # All musical scale/mode data


if __name__ == "__main__":
    main()
