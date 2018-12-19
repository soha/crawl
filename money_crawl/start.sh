#!/bin/sh

for i in `seq 0 9`; do

    sleep 5
    
    mv esol.jl esol.jl.old
    scrapy crawl ESolSpider -o esol.jl
    diff esol.jl esol.jl.old > diff.txt

    if [ ! -s diff.txt ]; then
	echo "no change"
    else
	osascript -e 'display notification "https://www.esol.co.jp/ir/" with title "check eSol"'
    fi

done
