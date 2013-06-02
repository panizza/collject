// ######### PROBLEMI ###################

// Lista problemi

$(function() {
    listProblems("http://23.21.187.163/api/problem/list/", "problem");
});

/*
[{"description": "some roads near elementary school in New York are very dirty and needs to be cleaned out.", "title": "Dirty roads", "follower_count": 0, "hashtag": null, "owner": {"username": "admin", "skills": [], "id": 1, "img": "", "email": "p@p.it"}, "id": 1}, {"description": "We are trying to find some methods to help some children from Uganda to learn math.\r\nTheir parents begins to trust us and they let their kids come to our centre.\r\nRecently we received some founding to provide sme lessons math ma we don't know how to encourage them to study.", "title": "Math Lessons", "follower_count": 0, "hashtag": null, "owner": {"username": "admin", "skills": [], "id": 1, "img": "", "email": "p@p.it"}, "id": 2}]
*/

function listProblems(url, type) {
    /* http://23.21.187.163/api/problem/list/ */

    $.ajax({
            url: url,
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {


                str = '<div class="list" >';

                        $.each(data,function(i,j) {

                            str += '<section>';
                            str += '<h2 class="link" rel="' + j[i].id + ']" type="[' + type + '">' + j[i].title + '</h2>';
                            str += '<span class="skills">' + j[i].hashtag + '</span>';
                            str += '</section>';
                            str +=  '<span class="follow icon">&#10003;</span></section>';



                            // content = '<span>';
                            // content += j[i].follower_count;
                            // content += '<br />';
                            // content += j[i].description;
                            // content += '<br />';
                            // content += j[i].id;
                            // content += '<br />';
                            // content += j[i].title;
                            // content += '<br /></span>';
                        });

                str += '</div>'
                $('#content').append(str);
            }
        });
    });
}

function powa() {

    skill = "";
    skill + = '<span rel="[id]" type="[type]">[skill]</span>';

    <section>
    <aside class="link img" rel="[id]" type="user">
    <img class="left" src="[src]" />
    </aside>
    <section>
    <h2 class="link" rel="[id]" type="[type]">[app]</h2>
    <span class="skills">[hacks]</span>
    </section>
    <span class="icon">&#10003;</span>
    </section>
}

// Info su un problema

function getInfoAboutProblem(int id) {

    $.ajax({
            url: 'http://23.21.187.163/api/problem/' + id + '/info/',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j) {
                            content = '<span>';
                            content += j[i].owner;
                            content += '<br />';
                            content += j[i].description;
                            content += '<br />';

                            // Scorro followers
                            content += 'followers: ';
                            $.each(j[i].follower, function(index, value) {
                                content += value;
                                content += '<br />';
                            });

                            content += j[i].title;
                            content += '<br /></span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}

function getFollowersAboutProblem(int id) {

    $.ajax({
            url: 'http://23.21.187.163/api/problem/' + id + '/follower/',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j) {

                            content = '<span>';
                            content += j[i].id;
                            content += '<br />';
                            content += j[i].email;
                            content += '</span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}

// ############# SOLUZIONI ################

// Lista soluzioni

function listSolutions() {

    $.ajax({
            url: 'http://23.21.187.163/api/solution/list/',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j) {

                            content = '<span>';
                            content += j[i].follower_count;
                            content += '<br />';
                            content += j[i].description;
                            content += '<br />';
                            content += j[i].creation_date;
                            content += '<br />';
                            content += j[i].id;
                            content += '<br />';
                            content += j[i].problem_id;
                            content += '<br /></span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}


function getInfoAboutSolution(int id) {

    $.ajax({
            url: 'http://23.21.187.163/api/solution/' + id + '/info',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j) {

                            content = '<span>';

                            // Scorro followers
                            content += 'followers: ';
                            $.each(j[i].follower, function(index, value) {
                                content += value;
                                content += '<br />';
                            });

                            content += j[i].problem;
                            content += '<br />';
                            content += j[i].description;
                            content += '<br />';
                            content += j[i].id;
                            content += '<br />';
                            content += j[i].user;
                            content += '<br /></span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}

function getFollowersAboutSolution(int id) {

    $.ajax({
            url: 'http://23.21.187.163/api/solution/' + id + '/follower/',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j) {

                            content = '<span>';
                            content += j[i].id;
                            content += '<br />';
                            content += j[i].email;
                            content += '<br /></span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}

// Lista progetti

function listProjects() {

    $.ajax({
            url: 'http://23.21.187.163/api/project/list/',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j){

                            content = '<span>';
                            content += j[i].description;
                            content += '<br />';
                            content += j[i].img;
                            content += '<br />';
                            content += j[i].title;
                            content += '<br />';
                            content += j[i].longitude;
                            content += '<br />';
                            content += j[i].creation_date;
                            content += '<br />';
                            content += j[i].follower_count;
                            content += '<br />';
                            content += j[i].user;
                            content += '<br />';
                            content += j[i].latitude;
                            content += '<br />';
                            content += j[i].id;
                            content += '<br /></span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}

function getInfoAboutProject(int id) {

    $.ajax({
            url: 'http://23.21.187.163/api/project/' + id +'/info/',
            type: "GET",
            data: "",
            dataType: 'json',
            success: function (data) {
                        $.each(data,function(i,j){

                            content = '<span>';
                            content += j[i].description;
                            content += '<br />';
                            content += j[i].title;
                            content += '<br />';
                            content += j[i].solution;
                            content += '<br />';
                            content += j[i].longitude;
                            content += '<br />';

                            // Scorro followers
                            content += 'followers: ';
                            $.each(j[i].follower, function(index, value) {
                                content += value;
                                content += '<br />';
                            });

                            content += j[i].user;
                            content += '<br />';
                            content += j[i].latitude;
                            content += '<br />';
                            content += j[i].skill;
                            content += '<br />';
                            content += j[i].id;
                            content += '<br /></span>';
                            $('#response').append(content);
                        });
            }
        });
    });
}

function getFollowersAboutProject(int id) {

$.ajax({
        url: 'http://23.21.187.163/api/project/' + id +'/follower/',
        type: "GET",
        data: "",
        dataType: 'json',
        success: function (data) {
                    $.each(data,function(i,j){

                        content = '<span>';
                        content += j[i].id;
                        content += '<br />';
                        content += j[i].email;
                        content += '<br /></span>';
                        $('#response').append(content);
                    });
        }
    });
});