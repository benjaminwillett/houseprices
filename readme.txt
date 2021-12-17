Ensure Docker is installed
git clone https://github.com/benjaminwillett/houseprices.git
within this directory run the following docker command:

for my mac from the following:
#sudo docker build -f- . < Dockerfile-dev
#sudo docker run -d -e FIXER_URL_APIKEY='http://data.fixer.io/api/latest?access_key=5aa5fdb42a041e444b788df7ab68b3f0' -p 5001:5000

for my prod machine run the following:
#sudo docker build -f- . < Dockerfile
#sudo docker run -d -e FIXER_URL_APIKEY='http://data.fixer.io/api/latest?access_key=5aa5fdb42a041e444b788df7ab68b3f0' -p 5001:5000
