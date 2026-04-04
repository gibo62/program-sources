#! /bin/bash
wget -O- -q https://sanbartolome.nsvalme.cloud/funzione.txt > /home/scripts/output.txt 
diff /home/scripts/output.txt /home/scripts/output.old > diff.txt
if grep -q c1 "diff.txt"; then
	if grep -q video "/home/scripts/output.txt"; 	then
		echo video
		/home/scripts/riavviastreaming.sh video
	else
		echo immagine		
		/home/scripts/riavviastreaming.sh immagine
	fi
else
	echo "no differenze"
fi

