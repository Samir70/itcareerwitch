# Project setup

## install XAMPP
downloaded [installer](https://sourceforge.net/projects/xampp/files/latest/download)
installed to `C:\xampp`

- ran `\xampp\xampp_start.exe` by double clicking it.
- visited: `http://localhost/` saw the `xampp` start page

## geonames example
- copied contents of `geonamesExample.zip` to `C:\xampp\htdocs` (found that location in the `http://localhost/dashboard/faq.html` from the homepage)
- Then visited `http://localhost/geonamesExample/` to see their app.

## Adapting for countryCode

- Set up `url`  
```php
$url = 'http://api.geonames.org//countryCode?lat='.$_REQUEST["lat"].'&lng='.$_REQUEST["lng"].'&username=flightltd&type=JSON';

```
- Visited `http://localhost/samirBetmouni/libs/php/getCountryCode.php?lat=47.03&lng=10.2` 

- Had to set data to the whole of `$decode`

Now visiting `http://localhost/samirBetmouni/` and clicking the submit button gives us the data:

```json
{"languages":"kk,ru","distance":"0","countryCode":"KZ","countryName":"Kazakhstan"}
```

## Adapting for neighbours

- Back to select inputs to limit choices for country code
- Rest is similar to before

## Adapting for streetNameLookup

- Only needs a query