import os
import csv

protocol_names = ['QUIC', 'DNS', 'ARP', 'TCP', 'UDP', 'SSDP', 'IGMPv2', 'SSL', 'TLSv1.2', 'DB-LSP-DISC','MDNS','TLSv1','BROWSER', 'ICMP','HTTP','HTTP/XML']

def make_initial_data_set():
    current_path = os.path.abspath(os.path.dirname(__file__))
    # read all lines
    header,original = read_resource(current_path)

    # find number of pairs
    dictionary = find_number_of_pairs(original)

    good,bad = group_rows_by_criteria(dictionary,original)

    # save into separate files
    good_resource_path = os.path.join(current_path, 'resources/dump_good.csv')
    save_resource(good_resource_path,header,good)
    bad_resource_path = os.path.join(current_path, 'resources/dump_bad.csv')
    save_resource(bad_resource_path,header,bad)
    

def read_resource(current_path):
    resource_path = os.path.join(current_path, 'resources/dump.csv')
    with open(resource_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        original = []
        header = []
        for row in reader:
            if not row[5].isdigit():
                header = row
            else:
                original.append(row)
        return header,original

def save_resource(file_path,header,original):
    with open(file_path, 'w') as fp:
        writer = csv.writer(fp, delimiter=',', lineterminator='\n')
        writer.writerow(header)
        writer.writerows(original)

def find_number_of_pairs(original):
    dictionary = {}
    for row in original:
        key = '{}-{}'.format(row[2], row[4])
        if key not in dictionary:
            dictionary[key] = {row[3]}
        else:
            set = dictionary.get(key)
            set.add(row[3])
            dictionary[key] = set 
    return dictionary

def group_rows_by_criteria(dictionary,original):
    good = []
    bad = []
    for row in original:
        key = '{}-{}'.format(row[2], row[4])
        if len(dictionary.get(key))>1:
            bad.append(row)
        else:
            good.append(row)
    return good,bad        