docker run -d --name nginx-base nginx 
docker exec -it nginx-base bash
sed -ie 's/Welcome to nginx!/Welcome to my website!/' /usr/share/nginx/html/index.html
exit
docker commit nginx-base nginx-custom
docker login
docker tag nginx-custom xamyp/nginx-custom
docker push xamyp/nginx-custom