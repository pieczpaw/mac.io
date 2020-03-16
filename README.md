# Branch
There are two branches, default is "master", but there is also branch called "alternative" which has different Docker file.

# mac.io
This is PoC for higher need

## Index
- [Dockerfiles](#Dockerfiles)
- [Script](#Script)
- [Usage](#Usage)


## Dockerfiles
I have create two separate docker files. 
 - First one Dockerfile, download image prepared by me, where everything is installed.
 - Second - Dockerfile_alternative is using default CentOS 8 docker container and all stuff is installed during container deployment.


## Script
Script macquery.py is checking vendor or mac address is locatet at /mac.io


## Usage

    python3 /mac.io/macquery.py 00:50:56...

## Security
Regarding security we could run container wihtout root privileges + configure SElinux (in case of RedHat, CentOS)
Container image can be also signed. Are the running container should be up to date.
