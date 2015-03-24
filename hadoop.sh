rm mapper.txt
rm reducer.txt

touch mapper.txt
touch reducer.txt

python A3715_mapper.py
python A3715_reducer.py

cat mapper.txt
cat reducer.txt
