// sudo npm install request

var request = require('request');

request({
  //this disables the ssl security (would accept a fake certificate). see:
  //http://stackoverflow.com/questions/20082893/unable-to-verify-leaf-signature
  "rejectUnauthorized": false,
  "url": 'https://api.tnyu.org/v3/people',
  "headers": {
    "content-type": "application/vnd.api+json",
    "accept": "application/*, text/html, */*",
    "authorization": "Bearer " + process.env.TNYU_API_KEY
  },
  timeout: 100000
}, function(err, response, body){
    var apiJson = JSON.parse(body),
        events = apiJson["data"];
    console.log(events[0]); // print out the first events
});