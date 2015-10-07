for f in *.log; do
  python ../../src/convert.py $f $f ultrix-look 12
done
