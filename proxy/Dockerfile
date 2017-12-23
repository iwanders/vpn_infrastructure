FROM ubuntu:trusty
RUN apt-get -q update && apt-get -qy install -y nginx  

# Remove the original nginx config.
RUN rm -v /etc/nginx/nginx.conf

# Copy all configuration files from the current directory
ADD ./etc/ /etc/

# Set the default command to execute
# when creating a new container
CMD service nginx start
