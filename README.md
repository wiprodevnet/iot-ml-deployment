# iot-ml-deployment
Deploying machine learning model on IOX-Gateway
## Technologies:
1. Python3
2. Flask


## Installation and Configuration:
* Clone this repo first and follow the steps to run each Component.

## Steps to Deploy IOXApp

### Prerequisites
Previous IOx labs needed to complete this lab
You will need to have completed the learning the following labs:
1. Introduction to Cisco IOx - https://developer.cisco.com/learning/tracks/iot/IoT-IOx-Intro/intro-2-iox/step/1
2. Intro to Containers - https://developer.cisco.com/learning/tracks/iot/IoT-IOx-Apps/Containers-101/step/1
3. Intro to Docker - https://developer.cisco.com/learning/tracks/iot/IoT-IOx-Apps/docker-101/step/1

### Docker technologies
You should have a basic understanding on how to build and run a docker application.

### Docker Platform
To create a Docker image and push it to the Docker Hub, you will need the correct Docker tools for your platform which are available at https://www.docker.com/products/overview.
Download and install the correct version for your operating system.

### IOx Dev Environment As A Service 
This lab has instructions for using a docker container that sets up a web service you can access from your browser. The web service is a browser based version of Visual Studio Code, developed by Coder Com (https://coder.com) and utilizes docker to run the service. Since it is Visual Studio Code, it it provides a text/code editor and comes pre-built with ioxclient and everything you need to build IOx applications. You will need the Docker Platform on your desktop or developer machine to run this environment.

### Cisco AnyConnect Client
To access the DevNet Sandbox, you will need to use the Cisco AnyConnect Client for Virtual Private Network (VPN) access to the IOx instance. If you need to install it, you can find it at this link.

	Note: If you are working on a DevNet Lab workstation, this software is already installed.

### ioxclient
You will need the ioxclient to package and deploy the IOx Application. If you need to download it, you can find it at this link.
	Note: If you are working on a DevNet Lab workstation or you are using the "IOx Dev Environment As A Service" container, this software is already installed.

### git
One way to get the application template code is to use git. We have the option to download the code, so this step is optional. If you are working on a DevNet Lab workstation, the git software is already installed. If you need to install it, you can find it at this link.

	Note: You can verify the installation of git by opening a command prompt and running:

### git --version
	Additional Note: If you are working on a DevNet Lab workstation or you are using the "IOx Dev Environment As A Service" container, this software is already installed.

Once you have verified the prerequisites to complete this lab you will:

### Reserve an IOx Sandbox instance:- 
   1. Setup a Local Container for the IOx Developer Environment
   2. Create a small IOx Application to run on the Sandbox IOx device
   3. Package the IOx Application with the ioxclient Docker tools
   4. Connect to the DevNet Sandbox
   5. Deploy the IOx Application
   6. Monitor and review the IOx Application
   7. Test the output of the IOx Application

## Refer below link for more details
* https://developer.cisco.com/learning/modules/iox-basic/iot-iox-app-docker/step/1

