const ready = () => {
	login()
}

const login = () => {
	$('.signin .github-signin').click(github_oauth());
}
const github_oauth = ()=> {
  // // Requests an api, which retrieves the auth token
 // let github_auth_url = 'https://github.com/login/oauth/authorize'

  // $.ajax({
    // url: github_auth_url,
	// crossDomain: true,
	// contentType: "application/json",
	// dataType: "jsonp",
    // data: {
		// "client_id": "926a308eec433f17e3ff",
		// "scope": {"user": "email"}
	// },
    // success: function (data, textStatus, jQxhr) {
		// alert("hi")
      // }
	// })
	$('.signin .github-signin').on('click', function() {
		OAuth.initialize('gZeK0rjdjMpH70JACRM_kaKLUIc');
		// Use popup for OAuth
		OAuth.popup('github').then(github => {
			console.log(github);
			console.log(github.me());
		});
	})
}

document.addEventListener('DOMContentLoaded', ready);
