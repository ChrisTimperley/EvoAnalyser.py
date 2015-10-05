for f in *.log; do
  python ../../src/convert.py $f $f indent 15
done
