AGOAMS (Au, 	o 	matic Gene Ontology Annotation for massive sequencing)
GOAA (Gene Ontology Automatic Anotation)
AFAMS (Automatic Functional Annotator for Masive Sequencing)
AFA (Automatic Functional Anotator)


<h1>GeneOntology-Python</h1>

A set of scripts in python designed to work with Gene Ontology project.


En esta artículo se presenta y evalúa _______________ una herramienta bioinformática libre, está diseñada para automatizar y facilitar el proceso de anotación funcional de genomas y transcriptomas a traves de los terminos de Gene Ontology.  Las anotaciones de Gene Ontology son de gran utilidad para entender las funciones asociadas con las secuencias genómicas y transcriptómicas.  ______ permite generar asociaciones masivas de términos de Gene Ontology a genomas y transcriptomas.  _____ además de hacer una anotación funcional de genomas y transcriptomas es capaz de generar diagramas de fácil interpretación para un usuario a partir de una lista de términos en los cuales quiera centrar su investigación. _____ está compuesto de varios pasos los cuales el usuario puede ejecutar uno a la vez o todos de una vez según sea su necesidad.  Al comparar ____ con herramientas como Blast2GO y CateGOrizer se evidenció ______________________.



<h2> Setup </h2>

<h3> Dependences </h3>

<ul> 
<li>Python 2.7</li>
<li>MySql Database </li>
</ul>

<h3>Optional Dependences</h3>
<h4>Graphing tools:</h4>
<ul>
<li>CairoSVG</li>
<li>Cairo</li>
<li>Tinycss </li>
<li>Cssselect </li>
<li>Pygal</li>
<li>Pycha</li>
</ul>

<h4>How to install optional dependences? </h4> 

easy_install CairoSVG tinycss cssselect pygal <br>

Clone the git repository <br>

git clone https://github.com/alejo0317/GeneOntology-Python.git
http://nazkter.xyz/optimizar-wordpress-pagespeed-insights/

<h3> Configure database </h3>

Edit the config.py file with your database settings (user, password, database)

<h2> Download mappings file and populate mysql database </h2>

Download the file idmapping.tab from ftp://ftp.pir.georgetown.edu/databases/idmapping/idmapping.tb and use it to populate your local database to generate GeneOntology associations.  <br>

To populate the database with the file idmapping.tab use the script named mappingsToDB.py. This a populate example: <br> 
python2 mappingsToDb.py /path/to/idmapping.tab

<h2> How to use </h2>

You can use the scripts one by one or can use the full wrapper of all process.

<h2> Scripts on this repository </h2>

<h4> GoDistribution.py </h4>

Generates two files: a file containing relation between GO Terms and sequences, another file containing the tabbed counts of GO terms wanted.

<h4> hits2go.py </h4>

Associantes Uniprot, Refseq, GI, accessions to GO identifiers using a mappings table.

<h4> GraphPie.py </h4>

Generates a Pie chart from a file with the GO counts.

<h2> Test data include </h2>

We have include a set of files to test this scripts. You will find it on the folder test_data

<h4> sequences2hits.csv</h4>
A blast-generated-file with the querys and subjects (NR and Uniprot database has been used)
<h4> sequences2Gos.csv </h4>
A relation between Sequences and his associated GO terms.
<h4> gos2Sequences.csv </h4>
A relation between GO terms and his association with the Sequences.
<h4> gosCounts.tab </h4>
Ready to graph file.

<h2> Other files include </h2>
<h4> go.obo </h4>
This file contain	s the descriptions and relations bettwen the avaliable GO terms. Has been downloaded from http://purl.obolibrary.org/obo/go.obo
<h4> Celullar_Component </h4>
A list of "2nd level" GO terms from the GO category Celullar Component (GO:0005575)
<h4> Biological_Process </h4>
A list of "2nd level" GO terms from the GO category Biological Process (GO:0008150)
<h4> Mollecular_Function </h4>
A list of "2nd level" GO terms from the GO category Mollecular Function (GO:0003674)




