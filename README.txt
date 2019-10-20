CREATE MYSQL SERVER:
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql

IF ALREADY CREATED, RUN IT
docker start some-mysql

GET IP FOR DOCKER CONTAINER (MAY NOT BE LOCALHOST):
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' some-mysql

INSTALL PIP MODULES:
pip install mysql-connector-python
pip install flask
pip install pytest-mock
pip install pytest-mock