import { createQueue } from 'kue';

const BLACK_LIST = ['4153518780', '4153518781'];
const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0);
  if (BLACK_LIST.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(0.5);
    console.log(
      `Sending notification to ${phoneNumber},`,
      'with message:',
      message,
    );
  }
};

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
