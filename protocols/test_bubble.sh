rm *.txt

echo "-1" > distro_bubble.txt
echo "-1" > distro_protocolo.txt

z="0"
for i in `seq 1 14000`
do
	valor_o=$(shuf -i 0-1999 -n 1)
	valor=$(shuf -i 0-1999 -n 1)
	tempo=$(shuf -i 1-400 -n 1)
	if [ "$valor_o" = "$valor" ]
	then
	    echo "$valor_o,$valor,$tempo"
	else
	    echo "$valor_o,$valor,$tempo"		
		python ./bubble.py $valor_o $valor ../../traces/grm2000/contacts_test.csv $tempo >> result_bubble.0.txt &
		python ./flood.py $valor_o $valor ../../traces/grm2000/contacts_test.csv $tempo >> result_bubble.2.txt &
		#python ./bubble.py $valor_o $valor ../mergedContacts.csv 1 >> result_bubble.1.txt &
		#python ./bubble.py $valor_o $valor ../mergedContacts.csv 2 >> result_bubble.2.txt &
		if [ `expr $i % 4` -eq 0 ]
		then
			wait;
		fi
	fi
done
