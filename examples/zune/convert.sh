for f in *.log; do
  python ../../src/convert.py $f $f zune 54
done
