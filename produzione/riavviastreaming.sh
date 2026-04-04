echo $1 > /home/gb-home/scripts/output.old
sudo pidof ffmpeg > input
while read line
do
echo "pid ${line}"
sudo kill ${line}
done < input

