Configuration Parser as a battery for `deepclusteringtoolbox`

# install:
```bash
pip install git+https://github.com/ETS-Research-Repositories/Config-Parser-battery.git
```
# example
```bash
# base:
echo "base config"
>>{'A': {'B': 1, 'C': True, 'E': False, 'F': [1, 2, 3], 'G': {1: 2, 3: 4}}}
echo "single variable assignment"
python demo.py A.B="A.B has been changed" A.C=False
>>{'A': {'B': 'A.B has been changed',
       'C': False,
       'E': False,
       'F': [1, 2, 3],
       'G': {1: 2, 3: 4}}}
echo "assigning a list"
python demo.py A.F="[1,2,3,4,5]"
>>{'A': {'B': 1, 'C': True, 'E': False, 'F': [1, 2, 3, 4, 5], 'G': {1: 2, 3: 4}}}
echo "assigning more complex variables"
python demo.py  trainer.lr:!seq="[{1:2},{'true':True}]" lr.yes=0.94 lr.no=False
>>{'A': {'B': 1, 'C': True, 'E': False, 'F': [1, 2, 3], 'G': {1: 2, 3: 4}},
 'lr': {'no': False, 'yes': 0.94},
 'trainer': {'lr': [{1: 2}, {'true': True}]}}
```