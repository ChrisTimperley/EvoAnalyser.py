for f in *.log; do
  python ../../src/convert.py $f $f svr-look 12
done
