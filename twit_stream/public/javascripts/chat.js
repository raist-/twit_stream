

$(window).load(function() {

    var messages = [];
    var socket = io.connect('http://localhost:3000');
    var channel = $('#channel') 
    var request = $('#request')
    var params = $('#params')
    var sendButton = $("#send");
    var content = $("#content");
 
    socket.on('message', function (data) {
	console.log(data);
        content.append('<p>' + data.message + '</p>');
    });

    sendButton.on("click", function(event) {
	event.preventDefault();
	socket.emit('send', { channel: channel.val(), method: request.val(), param_dict: params.val() });
    });
});
