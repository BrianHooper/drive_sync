drive1=drive1
drive2=drive2

files1=$(find drive1 | tail -n +2)
files2=$(find drive2 | tail -n +2)

for f in $files1
do
	mod=$(date +%s -r "$f")
	echo -e "$f,$mod" >> drive1.csv
done

for f in $files2
do
        mod=$(date +%s -r "$f")
        echo -e "$f,$mod" >> drive2.csv
done
