import csv

plants = [
    ["Snake Plant I", "Dracaena trifasciata 'Laurenti'", "Indirect", 14, 30, 14, 0],
    ["Snake Plant II", "Sansevieria trifasciata", "Indirect", 14, 30, 14, 0],
    ["Aloe Vera", "Aloe barbadensis miller", "Indirect", 14, 0, 365, 0],
    ["Flapjack", "Kalanchoe luciae", "Indirect", 14, 0, 60, 0],
    ["Green Pothos", "Epipremnum aureum", "Indirect", 7, 14, 60, 0],
    ["Crown of Thorns", "Euphorbia milii", "Direct", 14, 30, 14, 0],
    ["Peace Lilly", "Zamioculcas zamiifolia", "Indirect", 7, 14, 7, 0],
    ["Zanzibar Gem", "Zamioculcas zamiifolia", "Indirect", 14, 14, 365, 0],
    ["Banana Tree", "Musa spp", "Direct", 7, 14, 7, 0],
    ["Fiddle Leaf Fig", "Ficus lyrata", "Indirect", 7, 14, 7, 0],
    ["Aluminum Plant", "Pilea cadierei", "Indirect", 7, 14, 30, 0],
    ["Orchid", "Orchidaceae", "Indirect", 7, 30, 7, 0],
    ["Easter Cactus", "Rhipsalideae gaertneri", "Indirect", 7, 14, 30, 0],
    ["Jade", "Crassula ovata", "Indirect", 7, 30, 7, 0],
    ["Fishbone Cactus", "Disocactus anguliger", "Indirect", 14, 14, 14, 0],
    ["Prickly Pear Cactus", "Opuntia spp", "Direct", 21, 30, 21, 0],
    ["Hen and Chick", "Sempervivum tectorum", "Direct", 14, 30, 0, 0],
    ["Chinese Money", "Pilea peperomiodes", "Indirect", 7, 14, 30, 0],
    ["Poneytail Palm", "Beaucarnea recurvata", "Indirect", 7, 30, 7, 0],
]

column_headings = ["Plant Name", "Botanical Name", "Sunlight", "Growing Season Water", "Growing Season Fertilizer",
                   "Dormant Season Water", "Dormant Season Fertilizer"]

output_filename = 'my_plant_data.csv'

with open(output_filename, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(column_headings)
    writer.writerows(plants)