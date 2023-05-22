#!/bin/bash


if [[ ! -f "/etc/raddb/certs/ca.pem" || ! -f "/etc/raddb/certs/ca.key" ]]; then
  echo "Error: CA certificate and key are missing."
  exit 1
fi


while getopts u: option
do
  case "${option}" in
    u) username=${OPTARG};;
    *) echo "Usage: $0 [-u username]"; exit 1;;
  esac
done


openssl req -new -newkey rsa:4096 -nodes -out user_certs/${username}.csr -keyout user_certs/${username}.key -config /etc/raddb/certs/client.cnf
openssl ca -batch -keyfile /etc/raddb/certs/ca.key -cert /etc/raddb/certs/ca.pem -in user_certs/${username}.csr -out user_certs/${username}.crt -extensions xpclient_ext -extfile xpextensions -config /etc/raddb/certs/client.cnf
 

cp user_certs/${username}.crt user_certs/${username}.pem
cp user_certs/${username}.key user_certs/${username}.key
chmod 640 user_certs/${username}.pem
chmod 640 user_certs/${username}.key

