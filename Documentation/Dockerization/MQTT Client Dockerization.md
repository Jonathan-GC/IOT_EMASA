# MQTT Client Dockerization


## Installation and Deployment Guide

Software Version: 1.0 | 14 may 2025

## Installation and Deployment Guide template information

The purpose of this document is to provide the System Administrator or any other technical stakeholder with a complete and easy to follow guide designed specifically for the Technical Domain. It is intended to provide installation instructions to any stakeholder that has an interest or a role in the project.

### Document Responsibilities

The Installation and Deployment Guide is first created in the Deployment process step. Responsibilities for document creation and content are shown in the [RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) chart below:


| **Group Manager** | **Project Manager** | **Technical Lead** | **Business Analyst** | **Developer** | **Testing Analyst** |
| --- | --- | --- | --- | --- | --- |
| I | A | R | I | C | I |

### Combining or splitting documents

Documentation required by the process may be physically combined into fewer documents or split up into more documents in any way which makes sense to the project provided that all topics required by all the standard templates are present.

If information is split across several documents, all related documents shall be included in the reviews and sign off. For example, when installation and deployment instructions are in separate documents, the documents shall undergo the same preparation, review, and approval activities as well as review to ensure consistency of technical information among the component documents.

### Reviews

The Installation and Deployment Guide is to be reviewed by the Technical Lead, and the Test Lead. At a minimum the review should ensure that the Installation and Deployment Guide is technically correct and can be used to install and deploy the software or system in the target environment, resulting in a working and usable system.

### Approvals/Signoffs

The Installation and Deployment Guide is usually a deliverable component of the software solution. It is reviewed and bugs may be logged against it. But it is not approved or signed off unless required by the client scope/contract.

### Installation Guide guidelines

*Retain the following information in the final document, usually on the back of the cover page. The comment is for guidance and may be deleted or hidden.*

### Acknowledgements

This document may refer to documents in Adobe® Acrobat® Portable Document Format (PDF). (Adobe® and Acrobat® are registered trademarks of Adobe Systems Incorporated.)

This document may refer to use of products in the Microsoft® Office suite, the Microsoft® Team Foundation Server® and Visual Studio®.

### Guidelines for revising this document

This document is prepared using Microsoft Word. The Arial 11 point font is used.

Features of Word can be used to automatically maintain section numbers, table and figure numbers, and fields for information that appears frequently throughout the document.

This document is set up with margins of 0.75 inches on all sides. This setting will allow the document to be printed on both US Letter and European A4 paper sizes without reformatting.

This document contains comments to the author with guidelines on using or revising the document. To view this information, turn on the Review features of Word to show the Final Showing Markup view.

### Ownership and revision

This Installation and Deployment Guide is owned and controlled by the project’s System Administrator. After a baseline of this document is published, the Technical Lead shall ensure that it is placed under change control.

Each change or revision made to this Installation Guide Document shall be summarized in “Revision history” section of this document.

## Contents

[1. Introduction](#_Toc198137427)

[1.1. Purpose](#_Toc198137428)

[1.2. Revision history](#_Toc198137429)

[1.3. Intended audience and reading suggestions](#_Toc198137430)

[1.4. Technical project stakeholders](#_Toc198137431)

[1.5. References](#_Toc198137432)

[1.6. Definitions, acronyms and abbreviations](#_Toc198137433)

[2. System Configurations](#_Toc198137434)

[2.1. Roles, Features, and Packages](#_Toc198137435)

[2.2. Command-Line](#_Toc198137436)

[2.3. Configured Values](#_Toc198137437)

[3. Container Configurations](#_Toc198137438)

[3.1. Service 1 (MQTT Client)](#_Toc198137439)

[3.1.1. Roles, Features, and Packages](#_Toc198137440)

[3.1.2. Configured Values](#_Toc198137441)

[4. Additional Utilities](#_Toc198137442)

[4.1. Prepare the Environment](#_Toc198137443)

[4.1.1. Requirements](#_Toc198137444)

[4.1.2. Create Virtual Environment](#_Toc198137445)

[4.2. Healthchecks](#_Toc198137446)

[4.3. Gateway Simulator](#_Toc198137447)

[4.4. Device Simulator](#_Toc198137448)

[5. Software Deployment](#_Toc198137449)

[5.1. Connection with EMASA API-REST](#_Toc198137450)

[5.2. Orchestration](#_Toc198137451)

[6. Troubleshooting](#_Toc198137452)

# 1. Introduction

## 1.1. Purpose

The purpose of this Installation and Deployment Guide is to describe in technical terms the steps necessary to install the software referred to ChirpStack open-source LoRaWAN Network Server and make it operational.

## 1.2. Revision history

The Revision history table shows the date, changes, and authors who have worked on this document.

| Version/Change request number | Version date | Description of changes | Author |
| --- | --- | --- | --- |
| 1.0 | 21/04/2025 | First Draft | Eder D. Martínez |

## 1.3. Intended audience and reading suggestions

This Installation and Deployment Guide is intended to be used by technical stakeholders of the project who will be responsible for planning, performing, or maintaining the installation or deployment, such as the Systems Developers, Site Reliability Engineers (SRE) or Deployment Engineers.

It is intended that stakeholders and software support personnel can read this document and coordinate their efforts in the installation/deployment of the application.

## 1.4. Technical project stakeholders

This section provides a list of all known stakeholders with an interest in the project.

| Name | E-mail address | Role |
| --- | --- | --- |
| Jemison Montealgre | jeminson00@gmail.com | Product owner |
| Jonathan Gonzalez | jonathangc.awt@gmail.com | Lead Developer |
| Eder Martínez | 2220211052@estudiantesunibague.edu.co | Deployment Engineer |
| Carlos Bernal | 2420201003@estudiantesunibague.edu.co | Software Developer |

## 1.5. References

| Reference No. | Document | Author(s) |
| --- | --- | --- |
| REF-1 | [Enabling Intel VT and AMD-V virtualization hardware extensions in BIOS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/5/html/virtualization/sect-virtualization-troubleshooting-enabling_intel_vt_and_amd_v_virtualization_hardware_extensions_in_bios#sect-Virtualization-Troubleshooting-Enabling_Intel_VT_and_AMD_V_virtualization_hardware_extensions_in_BIOS) | Red Hat |
| REF-2 | [Install Hyper-V on Windows](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v) | Microsoft |
| REF-3 | [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install) | Red Hat |
| REF-4 | [Install Docker Engine](https://docs.docker.com/engine/install/) | Docker |
| REF-5 | [Overview of Docker Desktop](https://docs.docker.com/desktop/) | Docker |
| REF-6 | [paho-mqtt](https://pypi.org/project/paho-mqtt/) | Pypi |
| REF-7 | [MQTT Ports: Common Ports and How to Configure and Secure Them](https://www.emqx.com/en/blog/mqtt-ports) | EMQ Technologies |

## 1.6. Definitions, acronyms and abbreviations

| Term | Definition |
| --- | --- |
| Administrator | This is anyone from the client that has been given administrative rights in the ProjectName. |
| Ubuntu | Ubuntu 22.04 |
| db | Data base |
| CA | Certification Authority |
| CSR | Certificate Signing Request |

# 2. System Configurations

Installation of this product is supported on the following operation systems and versions:

* Linux Ubuntu 20.04
* Linux Ubuntu 22.04(recommended)
* Linux Ubuntu 24.04

## 2.1. Roles, Features, and Packages

**Features**

The main software is fetched from the project’s repository on GitHub and stored on chirpstack-docker directory

**Packages**

The following software packages must be installed before the deployment of the software:

1. Git Version Control System
2. Curl Command-Line Requests Tool
3. Vim Command-Line Text Editor
4. Docker Engine

## 2.2. Command-Line

**Authentication**

Most of the commands are recommended to be executed with administrative privileges

## 2.3. Configured Values

The table below describes the values for your installation environment for future reference. (Note: recording of information throughout should be in keeping with your local policies for system documentation and password security). The following map describes the key, values used for the current system.

| Information | Value |
| --- | --- |
| Default User | dragino |
| Default Root User Password | dragino |
| Default Software Directory | /home/dragino/IOT\_EMASA/lorawan\_server |

# 3. Container Configurations

## 3.1. Service 1 (MQTT Client)

The installation of this product is supported on the following operative systems and versions:

* Linux Ubuntu 20.04
* Linux Ubuntu 22.04(recommended)
* Linux Ubuntu 24.04

### 3.1.1. Roles, Features, and Packages

**Packages**

The following software packages must be installed on the construction of the Docker container:

1. paho-mqtt:1.6.1

### 3.1.2. Configured Values

The table below describes the values for your installation environment for future reference. (Note: recording of information throughout should be in keeping with your local policies for system documentation and password security). The following map describes the key, values used for the current deployment.

| Information | Value |
| --- | --- |
| Container name | paho-1 |
| Volumes | ● ../../.certs:/etc/paho-mqtt/certs |
| Environment Variables | ● MQTT\_BROKER\_HOST <br>● MQTT\_BROKER\_PORT |

# 4. Additional Utilities

This client also includes some testing utilities which are not accessible in docker container but are accessible for developers. It is recommended to check .env files and create a virtual environment to run these components.

## 4.1. Prepare the Environment

### 4.1.1. Requirements

Python 3.10

### 4.1.2. Create Virtual Environment

1. To create a virtual environment, run the following command:
    ```sh
    python -m venv .venv
   ```
2. A .venv folder will show up in the file explores, to enable the environment run the command
    ```sh
    .env/scripts/activate
    ```
3. Finally install the required packages saved in the requirements.txt file with the command

    ```sh
    pip install -r requirements.txt
    ```
## 4.2. Healthchecks

This service determines the health status of the container. It verifies if a main process is running and checking connectivity to an MQTT broker. It normally runs automatically during the dockerization.

## 4.3. Gateway Simulator

cript simulates an MQTT gateway for ChirpStack v4. It periodically generates sensor data (temperature, humidity, light), encodes it, and sends uplink payloads and gateway statistics to MQTT topics. Configurable parameters include MQTT connection details, device, and gateway information.

## 4.4. Device Simulator

script simulates a LoRaWAN device, generating sensor data (temperature, humidity, light), encoding it in Base64, and publishing it to MQTT topics in ChirpStack format. It mimics real device behavior with configurable settings and periodic message sending.

# 5. Software Deployment

## 5.1. Connection with EMASA API-REST

To have communication with the EMASA middleware, it is necessary to add a network into docker system, to do it, run the following command
```sh
docker network -d bridge chirp-django-net
```
Then, add the netwroks prop into each container settings
```yml
networks:
      - chirp-django-net
```
## 5.2. Orchestration

Then modify/create a docker-compose.yaml file and copy the following code into it.

NOTE: Environment variables and ports can be changed as necessary
```yml
services:
  paho:
    build: .
    restart: unless-stopped
    volumes:
    - ../../.certs:/etc/paho-mqtt/certs
    environment:
    - MQTT\_BROKER\_HOST=lorawan-server-mosquitto-1
    - MQTT\_BROKER\_PORT=1883
    networks:
    - chirp-django-net

networks:
    chirp-django-net:
        external: true
```
Finally, open the terminal in the path where docker-compose.yaml file is located and insert the following command, then press enter.
```sh
docker-compose up -d
```
## 5.3. Deployment Diagram for MQTT Client
![Diagram](resources/SVG/mqtt_client_docker_diagram.svg)

# 6. Troubleshooting

Docker logs can be visualized either through the Docker Engine container information using the docker logs <container name> command, by Checking container information on Docker Desktop
```sh
docker logs –-follow <docker container name>
```
or by accessing the log files directly on the host system. On Linux Ubuntu, logs are located at
```sh
/var/lib/docker/containers/<container\_id>/<container\_id>-json.log
```
