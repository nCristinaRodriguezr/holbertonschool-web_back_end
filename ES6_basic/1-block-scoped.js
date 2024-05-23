export default function taskBlock(trueOrFalse) {
  const tasks = {
    task: false,
    task2: true
  };

  if (trueOrFalse) {
    tasks.task = true;
    tasks.task2 = false;
  }

  return [tasks.task, tasks.task2];
}