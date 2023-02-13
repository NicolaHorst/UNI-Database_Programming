import gzip
from typing import Dict


def uniprot_file_to_dict(file_name: str, bos: str = "ID", filter_on=None) -> Dict:
    """
    Extract all information from uniprod files
    :param file_name: a file name of a uniprod file
    :param bos: information what shall be used as the key of the dictionary default is ID
    :param filter_on: a list of elements to be extracted ["AC", "OS", "OC", "OX", "RX", "DR"]
    :return: a dictionary containing all information requested from the uniprod files
    """
    filter_on = ["AC", "OS", "OC", "OX", "RX", "DR"] if filter_on is None else filter_on
    file_dict: Dict = {}

    is_first: bool = True
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
            if is_first:
                id = line.split("   ")[1]
                is_first = False
            else:
                file_dict.update({id: content})
                content = {}
                id = line.split("   ")[1]
                filter_id = ""
        else:
            line_start: str = line[:2]
            if line_start in filter_on:
                if line_start == filter_id:
                    content[line_start].append(line[5:].strip("\n"))
                else:
                    filter_id = line_start
                    content.update({line_start: [line[5:].strip("\n")]})

    file_dict.update({id: content})

    return file_dict


def extract_sequences(file_name: str) -> Dict:
    """
    extract the sequence for each uniprod ID
    :param file_name: name of the file
    :return: A dictionary with key ID value String version of sequence
    """
    file_dict: Dict = {}

    is_first: bool = True
    is_binary: bool = False
    is_sq: bool = False

    id: str = ""
    seq: str = ""

    if file_name.endswith(".dat.gz"):
        file = gzip.open(file_name, "rb")
        is_binary = True
    else:
        file = open(file_name, "r")

    for line in file:
        line = line.decode() if is_binary else line
        if line.startswith("ID") or line.startswith("SQ"):
            if line.startswith("ID"):
                if is_first:
                    is_first = False
                    id = line.split("   ")[1]
                else:
                    file_dict.update({id: seq[:-1]})
                    seq = ""
                    id = line.split("   ")[1]
            else:
                is_sq = True
        elif is_sq:
            if line.startswith("     "):
                seq += line[5:].strip("\n") + " "
            else:
                is_sq = False

    file_dict.update({id: seq[:-1]})

    return file_dict


def merge_dicts(d1: Dict, d2: Dict):
    for key in d1.keys():
        d1[key].update({"SQ": d2[key]})
    return d1


if __name__ == "__main__":
    path = "/Users/I518095/Documents/GitHub/UNI-Database_Programming/Test_Exam_4/uniprot-corona-virus-data-2022-02_short.dat"
    a = uniprot_file_to_dict(file_name=path)
    b = extract_sequences(file_name=path)
    c = merge_dicts(a, b)
