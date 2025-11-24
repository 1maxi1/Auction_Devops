# Auction_Devops
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io



test@test-VirtualBox:~$ sudo apt-get install -y ca-certificates curl gnupg lsb-release
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ca-certificates is already the newest version (20240203).
ca-certificates set to manually installed.
gnupg is already the newest version (2.4.4-2ubuntu17.3).
gnupg set to manually installed.
lsb-release is already the newest version (12.0-2).
lsb-release set to manually installed.
The following NEW packages will be installed:
  curl
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 226 kB of archives.
After this operation, 534 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 curl amd64 8.5.0-2ubuntu10.6 [226 kB]
Fetched 226 kB in 0s (614 kB/s)
Selecting previously unselected package curl.
(Reading database ... 153241 files and directories currently installed.)
Preparing to unpack .../curl_8.5.0-2ubuntu10.6_amd64.deb ...
Unpacking curl (8.5.0-2ubuntu10.6) ...
Setting up curl (8.5.0-2ubuntu10.6) ...
Processing triggers for man-db (2.12.0-4build2) ...
test@test-VirtualBox:~$ sudo mkdir -p /etc/apt/keyrings
test@test-VirtualBox:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
test@test-VirtualBox:~$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
test@test-VirtualBox:~$ sudo apt update
Get:1 https://download.docker.com/linux/ubuntu noble InRelease [48.5 kB]
Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease    
Hit:3 https://packages.microsoft.com/repos/code stable InRelease
Get:4 https://download.docker.com/linux/ubuntu noble/stable amd64 Packages [36.9 kB]
Get:5 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]
Get:6 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
Get:7 http://archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
Reading package lists... Done     
E: Release file for http://security.ubuntu.com/ubuntu/dists/noble-security/InRelease is not valid yet (invalid for another 16h 17min 38s). Updates for this repository will not be applied.
E: Release file for http://archive.ubuntu.com/ubuntu/dists/noble-updates/InRelease is not valid yet (invalid for another 16h 19min 23s). Updates for this repository will not be applied.
E: Release file for http://archive.ubuntu.com/ubuntu/dists/noble-backports/InRelease is not valid yet (invalid for another 16h 22min 14s). Updates for this repository will not be applied.
test@test-VirtualBox:~$ sudo apt install docker-ce docker-ce-cli containerd.io
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  docker-buildx-plugin docker-ce-rootless-extras
  docker-compose-plugin git git-man liberror-perl
  libslirp0 pigz slirp4netns
Suggested packages:
  cgroupfs-mount | cgroup-lite docker-model-plugin
  git-daemon-run | git-daemon-sysvinit git-doc git-email
  git-gui gitk gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce
  docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin git git-man liberror-perl
  libslirp0 pigz slirp4netns
0 upgraded, 12 newly installed, 0 to remove and 0 not upgraded.
Need to get 101 MB of archives.
After this operation, 426 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 https://download.docker.com/linux/ubuntu noble/stable amd64 containerd.io amd64 2.1.5-1~ubuntu.24.04~noble [22.4 MB]
Get:2 http://archive.ubuntu.com/ubuntu noble/universe amd64 pigz amd64 2.8-1 [65.6 kB]
Get:3 http://archive.ubuntu.com/ubuntu noble/main amd64 liberror-perl all 0.17029-2 [25.6 kB]
Get:4 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 git-man all 1:2.43.0-1ubuntu7.3 [1,100 kB]
Get:5 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce-cli amd64 5:29.0.2-1~ubuntu.24.04~noble [16.3 MB]
Get:6 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 git amd64 1:2.43.0-1ubuntu7.3 [3,680 kB]
Get:7 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce amd64 5:29.0.2-1~ubuntu.24.04~noble [20.3 MB]
Get:8 http://archive.ubuntu.com/ubuntu noble/main amd64 libslirp0 amd64 4.7.0-1ubuntu3 [63.8 kB]
Get:9 http://archive.ubuntu.com/ubuntu noble/universe amd64 slirp4netns amd64 1.2.1-1build2 [34.9 kB]
Get:10 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-buildx-plugin amd64 0.30.0-1~ubuntu.24.04~noble [16.4 MB]
Get:11 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce-rootless-extras amd64 5:29.0.2-1~ubuntu.24.04~noble [6,383 kB]
Get:12 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-compose-plugin amd64 2.40.3-1~ubuntu.24.04~noble [14.3 MB]
Fetched 101 MB in 4s (27.8 MB/s)                 
Selecting previously unselected package containerd.io.
(Reading database ... 153248 files and directories currentl
y installed.)
Preparing to unpack .../00-containerd.io_2.1.5-1~ubuntu.24.
04~noble_amd64.deb ...
Unpacking containerd.io (2.1.5-1~ubuntu.24.04~noble) ...
Selecting previously unselected package docker-ce-cli.
Preparing to unpack .../01-docker-ce-cli_5%3a29.0.2-1~ubunt
u.24.04~noble_amd64.deb ...
Unpacking docker-ce-cli (5:29.0.2-1~ubuntu.24.04~noble) ...
Selecting previously unselected package docker-ce.
Preparing to unpack .../02-docker-ce_5%3a29.0.2-1~ubuntu.24
.04~noble_amd64.deb ...
Unpacking docker-ce (5:29.0.2-1~ubuntu.24.04~noble) ...
Selecting previously unselected package pigz.
Preparing to unpack .../03-pigz_2.8-1_amd64.deb ...
Unpacking pigz (2.8-1) ...
Selecting previously unselected package docker-buildx-plugi
n.
Preparing to unpack .../04-docker-buildx-plugin_0.30.0-1~ub
untu.24.04~noble_amd64.deb ...
Unpacking docker-buildx-plugin (0.30.0-1~ubuntu.24.04~noble
) ...
Selecting previously unselected package docker-ce-rootless-
extras.
Preparing to unpack .../05-docker-ce-rootless-extras_5%3a29
.0.2-1~ubuntu.24.04~noble_amd64.deb ...
Unpacking docker-ce-rootless-extras (5:29.0.2-1~ubuntu.24.0
4~noble) ...
Selecting previously unselected package docker-compose-plug
in.
Preparing to unpack .../06-docker-compose-plugin_2.40.3-1~u
buntu.24.04~noble_amd64.deb ...
Unpacking docker-compose-plugin (2.40.3-1~ubuntu.24.04~nobl
e) ...
Selecting previously unselected package liberror-perl.
Preparing to unpack .../07-liberror-perl_0.17029-2_all.deb 
...
Unpacking liberror-perl (0.17029-2) ...
Selecting previously unselected package git-man.
Preparing to unpack .../08-git-man_1%3a2.43.0-1ubuntu7.3_al
l.deb ...
Unpacking git-man (1:2.43.0-1ubuntu7.3) ...
Selecting previously unselected package git.
Preparing to unpack .../09-git_1%3a2.43.0-1ubuntu7.3_amd64.
deb ...
Unpacking git (1:2.43.0-1ubuntu7.3) ...
Selecting previously unselected package libslirp0:amd64.
Preparing to unpack .../10-libslirp0_4.7.0-1ubuntu3_amd64.d
eb ...
Unpacking libslirp0:amd64 (4.7.0-1ubuntu3) ...
Selecting previously unselected package slirp4netns.
Preparing to unpack .../11-slirp4netns_1.2.1-1build2_amd64.
deb ...
Unpacking slirp4netns (1.2.1-1build2) ...
Setting up liberror-perl (0.17029-2) ...
Setting up docker-buildx-plugin (0.30.0-1~ubuntu.24.04~nobl
e) ...
Setting up containerd.io (2.1.5-1~ubuntu.24.04~noble) ...
Created symlink /etc/systemd/system/multi-user.target.wants
/containerd.service → /usr/lib/systemd/system/containerd.se
rvice.
Setting up docker-compose-plugin (2.40.3-1~ubuntu.24.04~nob
le) ...
Setting up docker-ce-cli (5:29.0.2-1~ubuntu.24.04~noble) ..
.
Setting up libslirp0:amd64 (4.7.0-1ubuntu3) ...
Setting up pigz (2.8-1) ...
Setting up git-man (1:2.43.0-1ubuntu7.3) ...
Setting up docker-ce-rootless-extras (5:29.0.2-1~ubuntu.24.
04~noble) ...
Setting up slirp4netns (1.2.1-1build2) ...
Setting up docker-ce (5:29.0.2-1~ubuntu.24.04~noble) ...
Created symlink /etc/systemd/system/multi-user.target.wants
/docker.service → /usr/lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/do
cker.socket → /usr/lib/systemd/system/docker.socket.
Setting up git (1:2.43.0-1ubuntu7.3) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for libc-bin (2.39-0ubuntu8.5) ...
test@test-VirtualBox:~$ sudo apt-get install ./docker-desktop-amd64.deb
Reading package lists... Done
E: Unsupported file ./docker-desktop-amd64.deb given on commandline






#!/bin/bash
set -e

# Переменные
DOCKER_USER="za43m1"
IMAGE_NAME="auction-app"
GIT_BRANCH="%teamcity.build.branch%"

# Определи тег в зависимости от ветки
if [ "$GIT_BRANCH" = "main" ] || [ "$GIT_BRANCH" = "refs/heads/main" ]; then
    TAG="prod-latest"
    FULL_TAG="$DOCKER_USER/$IMAGE_NAME:$TAG"
elif [ "$GIT_BRANCH" = "dev" ] || [ "$GIT_BRANCH" = "refs/heads/dev" ]; then
    TAG="dev-latest"
    FULL_TAG="$DOCKER_USER/$IMAGE_NAME:$TAG"
else
    TAG="$GIT_BRANCH"
    FULL_TAG="$DOCKER_USER/$IMAGE_NAME:$TAG"
fi

echo "Building Docker image for branch: $GIT_BRANCH"
echo "Image tag: $FULL_TAG"

# Собери образ
docker build -t $FULL_TAG .

# Логин в Docker Hub (нужны переменные окружения)
echo "%env.DOCKER_PASSWORD%" | docker login -u "%env.DOCKER_USERNAME%" --password-stdin

# Загрузи образ
docker push $FULL_TAG

echo "✅ Successfully pushed $FULL_TAG to Docker Hub"

