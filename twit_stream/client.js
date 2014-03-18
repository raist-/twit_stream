var client = function (socket) {

    var socket = socket;
    var redis = require("redis");
    var client1 = redis.createClient();
    var client2 = redis.createClient();


    client1.on("message", function (channel, message) {
        console.log("client1 channel " + channel + ": " + message);
        socket.emit('message', { message: message });
        if (message === 'END') {
            client1.unsubscribe();
            client1.end();
        }
    });


/*    var request = {
	method : "statuses/filter",
	param_dict : {"locations":"-74,40,-73,41"},
	channel : "test_channel"
    }
*/

    this.push_request = function(request) {
	var json = JSON.stringify(request);
	console.log('JSON STRINGIFY???' + json);
	console.log(request);
	client2.lpush('twitter_requests', json, function(err, reply) {} );
	client1.subscribe("test_channel");
    };

};

module.exports = client;

