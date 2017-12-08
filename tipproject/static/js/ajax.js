

search = function () {
    var keyword = document.querySelector('#search > input').getAttribute('value')
    var res = document.getElementById('refresh')
    $.ajax({
        url: 'https://www.baidu.com/s',
        method: 'GET',
        type: 'JSON',
        data: { wd: keyword },
    }).success(function (data) {
        alert(data)
    }).fail(function (data) {
        alert(data)
    })
}