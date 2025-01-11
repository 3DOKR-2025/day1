FROM openjdk:23-jdk
WORKDIR /app
COPY demo/build/libs/demo-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]