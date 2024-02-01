#!/usr/bin/env bash
# Install Nginx if not already installed
if [ ! -x "$(command -v nginx)" ]; then
    apt-get update
    apt-get -y install nginx
fi
USER_GROUP='root:root'
# Create necessary directories
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create fake HTML file
echo -e "<html>\n<head>\n</head>\n<body>\n  Holberton School\n</body>\n</html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group recursively
chown -R $USER_GROUP /data

# Update Nginx configuration
config_text="location /hbnb_static {\n\talias /data/web_static/current/;\n\tindex index.html;\n}\n"
sed -i "/server_name _;/a $config_text" /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

exit 0
