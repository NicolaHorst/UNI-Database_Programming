import gzip
from typing import Dict


def uniprot_file_to_dict(file_name: str, bos: str = "ID", filter_on=None) -> Dict:
    filter_on = ["SQ", "AC", "OS", "OC", "OX", "RX"] if filter_on is None else filter_on
    file_dict: Dict = {}

    is_first: bool = True
    is_seq: bool = False
    id: str = ""
    filter_id: str = ""
    content: Dict = {}
    is_binary: bool = False

    if file_name.endswith(".dat.gz"):
        file = gzip.open(file_name, "rb")
        is_binary = True
    else:
        file = open(file_name, "r")

    for line in file:
        line = line.decode() if is_binary else line
        if line.startswith(bos):
            id = line.split("   ")[1]
            if is_first:
                is_first = False
            else:
                file_dict.update({id: content})
                content = {}
                filter_id = ""
                is_seq = False
        else:
            line_start: str = line[:2]

            is_seq = True if line_start == "SQ" else is_seq
            is_seq = False if line_start == "//" else is_seq

            line_start = "SQ" if is_seq else line_start

            if line_start in filter_on or is_seq:
                if line_start == filter_id:
                    content[line_start].append(line[5:].strip("\n"))
                else:
                    filter_id = line_start
                    content.update({line_start: [line[5:].strip("\n")]})

    return file_dict


if __name__ == "__main__":
    path = "../Sample_Files/uniprot_sprot_viruses.dat"
    path2 = "../Sample_Files/uniprot_sprot_fungi.dat.gz"

    uniprot_file_to_dict(file_name=path2)
