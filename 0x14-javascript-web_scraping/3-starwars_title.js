#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`,
(error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
