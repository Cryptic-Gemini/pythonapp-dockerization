# pythonapp-dockerization
Python App Dockerization for Production Environment (multiple containers ) that leads to deployment in K8's


Prerequisites: 

Make sure you have already installed: 

1- Docker Engine

2- Docker Compose


We are using the word Docker again and again . So what exactly Docker is :

Docker is a tool that facilitate the developers to create, deploy, and run applications by using containers. 

There is a keyword “containers” in this definition .Let see what is container in connection with Docker:

Container is a standard unit of software that packages up code and all its dependencies so the application runs smoothly from one computing environment to another.

You can consider container as a box which has your application’s source code and all the dependencies that will be compulsory for your application to run .This will be independent of the host OS .You just need to install Docker on your machine ,pull the images and run the containers .



Doesn’t that sounds like Virtual Machines ???
But there is a key difference between containers and Virtual Machines.

Containers give us a way to virtualize an OS so that multiple workloads can run on a single OS instance.Containers are light-weighted because they share the machine's OS system kernel and therefore do not require an OS per application .

While VMs, demands the hardware virtualization to run multiple OS instances. VM generally runs a full-blown operating system, on top of the OS the host is already running.

Deployment:

Now we move ahead to see how we can make containers. The question arises :

Where do you begin?

Which configuration file do you use? 

Which method of deployment do you use?

You could make use of a tool that allows you to carefully construct the deployment within a configuration file, and then deploy the container with a simple command.
 
 You can go with docker-compose or docker. Your choice could all depend on the complexity of the application/service you plan on deploying. And that turns out to use either a Dockerfile or a docker-compose.yml or both of them.

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
-------------------------------------------------------------------------------------------------------------------------
Docker-compose is a tool for defining and running multi-container Docker applications.
-----------------------------------------------------------------------------------------------------------------------

docker-compose.yml is a file that contains the configuration for creating the containers, exposing ports, binding volumes and connecting containers through networks.

You can use docker-compose.yml in such a way that it will call upon a Dockerfile to allow you to create even more complex 
container.




The workflow will look like this: 

1-We will create Dockerfiles for each service to build images.

2-We will create docker-compose.yml to run multiple containers together.

3-Deploy the entire stack with the docker compose command.

As we want uWSGI to work as the web server and we want the traffic to be routed through Nginx. These two sections have their own dependencies. So we can isolate each in a container. Therefore, we have to build two Dockerfiles for each service, which docker-compose.yml can use in such a way that it will call upon a Dockerfiles to allow you to create even more complex containers.

After defining your entire application in a single docker-compose.yaml file ,you can breathe a sigh of relief .You just have to run a single command docker-compose up to run your entire app. Your Docker containers are running, feel free to rush to localhost to see your new web app live running in two separate containers.
