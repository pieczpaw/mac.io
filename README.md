# mac.io
This is PoC for higher need

## Index
- [Dockerfiles](#Dockerfiles)
- [Script macquery.py](#Script macquery.py)
- [Usage](#Usage)


## Dockerfiles
I have create two separate docker files. 
 - First one Dockerfile, download image prepared by me, where everything is installed.
 - Second - Dockerfile_alternative is using default CentOS 8 docker container and all stuff is installed during container deployment.


## Script macquery.py
Script which is checking vendor or mac address is locatet at /mac.io


## Usage
python3 /mac.io/macquery.py 00:50:56...

