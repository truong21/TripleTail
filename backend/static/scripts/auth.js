const ready = () => {
	login()
}

const login = () => {
	$('.signin .github-signin').click(github_oauth());
}
const github_oauth = ()=> {
  // Requests an api, which retrieves the auth token
 let github_auth_url = `https://github.com/login/oauth/authorize`

  $.ajax({
    url: github_auth_url,
	crossDomain: true,
	dataType: "jsonp",
    data: {
		"client_id": "926a308eec433f17e3ff",
		"scope": {"user": "email"}
	},
    success: function (data, textStatus, jQxhr) {
		alert("hi")
      }
	})
}
document.addEventListener('DOMContentLoaded', ready);
