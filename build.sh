#!/bin/sh

rules_date="2016-9-27 21:15"
video_date="2016-9-27 20:50"

rules_md5=`md5sum koolproxy.txt|tr " " "\n"|sed -n 1p`
video_md5=`md5sum 1.dat|tr " " "\n"|sed -n 1p`
# rule_date=`stat koolproxy.txt|grep Modify|awk '{print $2,$3}'|cut -d"." -f1`
# rules_date=`cat koolproxy.txt | awk 'NR==1{print}' | awk '{print $3,$4}'`
# video_date=`stat 1.dat|grep Modify|awk '{print $2,$3}'|cut -d"." -f1`

cat > ./version <<EOF
$rules_md5
$rules_date
$video_md5
$video_date
EOF

cat > ./config.json.js <<EOF
{
"rules_md5":"$rules_md5",
"rules_date":"$rules_date"
"video_md5":"$video_md5",
"video_date":"$video_date"
}
EOF
