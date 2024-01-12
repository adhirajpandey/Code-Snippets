DOCKER_IMAGE_NAME="notion_auto"
DOCKER_CONTAINER_NAME="notion_auto_cont"

FLASK_APP_PORT="5000"
HOST_MACHINE_PORT="5002"

docker rm -f ${DOCKER_CONTAINER_NAME}
docker rmi -f ${DOCKER_IMAGE_NAME}
echo "Removed Docker Image"


docker build -t ${DOCKER_IMAGE_NAME} .
docker run -d --name ${DOCKER_CONTAINER_NAME} --restart unless-stopped -p ${HOST_MACHINE_PORT}:${FLASK_APP_PORT} ${DOCKER_IMAGE_NAME}
echo "Docker container deployed using new image"