$(document).ready(function() {
  $('#btn_translate').click(function() {
    const langCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(url, { lang: langCode }, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
