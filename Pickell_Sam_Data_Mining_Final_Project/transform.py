###############################################################
#  Copyright (C) 2019 Sam Pickell
#  Last updated: December 8, 2019
#  transform.py - part of the COMP 5540 Data Mining Project
###############################################################


input_path = 'input.txt'
input_file = open(input_path, 'r')
output_path = 'output.txt'
output_file = open(output_path, 'w')

#  Get the first line of input from the input file
c = input_file.read(1)


#  Build the lists of features
toxicity = ['p', 'e']
cap_shape = ['b', 'c', 'f', 'k', 'x', 's']
cap_surface = ['f', 'g', 's', 'y']
cap_color = ['b', 'c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']
bruises = ['f', 't']
odor = ['a', 'c', 'f', 'l', 'm', 'n', 'p', 's', 'y']
gill_attachment = ['a', 'd', 'f', 'n']
gill_spacing = ['c', 'd', 'w']
gill_size = ['b', 'n']
gill_color = ['b', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']
stalk_shape = ['e', 't']
stalk_root = ['?', 'b', 'c', 'e', 'r', 'u', 'z']
stalk_surface_above_ring = ['f', 'k', 's', 'y']
stalk_surface_below_ring = ['f', 'k', 's', 'y']
stalk_color_above_ring = ['b', 'c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
stalk_color_below_ring = ['b', 'c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
veil_type = ['p', 'u']
veil_color = ['n', 'o', 'w', 'y']
ring_number = ['n', 'o', 't']
ring_type = ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z']
spore_print_color = ['b', 'h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
population = ['a', 'c', 'g', 'l', 'm', 'n', 'p', 's', 'v', 'y']
habitat = ['d', 'g', 'l', 'm', 'p', 'u', 'w']


#  Convert the input to binary
def transform(att_name, input_char):
    for i in range(len(att_name)):
        #  Determine what values to put in the edible and poisonous fields
        if att_name[i] == input_char:
            output_file.write('1')
        else:
            output_file.write('0')

        #  Eat and output commas
        output_file.write(',')

    #  Eat comma and get next character
    input_char = input_file.read(1)
    input_char = input_file.read(1)

    return


#  Convert the input to binary, specifically for the final value in a line
def transform_final_value(att_name, input_char):
    for i in range(len(att_name)):
        #  Determine what values to put in the edible and poisonous fields
        if att_name[i] == input_char:
            output_file.write('1')
        else:
            output_file.write('0')

        #  Eat and output commas, but considering this could be the last value, DON'T write a comma for the last value
        if not i == len(att_name) - 1:
            output_file.write(',')

    return


while True:

    #  Check toxicity
    transform(toxicity, c)

    #  Check cap shape
    transform(cap_shape, c)

    #  Check cap surface
    transform(cap_surface, c)

    #  Check cap color
    transform(cap_color, c)

    #  Check bruises
    transform(bruises, c)

    #  Check odor
    transform(odor, c)

    #  Check gill attachment
    transform(gill_attachment, c)

    #  Check gill spacing
    transform(gill_spacing, c)

    #  Check gill size
    transform(gill_size, c)

    #  Check gill color
    transform(gill_color, c)

    #  Check stalk shape
    transform(stalk_shape, c)

    #  Check stalk root
    transform(stalk_root, c)

    #  Check stalk surface above ring
    transform(stalk_surface_above_ring, c)

    #  Check stalk surface below ring
    transform(stalk_surface_below_ring, c)

    #  Check stalk color above ring
    transform(stalk_color_above_ring, c)

    #  Check stalk color below ring
    transform(stalk_color_below_ring, c)

    #  Check veil type
    transform(veil_type, c)

    #  Check veil color
    transform(veil_color, c)

    #  Check ring number
    transform(ring_number, c)

    #  Check ring type
    transform(ring_type, c)

    #  Check spore print color
    transform(spore_print_color, c)

    #  Check population
    transform(population, c)

    #  Check habitat
    transform_final_value(habitat, c)

    #  Get either  a newline or and eof
    c = input_file.read(1)

    #  Finished a line of input, check for eof. If not eof, insert newline and prepare for another line of input
    if not c:
        break
    else:
        output_file.write('\n')
        c = input_file.read(1)

input_file.close()
