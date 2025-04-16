## This module is used to count the frequency of each epitopes predicted
from collections import Counter
# Input and output file paths
input_file_1 = "F_pro_CTL.txt"
input_file_2 = "G_pro_CTL.txt"
output_file_1 = "F_pro_epitope_counts.txt"
output_file_2 = "G_pro_epitope_counts.txt"
"""
For F protein epitopes:
"""
# Reading epitopes from the input_file_1
with open(input_file_1, "r") as file:
    epitopes = file.read().splitlines()
# Counting the frequency of each epitope
epitope_counts = Counter(epitopes)
# Saving the results to a new file
with open(output_file_1, "w") as file:
    for epitope, count in epitope_counts.items():
        file.write(f"{epitope}: {count}\n")
print(f"Epitope counts have been written to {output_file_1}")
"""
For G protein epitopes:
"""
# Reading epitopes from the input_file_1
with open(input_file_2, "r") as file:
    epitopes = file.read().splitlines()
# Counting the frequency of each epitope
epitope_counts = Counter(epitopes)
# Saving the results to a new file
with open(output_file_2, "w") as file:
    for epitope, count in epitope_counts.items():
        file.write(f"{epitope}: {count}\n")
print(f"Epitope counts have been written to {output_file_2}")