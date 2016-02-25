var request = require('request');

var addToSlack = function(person) {
    if (person['attributes'] && person['attributes']['contact'] && person['attributes']['contact']['email']) {
        request.post({
            url: 'https://technyucommunity.slack.com/api/users.admin.invite',
            form: {
                email: person['attributes']['contact']['email'],
                token: process.env.TNYU_SLACK_TOKEN,
                set_active: true,
                extra_message: "Hi! You signed up for 'Backend Development With Node.js' event through our RSVP platform. We're inviting you to our Tech@NYU community slack that we will be using throughout our event. You'll be the first ones to try out our new platform! You'll be able to ask questions on installation problems before the event or questions during the event if you get stuck! You'll also always have access to the slack so you can ask us questions when you get stuck! Welcome to Tech@NYU!"
            }
        }, function(err, httpResponse, body) {
            if (err) {
                console.log(err);
            }
            if (!body['ok']) {
                console.log(person['attributes']['name']);
                console.log(body);
            }
        });
    }
}

var getEventData = function (EVENT_ID) {
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
    }, function(err, response, body) {
        var apiJson = JSON.parse(body),
            event = apiJson["data"],
            rsvps = apiJson["included"];

        rsvps.forEach(function(person) {
            addToSlack(person);
        });
    });
};

setInterval(function() {
  getEventData('56c29c57e7afddface1d78c8');
}, 5 * 60 * 1000);
