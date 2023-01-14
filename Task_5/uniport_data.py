import gzip
import re

data_path = "/Users/I518095/Library/CloudStorage/OneDrive-Personal/UNI Potsdam/Lectures/Databases and Programming/programming-tasks/data/uniprot_sprot_fungi.dat.gz"

with gzip.open(filename=data_path, mode="rb") as file_reader:
    rx_counter = 0
    for line in file_reader:
        if line.startswith(b"ID") or line.startswith(b"RX"):
            _i = line.split(b"   ")[1]
            if line.startswith(b"ID"):
                print(f"{_i.decode() : <15}{rx_counter}")
                old_id = _i
                rx_counter = 0
            else:
                rx_counter +=1

