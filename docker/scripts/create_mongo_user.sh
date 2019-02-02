#!/bin/bash

n=0
until [ $n -ge 60 ]
do
        mongo_output=`mongo --host mongo --username ${MONGO_INITDB_ROOT_USERNAME} --password ${MONGO_INITDB_ROOT_PASSWORD} --authenticationDatabase admin --eval  "db.getSiblingDB('${MONGO_DB}').createUser({user:'${MONGO_USER}', pwd:'${MONGO_PASS}', roles:[{role:'readWrite',db:'${MONGO_DB}'}]});"`

        echo $mongo_output | grep "Successfully added user" && break
        echo $mongo_output | grep "already exists" && break
        n=$[$n+1]
        sleep 1
done
