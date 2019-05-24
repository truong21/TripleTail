const ready = () => {
	login()
}

const login = () => {
    $('.signin .github-signin').onclick(github_oauth());
}

const github_oauth = () => {
    // Requests an api, which retrieves the auth token
    
	window.location.href = "https://github.com/login/oauth/authorize?client_id=926a308eec433f17e3ff"
}

document.addEventListener('DOMContentLoaded', ready);
