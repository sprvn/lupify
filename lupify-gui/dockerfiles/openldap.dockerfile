FROM osixia/openldap:1.2.1

COPY data/openldap-user.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom/01-user.ldif

EXPOSE 389
EXPOSE 636
