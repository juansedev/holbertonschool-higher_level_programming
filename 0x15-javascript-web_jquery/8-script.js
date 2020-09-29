document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    dataType: 'text',
    success: (data) => {
      for (const movie of data) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  });
});
