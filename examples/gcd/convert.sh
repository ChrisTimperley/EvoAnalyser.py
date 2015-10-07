for f in *.log; do
  python ../../src/convert.py $f $f gcd 30
done
