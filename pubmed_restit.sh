#! /bin/bash
mkdir tempdir
mkdir tempdir/data

# Copier fichiers à tempdir
cp -r data/* tempdir/data/.
cp pubmed_restitution.py tempdir/.
cp components.py tempdir/
cp processing_fct.py tempdir/
cp main.py tempdir/

# Création du fichier Dockerfile
echo "FROM python" > tempdir/Dockerfile	
echo "RUN pip3 install pandas" >> tempdir/Dockerfile
echo "RUN pip3 install json" >> tempdir/Dockerfile
echo "RUN pip3 install re" >> tempdir/Dockerfile
echo "RUN pip3 install sys" >> tempdir/Dockerfile
echo "COPY  pubmed_restitution.py /home/med_project/" >> tempdir/Dockerfile
echo "COPY  components.py /home/med_project/" >> tempdir/Dockerfile
echo "COPY  processing_fct.py /home/med_project/" >> tempdir/Dockerfile
echo "COPY  main.py /home/med_project/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/med_project/pubmed_restitution.py" >> tempdir/Dockerfile

# Lancement du build de l'image pubmed_restit à partir de Dockerfile sous /tempdir
cd tempdir
docker build -t pubmed_restit .

# Lancement du container ctn_restit avec l'image pubmed_restit
docker run -t -d -p 5050:5050 --name ctn_restit pubmed_restit

# Tester si le container a bien démarré
docker ps -a
