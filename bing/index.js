var request = require("request");



let https = require('https');

//**********************************************
// *** Update or verify the following values. ***
// **********************************************

// Replace the subscriptionKey string value with your valid subscription key.
var subscriptionKey = '3b061a1ada8d4ceaa46154c363791098';
// Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
// search APIs.  In the future, regional endpoints may be available.  If you
// encounter unexpected authorization errors, double-check this host against
// the endpoint for your Bing Web search instance in your Azure dashboard.
let host = 'api.cognitive.microsoft.com';
let path = '/bing/v7.0/images/search';

let term = 'stained glass sheep';

function fn(offset) {
	if (offset >= 1500) {
		return;
	}

let response_handler = function (response) {
let body = '';
response.on('data', function (d) {
body += d;
});
response.on('end', function () {
//console.log('\nRelevant Headers:\n');
//for (var header in response.headers)
// header keys are lower-cased by Node.js
/*if (header.startsWith("bingapis-") || header.startsWith("x-msedge-"))
console.log(header + ": " + response.headers[header]);*/
let vv = JSON.parse(body).value;
if (!vv) {
  return;
}
body = vv.map(
  (v) => v.thumbnailUrl	
).join("\n");
//console.log('\nJSON Response:\n');
console.log(body);
});
response.on('error', function (e) {
console.log('Error: ' + e.message);
});
};

let bing_web_search = function (search) {
//console.log('Searching the Web for: ' + term);
let request_params = {
method : 'GET',
hostname : host,
path : path + '?offset=' + offset + '&count=150&q=' + encodeURIComponent(search),
headers : {
'Ocp-Apim-Subscription-Key' : subscriptionKey,
}
};

let req = https.request(request_params, response_handler);
req.end();

fn(offset + 150);
}

if (subscriptionKey.length === 32) {
bing_web_search(term);
} else {
console.log('Invalid Bing Search API subscription key!');
console.log('Please paste yours into the source code.');
}

}

fn(0);
