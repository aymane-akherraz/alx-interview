#!/usr/bin/node
const request = require('request');
const { promisify } = require('util');

const requestPromise = promisify(request);

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

const fetchAll = async () => {
  const { body } = await requestPromise(url);
  const film = JSON.parse(body);
  return film.characters;
};

const fetchCharacter = async (url) => {
  const { body } = await requestPromise(url);
  const character = JSON.parse(body);
  return character.name;
};

const main = async () => {
  const chars = await fetchAll();
  for (const charUrl of chars) {
    const characterName = await fetchCharacter(charUrl);
    console.log(characterName);
  }
};

main();
