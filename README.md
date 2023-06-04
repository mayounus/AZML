# Overview

<Run Python-based machine learning application using the Flask web framework with industry best standards to deploy self hosted Azure cloud infrastructure app. Use MSFT link for details on using CI/CD to deploy a Python web app to Azure App Service on Linux: https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops
>

## Project Plan
Using spreedshet for planning and Tello Board for monitoring & managing projects allows for a timely business requirments successful delivery. 
Please find links to both the Trello board and spreadsheet which helps in monitoring timeline for projects and future plans for improvements. 

* Trello board for the project: https://trello.com/b/WRbN7Qb2/python-flask-ml-web-application
* Spreadsheet Plan: https://app.box.com/s/f3o77ggxmls3ao9u17tsp5sa6vfu1ll7


## Instructions

<Architectural Diagram:
![image](https://github.com/mayounus/AZML/assets/129637851/95695607-acfe-4db5-83a4-7cf6597256b1)
>

<Instructions for running the Python project.  

1- Clone Repo using AZ Bash CLI.   git clone https://github.com/mayounus/AZML.git
2- Create App Service to initially deploy your app EX: <az webapp up -n "azmlmoyounus">
3- Run commands.sh file which includes scaffolding
    ![image](https://github.com/mayounus/AZML/assets/129637851/78748cb7-738a-48a7-a926-d3f48f6b2a07)
   
* Project running on Azure App Service
  ![image](https://github.com/mayounus/AZML/assets/129637851/15b29188-9e6f-47ad-9d14-57780656c1e0)

* Project cloned into Azure Cloud Shell
  ![image](https://github.com/mayounus/AZML/assets/129637851/23b79fe4-7c1e-473e-9f85-a0437b57bd53)

* Passing tests `make all` command from the `Makefile`
  ![image](https://github.com/mayounus/AZML/assets/129637851/522f07a9-cdb6-4c59-8eaa-081b03dc6d6d)
  
 * Successful Github Actions.
  ![image](https://github.com/mayounus/AZML/assets/129637851/4bb29acb-b149-4207-852f-dada8f1e9af9)

* Output of a test run
  ![image](https://github.com/mayounus/AZML/assets/129637851/b3ad8f28-27d3-459b-97bb-83db32da9eea)

* Successful deploy of the project in Azure Pipelines.  
  ![image](https://github.com/mayounus/AZML/assets/129637851/74e0046b-6fb4-463a-b9e6-69891349e00c)

* Running Azure App Service from Azure Pipelines automatic deployment
  ![image](https://github.com/mayounus/AZML/assets/129637851/5c3678c5-52ab-472d-b0ee-68bc28554915)

 *Passing Locust test.
  ![image](https://github.com/mayounus/AZML/assets/129637851/2eed5897-c73a-4869-a7cf-b4ba38b805e7)


* Output of streamed log files from deployed application
  ![image](https://github.com/mayounus/AZML/assets/129637851/66c47144-67c8-4b05-8902-b5fd534843c3)

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


