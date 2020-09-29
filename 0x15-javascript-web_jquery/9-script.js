document.addEventListener('DOMContentLoaded', function () {
  $.ajax({
	url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (data) => {
      $('div#hello').text(data.hello);
    }
  });
});
