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
    "Diminished": [1, 2, 4],
    "Augmented": [1, 3, 6],
    # Add more later, these are enough for testing...
}

scale_length = 6  # Does not wrap to root note
