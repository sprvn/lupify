#!/bin/bash

mongoimport --host mongo --username ${MONGO_INITDB_ROOT_USERNAME} --password ${MONGO_INITDB_ROOT_PASSWORD} --authenticationDatabase admin --db ${MONGO_DB} --collection ${MONGO_COL} --type json --file /seed_data.json --jsonArray