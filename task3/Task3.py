import json
import sys

def main():
    with open(sys.argv[1], 'r') as f:
        tests = json.load(f)

    with open(sys.argv[2], 'r') as f:
        values = json.load(f)['values']  

    values_dict = {v['id']: v['value'] for v in values}

    for test in tests['tests']:
        fill_values(test, values_dict)

    with open(sys.argv[3], 'w') as f:
        json.dump(tests, f, indent=2)

def fill_values(test, values_dict):
    if 'id' in test:
        test['value'] = values_dict.get(test['id'])

    if 'tests' in test:
        for subtest in test['tests']:
            fill_values(subtest, values_dict)

    if 'values' in test:
        for subtest in test['values']:
            fill_values(subtest, values_dict)

main()