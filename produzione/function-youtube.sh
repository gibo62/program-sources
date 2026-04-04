#! /bin/bash
wget -O- -q https://appoggio.nsvalme.cloud/funzione.txt > /home/gb-home/scripts/output.txt
diff /home/gb-home/scripts/output.txt /home/gb-home/scripts/output.old > diff.txt
if grep -q c1 "diff.txt"; then
        if grep -q video "/home/gb-home/scripts/output.txt";  then
                echo video
                /home/gb-home/scripts/riavviastreaming.sh video
        else
                echo immagine
		/home/gb-home/scripts/riavviastreaming.sh immagine
        fi
else
	echo "no differenze"
fi

