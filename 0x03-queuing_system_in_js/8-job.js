import { Queue, Job } from 'kue';

/**
 * creates jobs
 * @param {Job[]} jobs
 * @param {Queue} queue
 */
function createPushNotificationsJobs(jobs, queue){
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_3', jobInfo);

    job.on('enqueue', () => {
      console.log('Notification job created:', job.id);
    });
    job.on('complete', () => {
      console.log('Notification job', job.id, 'completed');
    });
    job.on('failed', (err) => {
      console.log('Notification job', job.id, 'failed:', err.message || err.toString());
    });
    job.on('progress', (progress, data) => {
      console.log('Notification job', job.id, `${progress}% complete`);
    });
    job.save();
  }
};

export default createPushNotificationsJobs;