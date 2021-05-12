# assignment-repo
1. Created Application using Python Flask framework

Direct application url: http://18.217.231.21:5000/hello


2. Containerize using Dockerfile code for the testing purpose

3. Used Python as base image, overall image is pretty light weight, tested, less layers and without any Base image

4. Created new release using command
git checkout -b release/assignment-demo

5. Changed the code in main.py to add additional url /health

git push origin release/assignment-demo

6. Jenkins job configured at url
http://18.217.231.21:8080/job/assignment-job/
Username: admin
Password: admin123

7. Jenkins job automatically triggers, with following details
 - As soon as new commit is there in release/assignment-demo branch
 - Pipeline will be triggered and do the following tasks:
 - Download the latest code
 - Create the new light weight image
 - Stop all existing container
 - Launch new container with port forwarding at port 5000

BONUS QUESTIONS:

1. Code review:

For merge with master branch, developer need to raise PullRequest, which will be approved by Reviewer.


