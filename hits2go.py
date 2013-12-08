#!/usr/bin/python2
#This script use the hits generated by blast and associate them to GO terms ids
#Cristian Rojas
#carojasq@correo.udistrital.edu.co+
import sys, os
sys.path.append(os.path.split(sys.argv[0])[0])
sys.path.append(os.path.split(sys.argv[0])[0]+"/Utilities")
sys.path.append("Utilities")
import Config
#The table where you have the  mappings from GO
global table 
table = "mappings_e"
def usage():
	print """ This script use the hits generated by blast and associate them to GO terms ids
	hits2go.py querys2hits.csv hits2terms.csv
	"""
	exit()

def hit2go(field_name, hit_id):
	cursor=Config.connect()
	#if field_name!="GI":
	query="SELECT GoId FROM  `%s` WHERE  `%s` =  '%s'" % (table, field_name, hit_id)
	#else:
#query="SELECT GoId FROM  `"+table+"` WHERE  `"+field_name+"` like '%"+ hit_id + "%'" 
	#print query
	cursor.execute(query)
	query_responses=cursor.fetchall()
	terms=[]
	if query_responses==None:
		terms="NotFound"
	else:
		for query_response in query_responses:
			tmp_arr=query_response['GoId'].split(";")
			terms.extend(tmp_arr)
	return list(set(terms))

#With the idenfier we'll know what is the origin of the hit identifier (RefSeq, Uniprot, Gene ID)
def hitDef2hit_id(hit_def):
	fields=hit_def.split("|")
	field_name=hit_id=""
	if "ref" in fields:
		field_name="RefSeq"
		hit_id=fields[fields.index("ref")+1]#.split(".")[0]
	elif "sp" in fields:
		field_name="UniprotAC"
		hit_id=fields[fields.index("sp")+1]#.split(".")[0]
	elif "lcl" in fields:
		field_name="UniprotAC"
		hit_id=fields[fields.index("lcl")+1]#.split(".")[0]
	elif "gi" in fields:
		field_name="GI"
		hit_id=fields[fields.index("gi")+1]#.split(".")[0]
	return [field_name, hit_id]


#The input format is:
#ID_Sequence1,sp|Q9ZZ53|NU2M_SQUAC NADH-ubiquinone oxidoreductase chain 2 OS=Squalus acanthias GN=MT-ND2 PE=3 SV=1
#ID_Sequence2,sp|Q9ZYM7|NU5M_RHISA NADH-ubiquinone oxidoreductase chain 5 OS=Rhipicephalus sanguineus GN=ND5 PE=3 SV=1
#ID_Sequence,Hit_definition

def hits2go(in_file):
	print "Associating hits to terms"
	in_file=open(in_file,"r")
	results=[]
	for line in in_file:
		tmp=line.split(",")
		seq_identifier=tmp[0].replace('""','')
		fandid=hitDef2hit_id(tmp[1].replace('""','')) #stores temporaly field to search a id to search
		field_name=fandid[0]
		hit_id=fandid[1]
		gos=hit2go(field_name, hit_id)
		results.append([seq_identifier, gos])
	return results

 
def writeOutFile(toWrite, out_file):
	print "Writing output file"
	out_file=open(out_file, "w")
	count=0;
	for result in toWrite:
		out_file.write(result[0]+","+";".join(result[1])+"\n")
		count=count+1	
	return count

def main():
	if len(sys.argv)!=3:
		usage()
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	results=hits2go(in_file)
	out=writeOutFile(results, out_file)
	print "%s associations has been writen to %s" % (str(out), out_file)

main()