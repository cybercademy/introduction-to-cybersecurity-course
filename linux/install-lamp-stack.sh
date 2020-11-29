#!/bin/bash

# Purpose: This is a script to install the LAMP Stack and configure baselines testing.

# Probe for and update the system.
sudo apt update 

# Install Apache2, MySQL, and PHP.
sudo apt install apache2 mysql-server php php-mysql libapache2-mod-php php-cli

# Run/Enable Apache2 on Boot.
sudo systemctl enable apache2

# Restart Apache2 web server.
sudo systemctl start apache2 

# Enable HTTP and HTTPS on UFW Firewall for apache web server.
sudo ufw allow in "Apache Full" 

# Set read/write permissions for default html directory location.
sudo chmod 755 /var/www/html/

# Create info.php and test for php.

sudo touch /var/www/html/info.php

sudo chmod 777 /var/www/html/info.php

sudo echo "<?php phpinfo(); ?>" > /var/www/html/info.php

sudo chmod 755 /var/www/html/info.php

# Open web browser and test for web access.
xdg-open "http://localhost"

xdg-open "http://localhost/info.php"
