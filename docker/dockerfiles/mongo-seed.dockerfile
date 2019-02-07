FROM mongo

COPY docker/scripts/mongo_seed.sh /mongo_seed.sh
COPY docker/data/mongo_seed_data.json /seed_data.json
COPY docker/scripts/create_mongo_user.sh /create_mongo_user.sh
COPY docker/scripts/init_script_dev.sh /init_script_dev.sh

ENTRYPOINT /bin/bash /init_script_dev.sh
