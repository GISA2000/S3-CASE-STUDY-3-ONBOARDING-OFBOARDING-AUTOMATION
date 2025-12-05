FROM phpmyadmin/phpmyadmin:latest

# Enable SSL and rewrite modules
RUN a2enmod ssl rewrite

#pma secret config file kopieren naar juiste directory

COPY pma_config/config.secret.inc.php /etc/phpmyadmin

# Copy SSL certs
COPY certs/pma_cert.crt /etc/ssl/certs/pma_cert.crt
COPY certs/pma_cert.key /etc/ssl/private/pma_cert.key


# Copy Apache HTTPS config
COPY phpmyadmin.conf /etc/apache2/sites-available/phpmyadmin.conf

#apache eigenaar maken van "/var/www/html"

RUN chown -R www-data:www-data /var/www/html 

# Enable the custom HTTPS site (after files are in place)
RUN a2ensite phpmyadmin.conf && \ 
    apachectl configtest

EXPOSE 443 

# Start Apache in foreground
CMD ["apachectl", "-D", "FOREGROUND"]
