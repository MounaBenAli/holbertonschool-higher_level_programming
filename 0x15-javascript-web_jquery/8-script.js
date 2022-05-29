$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (data) {
    $.each(data.results, function (i, data) {
      $('UL#list_movies').append('<li>' + data.title + '</li>');
    });
  }
});
