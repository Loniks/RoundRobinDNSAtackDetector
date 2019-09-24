import os
import csv
import joblib

protocol_names = [
    'QUIC', 'DNS', 'ARP', 'TCP', 'UDP', 'SSDP', 'IGMPv2', 'SSL',
    'TLSv1.2', 'DB-LSP-DISC', 'MDNS', 'TLSv1', 'BROWSER', 'ICMP',
    'HTTP', 'HTTP/XML'
    ]


def test_verify_model():
    # arrange test by loading model
    current_path = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(current_path, '../models/dns_model.pkl')
    clf = joblib.load(model_path)
    # act test by analysing file
    count = 0
    resource_path = os.path.join(current_path, 'resources/test.csv')
    with open(resource_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[5].isdigit():
                feature = [
                    int(row[2].replace(".", "")), int(row[3].replace(".", "")),
                    protocol_names.index(row[4])
                    ]
                if clf.predict([feature]) == 'bad':
                    count += 1
    # assert count of detected issues
    assert count == 3544
