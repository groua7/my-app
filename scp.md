# when do we use scp in linux ?
scp fillename username@ip_address
scp -i key.pem  filename username@ip_address  
# for directory, use the following
scp -r dirname username@ip_address 
scp -r -i key.pem filename username@ip_address 