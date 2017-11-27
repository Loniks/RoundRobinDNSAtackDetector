from sklearn import tree
from sklearn.externals import joblib
import csv

features = []
labels = []

protocol_names = ['QUIC', 'DNS', 'ARP', 'TCP', 'UDP', 'SSDP', 'IGMPv2', 'SSL', 'TLSv1.2', 'DB-LSP-DISC','MDNS','TLSv1','BROWSER', 'ICMP']

with open('dump_good.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[5].isdigit():
            feature = [int(row[2].replace(".", "")), int(row[3].replace(".", "")), protocol_names.index(row[4])]
            features.append(feature)
            labels.append('ok')

with open('dump_bad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[5].isdigit():
            feature = [int(row[2].replace(".", "")), int(row[3].replace(".", "")), protocol_names.index(row[4])]
            features.append(feature)
            labels.append('bad')
   

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

with open('test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[5].isdigit():
            feature = [int(row[2].replace(".", "")), int(row[3].replace(".", "")), protocol_names.index(row[4])]

            if clf.predict([feature])=='bad':
                print('Warning! you hava a DNS attack')
                print(row)
            

joblib.dump(clf, 'dns_model.pkl', compress=9)

