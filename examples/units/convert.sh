for f in *.log; do
  python ../../src/convert.py $f $f units 15
done
