docker build --tag express-docker:0.1.0 .
docker run \
	--detach \
	--rm \
	--publish 3000:3000 \
	--name express-docker-container \
	express-docker:0.1.0

curl http://localhost:3000/
curl http://localhost:3000/json
curl -X POST http://localhost:3000/echo -H "Content-Type: application/json" -d '{"name": "Alice", "age": 25}'
