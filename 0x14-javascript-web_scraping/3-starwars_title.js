#!/usr/bin/node
//a script that prints the title of a Star Wars movie
const request = require('request');

const movieId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`,
(error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});
