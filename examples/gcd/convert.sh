for f in *.log; do
  python ../../src/convert.py $f $f gcd
done
