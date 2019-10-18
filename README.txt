START MYSQL SERVER:
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql

GET IP FOR DOCKER CONTAINER:
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql

INSTALL MYSQL.CONNECTOR:
pip install mysql-connector-python