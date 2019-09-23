from sklearn import tree
import joblib
import csv

features = []
labels = []

protocol_names = ['QUIC', 'DNS', 'ARP', 'TCP', 'UDP', 'SSDP', 'IGMPv2', 'SSL', 'TLSv1.2', 'DB-LSP-DISC','MDNS','TLSv1','BROWSER', 'ICMP']

with open('resources/dump_good.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[5].isdigit():
            feature = [int(row[2].replace(".", "")), int(row[3].replace(".", "")), protocol_names.index(row[4])]
            features.append(feature)
            labels.append('ok')

with open('resources/dump_bad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[5].isdigit():
            feature = [int(row[2].replace(".", "")), int(row[3].replace(".", "")), protocol_names.index(row[4])]
            features.append(feature)
            labels.append('bad')
   

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


joblib.dump(clf, '../models/dns_model.pkl', compress=9)

