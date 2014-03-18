
function initRequest(channel, method, param_dict) {

    return {
	
	channel : channel,
	method : method,
	// may pull the param dict into more granular parameters later and combine them into the dictionary in this method
	param_dict : param_dict
    }
}
