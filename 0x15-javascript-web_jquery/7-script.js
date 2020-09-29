document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    dataType: 'text',
    success: (data) => {
      $('DIV#character').text(JSON.parse(data).name);
    }
  });
});
