for f in *.log; do
  python ../../src/convert.py $f $f uniq 15
done
