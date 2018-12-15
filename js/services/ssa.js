const querystring = require('querystring');
const https = require('https');


function life_expectancy(sex, year, month, day=1) {
    // birth year, month, day
    var url = "https://www.ssa.gov/cgi-bin/longevity.cgi"
    var payload = querystring.stringify({
        "sex": sex, // m, f
        "monthofbirth": month, // 0, 1, 2... 11
        "dayofbirth": day, // 1, 2...
        "yearofbirth": year // 1982
    })

    http.request({
        "hostname": "www.ssa.gov",
        "port": 443,
        "method": "POST"
        "path": "/cgi-bin/logevity.cgi",
        "agent": false
        "headers": {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Content-Length': payload.length
        }
      }, (res) => {
        console.log('statusCode:', res.statusCode);
        console.log('headers:', res.headers);

        res.on('data', (d) => {
          process.stdout.write(d);
        });

      });

}
