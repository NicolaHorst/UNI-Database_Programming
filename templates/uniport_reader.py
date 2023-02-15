import gzip
import re
from typing import Dict
from typing import List


def uniprot_file_to_dict(file_name: str, filter_on=None) -> Dict:
    """
    Extract all information from uniprot files
    :param file_name: a file name of a uniprod file
    :param filter_on: a list of elements to be extracted ["AC", "OS", "OC", "OX", "RX", "DR"]
    :return: a dictionary containing all information requested from the uniprot files
    """
    filter_on = ["AC", "OS", "OC", "OX", "RX", "DR"] if filter_on is None else filter_on
    file_dict: Dict = {}

    # some flags
    is_binary: bool = True if file_name.endswith(".dat.gz") else False

    # store current used id
    _id = ""

    # open the file in binary or normal mode
    if is_binary:
        file = gzip.open(file_name, "rb")
    else:
        file = open(file_name, "r")

    for line in file:
        # some preprocessing for binary strings
        line = line.decode() if is_binary else line

        if re.match("^ID", line):
                _id = line.split("   ")[1]
                file_dict.update({_id: {target: [] for target in filter_on}})
        else:
            line_start = line[:2]  # take first two characters from string
            if line_start in filter_on:
                file_dict[_id][line_start].append(line[5:].strip("\n"))

    return file_dict


def extract_sequences(file_name: str) -> Dict:
    """
    extract the sequence for each uniprod ID
    :param file_name: name of the file
    :return: A dictionary with key ID value String version of sequence
    """
    file_dict: Dict = {}

    # some flags
    is_binary: bool = True if file_name.endswith(".dat.gz") else False
    is_sq: bool = False

    # current id
    id = ""

    if file_name.endswith(".dat.gz"):
        file = gzip.open(file_name, "rb")
    else:
        file = open(file_name, "r")

    for line in file:
        line = line.decode() if is_binary else line
        if line.startswith("ID"):
                id = line.split("   ")[1]
                file_dict.update({id: []})
        elif line.startswith("SQ") or is_sq:
            if line.startswith("SQ"):
                is_sq = True
                continue
            elif line.startswith("//"):
                is_sq = False
            else:
                line = line.strip()
                file_dict[id].append(line.strip("\n"))

    return file_dict


def merge_dicts(d1: Dict, d2: Dict):
    for key in d1.keys():
        d1[key].update({"SQ": d2[key]})
    return d1


def extract_from_dr(fn: str, match_on: str, split_on: str = " ") -> Dict:
    file_dict = uniprot_file_to_dict(file_name=fn, filter_on=["DR"])
    extracted_ids: Dict = {}
    for uniprot_id in file_dict.keys():
        sequences: List = []
        for go_entry in file_dict[uniprot_id]["DR"]:
            if re.search(match_on, go_entry):
                sequences.append(go_entry.split(split_on)[1])
        # add sequence to dictionary or NA if no sequence was found
        sequence = "NA" if not sequences else sequences
        extracted_ids.update({uniprot_id: sequence})

    return extracted_ids


def extract_doi(fn: str) -> Dict:
    file_dict = uniprot_file_to_dict(file_name=fn, filter_on=["RX"])
    extracted_doi: Dict = {}
    for uniprot_id in file_dict.keys():
        sequences: List = []
        for entry in file_dict[uniprot_id]["RX"]:
            # TODO add processing here
            sequences.append(entry)
        # add sequence to dictionary or NA if no sequence was found
        extracted_doi.update({uniprot_id: sequences})

    return extracted_doi


if __name__ == "__main__":
    path = r"/Users/I518095/Documents/GitHub/UNI-Database_Programming/Test_Exam_4/uniprot-corona-virus-data-2022-02.dat"
    f = extract_from_dr(fn=path, match_on="GO;")
    g = extract_from_dr(fn=path, match_on="KEGG;")
    a = uniprot_file_to_dict(file_name=path)
    i = extract_doi(fn=path)
    b = extract_sequences(file_name=path)
    c = merge_dicts(a, b)
