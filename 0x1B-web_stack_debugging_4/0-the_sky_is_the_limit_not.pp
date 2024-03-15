events {}
http {
     keepalive_timeout 30s;
     worker_processes auto;
     client_body_buffer_size 8k;
    client_header_buffer_size 1k;
    proxy_buffer_size 16k;
