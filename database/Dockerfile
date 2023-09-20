FROM mariadb:11.1.2-jammy

# HEALTHCHECK --start-period=5m \
#     CMD mariadb -e 'SELECT @@datadir;' || exit 1
EXPOSE 3306
CMD ["mariadbd"]