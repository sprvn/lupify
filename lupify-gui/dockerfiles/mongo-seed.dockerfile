FROM mongo

COPY scripts/mongo_seed.sh /mongo_seed.sh
COPY data/mongo_seed_data.json /seed_data.json
COPY scripts/create_mongo_user.sh /create_mongo_user.sh
COPY scripts/init_script_dev.sh /init_script_dev.sh

ENTRYPOINT /bin/bash /init_script_dev.sh
