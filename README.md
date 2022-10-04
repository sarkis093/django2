# Project e-commerce

## Project description:
<p> A simple e-commerce project using Django framework and Docker.</p>
<br>

## Libraries needed for the project:
`$ sudo apt install libmysqlclient-dev python3-dev`
<br>

#### * for each project we create a "forms.py" file that contains all the project forms.
<br>

## Comands Docker:
`$ sudo docker build -t <Dockerfile> .`
<br>

`$ docker run -d -t -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<PASS_ROOT> -e MYSQL_DATABASE=<DATABASE> -e MYSQL_USER=<USER> -e MYSQL_PASSWORD=<PASS_USER> <IMAGE_FROM_DOCKERFILE>`
<br>

`$ docker exec -it <CONTAINER_ID> bash`


