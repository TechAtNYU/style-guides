var request = require('request');

var EVENT_ID = '56c29c57e7afddface1d78c8';

request({
  //this disables the ssl security (would accept a fake certificate). see:
  //http://stackoverflow.com/questions/20082893/unable-to-verify-leaf-signature
  "rejectUnauthorized": false,
  "url": 'https://api.tnyu.org/v3/events/' + EVENT_ID + '?include=rsvps',
  "headers": {
    "content-type": "application/vnd.api+json",
    "accept": "application/*, text/html, */*",
    "authorization": "Bearer " + process.env.TNYU_API_KEY
  },
  timeout: 100000
}, function(err, response, body){
    var apiJson = JSON.parse(body),
        event = apiJson["data"],
        rsvps = apiJson["included"];
    console.log(event); // print out the first events
});