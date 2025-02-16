echo "BUILD START"
python 3.12.8 pip install -r requirements.txt
python 3.12.8 manage.py collectstatic --noinput --clear
echo "BUILD END"