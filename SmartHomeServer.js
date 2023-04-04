const env = require('dotenv').config();
const coffeescript = require('coffee-script/register');
const gapi = require('gapi');


gapi.load('client' , () => {
    gapi.client.init({
        apiKey:process.env.API_KEY,
        clientId:process.env.CLIENT_ID,
        scope:'https://www.googleapis.com/auth/homegraph',
        discoveryDocs:['https://homegraph.googleapis.com/$discovery/rest'],
    }).then(() => {
        gapi.auth2.getAuthInstance().signIn().then(() => {
            let access_token = gapi.auth2.getAuthInstance.currentUser.get();
            console.log(access_token);
        })
    })
})
