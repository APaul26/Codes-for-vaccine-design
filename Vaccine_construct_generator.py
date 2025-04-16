## This module is used to generate vaccine constructs using the predicted epitopes
"""
The vaccine constructx have been designed using the following components:
1. A Cholera B Toxin (CTB) adjuvant has been used at the beginning of each of the vaccine constructs.
2. The CTB adjuvant is linked to the first epitope using a EAAAK linker.
3. The CTL and HTL epitopes are randomly distributed in the linear vaccine construct.
4. Each epitope is joined by a GPGPG linker.
5. Each of the constructs generated will be later checked for overall antigenicity, immunogenicity and allergenicity
6. A total of 20 vaccine constructs will be generated.
"""
import random
from openpyxl import Workbook
# Adjuvant (CTB toxin)
adjuvant = "MTPQNITDLCAEYHNTQIHTLNDKIFSYTESLAGKREMAIITFKNGATFQVEVPGSQHIDSQKKAIERMKDTLRIAYLTEAKVEKLCVWNNKTPHAIAAISMAN"
# Predicted CTL and HTL Epitopes
epitopes = {
    "CTL_F": ["QITAGVALY", "FILVRNTLI", "YLSDLLFVF"],
    "CTL_G": ["AMDEGYFAY", "FLIDRINWI", "YFPAVGFLV"],
    "HTL_F": ["GVAIGIATAAQITAG", "NSEWISIVPNFILVR", "FISFIIVEKKRNTYS"],
    "HTL_G": ["DTLYFPAVGFLVRTE", "KVVFIEISDQRLSIG", "NDAFLIDRINWISAG"]
}
# Linker sequence
linker = "GPGPG"
# Function to generate random vaccine variants
def generate_random_constructs(epitopes, adjuvant, linker, num_variants = 50):
    # Epitopes into a single list
    all_epitopes = [epitope for category in epitopes.values() for epitope in category]
    vaccine_constructs = []
    # Generating the desired number of random variants
    while len(vaccine_constructs) < num_variants:
        random.shuffle(all_epitopes) # Shuffling the epitopes randomly
        combined_epitopes = linker.join(all_epitopes) # Joining with linker
        vaccine_sequence = f"{adjuvant}EAAAK{combined_epitopes}" # Adding the adjuvant at the start
        vaccine_constructs.append(vaccine_sequence)
    return vaccine_constructs
# Generating 50 random vaccine variants
random_variants = generate_random_constructs(epitopes, adjuvant, linker, num_variants = 50)
# Saving the generated vaccine variants to a file
output_file = "random_vaccine_constructs.xlsx"
workbook = Workbook()
sheet = workbook.active
sheet.title = "Vaccine Constructs"
sheet.append(["Construct Number", "Vaccine sequence"])
# Populate the sheet with constructs
for i, variant in enumerate(random_variants, 1):
    sheet.append([i, variant])
workbook.save(output_file)
print(f"Generated 50 random vaccine constructs. Results saved to {output_file}")