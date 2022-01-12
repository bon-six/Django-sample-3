LOGIN_URL=https://yourdjangowebsite.com/login/
YOUR_USER='username'
YOUR_PASS='password'
COOKIES=cookies.txt
CURL_BIN="curl -v -c $COOKIES -b $COOKIES -e "

Write-Output "Django Auth: get csrftoken ..."
$CURL_BIN $LOGIN_URL
DJANGO_TOKEN="csrfmiddlewaretoken=$(grep csrftoken $COOKIES | sed 's/^.*csrftoken\s*//')"

Write-Output " perform login ..."
$CURL_BIN `
    -d "$DJANGO_TOKEN&username=$YOUR_USER&password=$YOUR_PASS" `
    -X POST $LOGIN_URL

Write-Output " do something while logged in ..."
$CURL_BIN `
    -d "$DJANGO_TOKEN&..." `
    -X POST https://yourdjangowebsite.com/whatever/

Write-Output " logout"
Remove-Item $COOKIES