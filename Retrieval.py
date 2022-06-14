import csv
from write_PlantData import plants
from write_PlantData import column_headings

plant_data_filename = 'my_plant_data.csv'

with open(plant_data_filename, encoding='utf-8', newline='') as plant_data_file:
    headings = plant_data_file.readline().strip('\n')
    plant_reader = csv.reader(plant_data_file, quoting=csv.QUOTE_NONNUMERIC)
    while True:
        print("Please choose your plant (0 exits): ")
        for index, (plant_name, botanical_name, sunlight, gsw, gsf, dsw, dsf) in enumerate(plant_reader):
            print("{}: {}".format(index + 1, plant_name))

        try:
            current_choice = int(input())
        except ValueError:
            print("Please use only integers")
            continue
        if current_choice == 0:
            exit()
        elif 1 <= current_choice <= len(plants):
            current_choice_list = plants[current_choice - 1]
            print("You chose {}.".format(current_choice_list[0]))
        else:
            print("Please select a valid number from the list")
            continue

        print("To learn more about your plant, chose from the list below. \nTo learn about a different plant, "
              "enter 0 to go back to the Plant List")
        for index, headers in enumerate(column_headings):
            print("{}: {}".format(index + 1, headers))

        header_choice = int(input())
        while 1 <= header_choice <= len(column_headings):
            header_choice_list = column_headings[header_choice - 1]
            print("{}: {}".format(header_choice_list, current_choice_list[header_choice - 1]))
            header_choice = int(input())
            continue
        if header_choice == 0:
            continue
