import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient();
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const reply = await getAsync(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
