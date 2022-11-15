# README

## How to run
* Install `mysql-connector` packager using pip
        `pip install mysql-connector`
## Prepare DB
`docker run --name simple-app-db --rm -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=customer_data -p 3306:3306 -it mysql:latest`

login to container `docker exec -it a0ba7b423edb bash`

create user `create user 'user'@'%' identified by 'password'; grant all on *.* to 'user'@'%';`