#requirements: node.js and underscoreJS
#https://github.com/ddopson/underscore-cli

hopt -s nullglob
for myfile in *.json
do
    echo $myfile
    cat $myfile | underscore print > output/$myfile 
done
