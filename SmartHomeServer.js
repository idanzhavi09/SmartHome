const { google } = require('googleapis');

// Set up the Home Graph API client
const homegraph = google.homegraph({
  version: 'v1',
  auth: '<YOUR_ACCESS_TOKEN>'
});
const getAuthToken = async() => {
    const getAuth = await fetch(`https://accounts.google.com/o/oauth2/auth?client_id=${process.env.CLIENT_ID}&redirect_uri=http://localhost:3000/auth/google/callback&response_type=code` , {
        method:'get', 
    }).then((res) => {
        console.log(res);
    })
}

getAuthToken();
