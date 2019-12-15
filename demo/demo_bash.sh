#!/usr/bin/env bash
echo "base config:"
python demo.py
echo "single variable assignment"
python demo.py A.B="A.B has been changed" A.C=False
echo "assigning a list"
python demo.py A.F="[1,2,3,4,5]"
echo "assigning more complex variables"
python demo.py  trainer.lr:!seq="[{1:2},{'true':True}]" lr.yes=0.94 lr.no=False

