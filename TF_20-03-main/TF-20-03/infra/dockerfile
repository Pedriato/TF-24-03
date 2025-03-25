FROM postgres:latest
ENV POSTGRES_DB=escola
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=senha123
COPY setup.sql /docker-entrypoint-initdb.d/

EXPOSE 5432