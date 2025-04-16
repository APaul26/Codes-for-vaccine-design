## This module is used to fetch Nipah Virus peptide sequences from Uniprot database
"""
The accesion IDs for the 2 surface glycoproteins of Nipah virus are listed below:
Fusion glycoprotein (F) - Q9IH63 / FUS_NIPAV (https://www.uniprot.org/uniprotkb/Q9IH63/entry)
Attachment glycoprotein (G) - Q9IH62 / GLYCP_NIPAV (https://www.uniprot.org/uniprotkb/Q9IH62/entry)
"""
import requests
accession_ids = [
    "Q9IH63", # F_protein
    "Q9IH62", # G_protein
]
# Changing the header names to custom names for easier identification
custom_headers = [
    "F_protein",
    "G_protein",
]
# Fetchting FASTA sequences from UniProt
def fetch_fasta(acc_id):
    url = f"https://www.uniprot.org/uniprot/{acc_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch {acc_id}: Status code {response.status_code}")
        return None
# Saving the sequences to a .fasta file
output_file = "nipah_structural_prot.fasta"
# Fetchting and write sequences to file
with open(output_file, "w") as fasta_file:
    for acc_id, custom_headers in zip(accession_ids, custom_headers):
        fasta_sequence = fetch_fasta(acc_id) 
        if fasta_sequence:
            # Modify the header
            fasta_lines = fasta_sequence.split("\n")
            fasta_lines[0] = f">{custom_headers}"  # Replace the header line
            modified_sequence = "\n".join(fasta_lines)
            # Write the modified sequence to file
            fasta_file.write(modified_sequence)
print(f"FASTA sequences saved to {output_file}")