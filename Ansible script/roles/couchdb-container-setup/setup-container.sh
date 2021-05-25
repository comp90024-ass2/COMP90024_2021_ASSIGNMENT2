echo "***** Start CouchDB Deployment *****"
sudo service docker restart

export node="$1"
export size=${#nodes[@]}
export user='admin'
export pass='admin'
export VERSION='3.1.1'
export cookie='a192aeb9904e6590849337933b000c99'

echo "Pull couchDB......"
sudo docker pull ibmcom/couchdb3:${VERSION}

echo "Create Docker containers......"
if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ] 
    then
        docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet) 
        docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
fi

# Create Docker
echo "Create couchDB......"
docker create\
    -p 5984:5984\
    -p 4369:4369\
    -p 9100-9200:9100-9200\
    -p 5986:5986\
    --name couchdb${node}\
    --env COUCHDB_USER=${user}\
    --env COUCHDB_PASSWORD=${pass}\
    --env COUCHDB_SECRET=${cookie}\
    --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\""\
    ibmcom/couchdb3:${VERSION}

# Start container of couchdb
echo "Start couchDB container......"
sudo docker start couchdb${node}

# Restart docker
echo "Restart couchDB container......"
sudo docker restart couchdb${node}

