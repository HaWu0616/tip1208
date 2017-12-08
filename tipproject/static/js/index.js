showTab = function (tabname, is_strong = false) {
    var login_form = document.getElementById('login-form')
    var reg_form = document.getElementById('reg-form')
    if (tabname === 'login') {
        login_form.classList.remove('sr-only')
        if (is_strong === true) strong()
    } else login_form.classList.add('sr-only')
    if (tabname === 'register') {
        reg_form.classList.remove('sr-only')
        if (is_strong === true) strong()
    } else reg_form.classList.add('sr-only')
}

strong = function () {
    var main = document.querySelector('.login > .login-main')
    main.classList.remove('strong')
    main.classList.add('strong')
}
