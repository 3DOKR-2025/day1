# Générer le jar en utilisant un conteneur et le binaire installé sur votre pc (optionnel)
cd demo
docker run --rm \
  -v "$PWD:/app" \
  -w /app \
  gradle:8-jdk23 ./gradlew bootJar
cd ..

# Correction
docker build -t spring-boot-app .
docker run --name spring-boot-container -p 8080:8080 -d spring-boot-app
curl localhost:8080 