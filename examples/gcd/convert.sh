for f in *.log; do
  python ../../src/convert.py $f $f gcd 20
done
