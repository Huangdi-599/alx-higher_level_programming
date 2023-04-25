#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesFilms = films.filter((film) => {
    return film.characters.some((character) => character.endsWith('/18/'));
  });

  console.log(`Wedge Antilles appears in ${wedgeAntillesFilms.length} films.`);
});
