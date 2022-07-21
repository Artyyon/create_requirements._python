@ECHO OFF
pip list > saida.txt
python create_requeriments.py saida.txt
del saida.txt
