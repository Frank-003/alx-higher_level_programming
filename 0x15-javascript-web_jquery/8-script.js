 $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        var movies = data.results;
        var $list = $("UL#list_movies");
        
        $.each(movies, function(index, movie) {
            $list.append("<li>" + movie.title + "</li>");
        });
