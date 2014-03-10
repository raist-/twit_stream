var redis = require("redis");
var client1 = redis.createClient();
var client2 = redis.createClient();


client1.on("message", function (channel, message) {
        console.log("client1 channel " + channel + ": " + message);
        
        if (message === 'END') {
            client1.unsubscribe();
            client1.end();
        }
    });


    var request = {
	method : "statuses/filter",
	param_dict : {"locations":"-74,40,-73,41"},
	channel : "test_channel"
    }

    client2.lpush('twitter_requests', JSON.stringify(request), function(err, reply) {})
    client1.subscribe("test_channel");


var request = {

    method : "??",
    param_dict : {},
    channel : "channel?"


}
