docker run -d \
  --name redis \
  -p 6379:6379 \
  --restart always \
  -e REDIS_HOST_PASSWORD=Sup1nf0 \
  redis \
  /bin/sh -c "redis-server --requirepass \$REDIS_HOST_PASSWORD"

pip3 install redis