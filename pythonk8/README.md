Prerequisites: Make sure you have already installed: Docker Engine Docker Compose

The workflow will look like this: We will create Dockerfiles for each service to build images. We will create docker-compose.yml to run multiple containers together. Deploy the entire stack with the docker compose command.

As we want uWSGI to work as the web server and we want the traffic to be routed through Nginx. These two sections have their own dependencies. So we can isolate each in a container. Therefore, we have to build two Dockerfiles for each service, which docker-compose.yml can use in such a way that it will call upon a Dockerfiles to allow you to create even more complex containers.

After defining your entire application in a single docker-compose.yaml file ,you can breathe a sigh of relief .You just have to run a single command docker-compose up to run your entire app. Your Docker containers are running, feel free to rush to localhost to see your new web app live running in two separate containers.
