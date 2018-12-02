var request = require('request');

function chara_name(body) {
    var chara_name_dict = {};
    for (key in body) {
        chara_name_dict[key] = body[key]['name'];
    }
    return chara_name_dict;
}

function print_chara_mames(chara_dict) {
    for (key in chara_dict) {
        console.log(key + " : " + chara_dict[key]);
    }
}

function do_task(body) {
    var ret = chara_name(body);
    print_chara_mames(ret);
}

request.get(
    {
        url: 'https://prickathon.github.io/webapi-mock-up/characters.json',
        headers: {
            'Content-Type': 'application/json'
        },
        json: true,
    }, function (error, response, body) {
        if (error) {
            console.log(error);
            return;
        }
        console.log(response.statusCode);
        do_task(body)
    }
)

