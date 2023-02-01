from typing import Dict


def fasta_file_to_dict(file_name: str) -> Dict:
    """
    Header Line = >sp|P0C6X7|R1AB_CVHSA Replicase polyprotein 1ab OS=Human SARS coronavirus OX=694009 GN=rep PE=1 SV=1
    for each header line, the following n lines contain the Amino Acid Sequence
    :param file_name: File Name
    :return: A dictionary with key=id and value=Amino Acid ID
    e.g. key=|P0C6X7|R1AB_CVHSA valu=AMTECHDSGKJEW...
    """
    file_dict = {}
    is_first: bool = True
    key: str = ""
    seq: str = ""
    with open(file_name, "r") as reader:
        for line in reader:
            if line.startswith(">sp"):
                if is_first:
                    key = line.split(" ")[0][1:]
                    is_first = False
                else:
                    file_dict.update({key: seq})
                    key = line.split(" ")[0][1:]
                    seq = ""
            else:
                seq += line.strip('\n')

        # to also catch tha last entry
        file_dict.update({key: seq})

    return file_dict
