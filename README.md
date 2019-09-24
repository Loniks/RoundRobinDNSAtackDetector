# RoundRobinDNSAtackDetector
A simple DNS atack detector based on DecisionTree built with scikit-learn

## Quickstart

1. Install Python 3
2. Clone repo and open folder with it
3. Create virual env `pyvenv venv && activate venv/bin/activate`
4. Install dependencises `pip install -r requirements.txt`
5. Build model on provided [DNS dump](https://github.com/Loniks/RoundRobinDNSAtackDetector/blob/master/round_robin_dns_atack_detector/resources/dump.csv) by script `python main.py`
6. Verify model calling  `pytest`
7. Based on [test script](https://github.com/Loniks/RoundRobinDNSAtackDetector/blob/master/test/test_verify_model.py) use model located in *models/dns_model.pkl* with any new data

## Technologies used

- [Python](https://www.python.org/)
- [scikit-learn](https://scikit-learn.org)
- [pytest](http://pytest.org/en/latest/)

