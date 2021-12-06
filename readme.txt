Ensure Docker is installed
Create a local directory and copy the Dockerfile into this.
within this directory run the following docker command:

#sudo docker build --no-cache houseprices:latest .
#sudo docker run -d -p 5001:80 houseprices:latest