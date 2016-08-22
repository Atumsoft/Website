FROM php:7-apache

RUN apt-get update && apt-get install -y libpng12-dev libjpeg62-turbo-dev libfreetype6-dev 
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd
