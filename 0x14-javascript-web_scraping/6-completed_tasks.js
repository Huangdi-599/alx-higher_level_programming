#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, { json: true }, (err, res, data) => {
  if (err) {
    return console.log(err);
  }

  const tasksByUser = {};

  data.forEach(task => {
    if (task.completed) {
      if (!tasksByUser[task.userId]) {
        tasksByUser[task.userId] = 0;
      }
      tasksByUser[task.userId]++;
    }
  });

  for (const [userId, numTasks] of Object.entries(tasksByUser)) {
    console.log(`User ${userId} completed ${numTasks} tasks.`);
  }
});
