import { createClient, print } from "redis";

const CHANNEL = 'holberton school channel';
const client = createClient();
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err}`));
client.on('ready', () => console.log('Redis client connected to the server'));

client.subscribe(CHANNEL);

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit()
  }
});
