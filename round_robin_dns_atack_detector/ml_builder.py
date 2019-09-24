import os
from sklearn import tree
import joblib
import csv

def build_model():
    features = []
    labels = []

    #fill data in futures and labels

    current_path = os.path.abspath(os.path.dirname(__file__))
    good_resource_path = os.path.join(current_path, 'resources/dump_good.csv')
    get_data(good_resource_path,features,labels)
    bad_resource_path = os.path.join(current_path, 'resources/dump_bad.csv')
    get_data(bad_resource_path,features,labels,False)

    #build classifier
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    #save model
    model_path = os.path.join(current_path, '../models/dns_model.pkl')
    joblib.dump(clf, model_path, compress=9)

def get_data(file_path,features,labels,is_ok=True):
    protocol_names = ['QUIC', 'DNS', 'ARP', 'TCP', 'UDP', 'SSDP', 'IGMPv2', 'SSL', 'TLSv1.2', 'DB-LSP-DISC','MDNS','TLSv1','BROWSER', 'ICMP']
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[5].isdigit():
                feature = [int(row[2].replace(".", "")), int(row[3].replace(".", "")), protocol_names.index(row[4])]
                features.append(feature)
                if is_ok:
                    labels.append('ok')
                else:
                    labels.append('bad')   